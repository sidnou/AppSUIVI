import customtkinter
import os
import re
from datetime import date
from gen_pdf import GenPdf

# Imports conditionnels pour Windows
try:
    import win32print
    import win32api
    WINDOWS_PRINTING = True
except ImportError:
    print("Modules win32 non disponibles - impression désactivée")
    WINDOWS_PRINTING = False

VERSION = "1.0.2b - ZEBRA DS2278"
NOMBRE_SAISI = 60  # Nombre total de champs de saisie

# Configuration spécifique au ZEBRA DS2278
ZEBRA_CONFIG = {
    'scan_delay': 100,  # Délai en ms après scan pour traitement
    'auto_advance_delay': 50,  # Délai avant passage au champ suivant
    'min_scan_length': 8,  # Longueur minimum d'un scan valide
    'max_scan_length': 13,  # Longueur maximum d'un scan valide
    'sound_feedback': True,  # Feedback sonore (si disponible)
    'qr_parsing': True  # Analyse des QR codes structurés
}

# Patterns pour extraction des données QR
QR_PATTERNS = {
    'chronopost_tracking': r'([A-Z]{2}\d{11,12}[A-Z]{2})',  # Format XS381054923248GE
    'dossier_number': r'(M\d{2}[A-Z]-\d{4}-\d{5})',  # Format M67S-2510-00707
    'alternative_dossier': r'([A-Z]\d{2}[A-Z]-\d{4}-\d{5})'  # Autres formats possibles
}


class ChronopostApp:
    def __init__(self):
        self.entries = []
        self.nColis_var = None
        self.current_entry_index = 0  # Index de l'entrée actuelle pour la douchette
        self.auto_advance = True  # Navigation automatique
        self.last_scan_time = 0  # Timestamp du dernier scan
        self.zebra_scan_buffer = ""  # Buffer pour les scans Zebra
        self.scan_in_progress = False  # Flag pour éviter les doublons
        self.dossier_numbers = []  # Liste des numéros de dossier extraits
        self.setup_ui()

    def parse_qr_code(self, qr_content):
        """Parse le contenu d'un QR code pour extraire le numéro de suivi et le dossier"""
        result = {
            'tracking_number': None,
            'dossier_number': None,
            'raw_content': qr_content,
            'is_qr_code': len(qr_content) > 50  # QR codes sont généralement longs
        }
        
        try:
            # Recherche du numéro de suivi Chronopost
            tracking_match = re.search(QR_PATTERNS['chronopost_tracking'], qr_content)
            if tracking_match:
                full_tracking = tracking_match.group(1)
                # Extraire les 13 premiers caractères (format standard Chronopost)
                result['tracking_number'] = full_tracking[:13]
            
            # Recherche du numéro de dossier
            dossier_match = re.search(QR_PATTERNS['dossier_number'], qr_content)
            if not dossier_match:
                # Essayer le pattern alternatif
                dossier_match = re.search(QR_PATTERNS['alternative_dossier'], qr_content)
            
            if dossier_match:
                result['dossier_number'] = dossier_match.group(1)
            
            return result
            
        except Exception as e:
            print(f"Erreur lors du parsing QR: {e}")
            return result

    def show_qr_parse_result(self, parse_result, entry_index):
        """Affiche le résultat du parsing QR avec options"""
        if not parse_result['is_qr_code']:
            return False  # Pas un QR code, traitement normal
        
        colonne = (entry_index // 20) + 1
        ligne = (entry_index % 20) + 1
        
        # Créer une fenêtre de résultat QR
        qr_window = customtkinter.CTkToplevel(self.fenetre)
        qr_window.title("QR Code détecté")
        qr_window.geometry("500x400")
        qr_window.transient(self.fenetre)
        qr_window.grab_set()
        
        # Frame principal
        main_frame = customtkinter.CTkScrollableFrame(qr_window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Titre
        title_label = customtkinter.CTkLabel(
            main_frame,
            text=f"🔍 QR Code scanné - Position L{ligne:02d}-C{colonne}",
            font=customtkinter.CTkFont(size=16, weight="bold"),
            text_color="#4ECDC4"
        )
        title_label.pack(pady=10)
        
        # Informations extraites
        if parse_result['tracking_number']:
            tracking_frame = customtkinter.CTkFrame(main_frame)
            tracking_frame.pack(fill="x", padx=10, pady=5)
            
            customtkinter.CTkLabel(
                tracking_frame,
                text="📦 Numéro de suivi Chronopost:",
                font=customtkinter.CTkFont(size=12, weight="bold")
            ).pack(anchor="w", padx=10, pady=5)
            
            tracking_label = customtkinter.CTkLabel(
                tracking_frame,
                text=parse_result['tracking_number'],
                font=customtkinter.CTkFont(size=14, weight="bold"),
                text_color="#00FF00"
            )
            tracking_label.pack(anchor="w", padx=20, pady=5)
        
        if parse_result['dossier_number']:
            dossier_frame = customtkinter.CTkFrame(main_frame)
            dossier_frame.pack(fill="x", padx=10, pady=5)
            
            customtkinter.CTkLabel(
                dossier_frame,
                text="📁 Numéro de dossier:",
                font=customtkinter.CTkFont(size=12, weight="bold")
            ).pack(anchor="w", padx=10, pady=5)
            
            dossier_label = customtkinter.CTkLabel(
                dossier_frame,
                text=parse_result['dossier_number'],
                font=customtkinter.CTkFont(size=14, weight="bold"),
                text_color="#FFD93D"
            )
            dossier_label.pack(anchor="w", padx=20, pady=5)
            
            # Stocker le numéro de dossier
            if parse_result['dossier_number'] not in self.dossier_numbers:
                self.dossier_numbers.append(parse_result['dossier_number'])
        
        # Boutons d'action
        button_frame = customtkinter.CTkFrame(main_frame)
        button_frame.pack(fill="x", padx=10, pady=20)
        
        def use_tracking():
            if parse_result['tracking_number']:
                self.entries[entry_index].delete(0, 'end')
                self.entries[entry_index].insert(0, parse_result['tracking_number'])
                qr_window.destroy()
                if self.auto_advance:
                    self.fenetre.after(100, self.advance_to_next_entry)
        
        def manual_entry():
            qr_window.destroy()
            # Effacer le champ pour saisie manuelle
            self.entries[entry_index].delete(0, 'end')
        
        if parse_result['tracking_number']:
            use_btn = customtkinter.CTkButton(
                button_frame,
                text="✅ Utiliser le numéro de suivi",
                command=use_tracking,
                fg_color="#1E8449",
                hover_color="#27AE60"
            )
            use_btn.pack(side="left", padx=5, pady=10)
        
        manual_btn = customtkinter.CTkButton(
            button_frame,
            text="✏️ Saisie manuelle",
            command=manual_entry,
            fg_color="#E74C3C",
            hover_color="#C0392B"
        )
        manual_btn.pack(side="right", padx=5, pady=10)
        
        # Affichage du contenu brut (optionnel)
        if len(parse_result['raw_content']) > 100:
            raw_frame = customtkinter.CTkFrame(main_frame)
            raw_frame.pack(fill="x", padx=10, pady=10)
            
            customtkinter.CTkLabel(
                raw_frame,
                text="📄 Contenu brut (extrait):",
                font=customtkinter.CTkFont(size=10)
            ).pack(anchor="w", padx=10, pady=5)
            
            raw_preview = parse_result['raw_content'][:200] + "..."
            customtkinter.CTkLabel(
                raw_frame,
                text=raw_preview,
                font=customtkinter.CTkFont(size=9),
                text_color="gray",
                wraplength=450
            ).pack(anchor="w", padx=10, pady=5)
        
        return True  # QR code traité

    def setup_ui(self):
        """Configuration de l'interface utilisateur"""
        # Configuration de l'apparence
        customtkinter.set_appearance_mode("dark")
        
        # Fenêtre principale
        self.fenetre = customtkinter.CTk()
        self.fenetre.title(f"Suivi Envoi Chronopost v{VERSION}")
        self.fenetre.geometry("1200x800+300+100")
        self.fenetre.minsize(1200, 800)
        
        # Gestion de l'icône
        self.load_icon()
        
        # Frame principal
        self.main_frame = customtkinter.CTkFrame(self.fenetre)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # En-tête avec compteur de colis et indicateur douchette
        self.create_header()
        
        # Contrôles spécifiques à la douchette
        self.create_scanner_controls()
        
        # Zone de saisie avec onglets
        self.create_input_area()
        
        # Boutons d'action
        self.create_buttons()
        
        # Focus sur la première entrée
        self.fenetre.after(100, self.focus_current_entry)
        
        # Raccourcis clavier pour la douchette
        self.setup_keyboard_shortcuts()

    def setup_keyboard_shortcuts(self):
        """Configure les raccourcis clavier"""
        # F1: Aller au premier champ vide
        self.fenetre.bind('<F1>', lambda e: self.go_to_first_empty())
        # F2: Basculer l'avancement automatique
        self.fenetre.bind('<F2>', lambda e: self.toggle_auto_advance())
        # F3: Aller au champ précédent
        self.fenetre.bind('<F3>', lambda e: self.go_to_previous_entry())
        # F4: Aller au champ suivant
        self.fenetre.bind('<F4>', lambda e: self.go_to_next_entry())
        # F5: Générer PDF
        self.fenetre.bind('<F5>', lambda e: self.generer_pdf())
        # Ctrl+E: Effacer tout
        self.fenetre.bind('<Control-e>', lambda e: self.effacer_tout())

    def load_icon(self):
        """Charge l'icône de l'application"""
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "chronopost.ico")
            if os.path.exists(icon_path):
                self.fenetre.iconbitmap(icon_path)
        except Exception as e:
            print(f"Erreur lors du chargement de l'icône: {e}")

    def create_header(self):
        """Crée l'en-tête avec le compteur de colis"""
        header_frame = customtkinter.CTkFrame(self.main_frame)
        header_frame.pack(fill="x", padx=10, pady=(10, 5))
        
        # Titre
        title_label = customtkinter.CTkLabel(
            header_frame, 
            text="Chronopost - Scanner ZEBRA DS2278",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title_label.pack(side="left", padx=20, pady=10)
        
        # Indicateur d'entrée actuelle
        self.current_entry_label = customtkinter.CTkLabel(
            header_frame,
            text="Entrée: L01-C1",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            text_color="#FFD93D"
        )
        self.current_entry_label.pack(side="left", padx=20, pady=10)
        
        # Bouton pour activer/désactiver l'avancement automatique
        self.auto_advance_btn = customtkinter.CTkButton(
            header_frame,
            text="Auto: ON",
            command=self.toggle_auto_advance,
            width=80,
            height=30,
            fg_color="#4ECDC4"
        )
        self.auto_advance_btn.pack(side="left", padx=10, pady=10)
        
        # Compteur de colis
        self.nColis_var = customtkinter.StringVar(value="0")
        colis_label = customtkinter.CTkLabel(
            header_frame, 
            text="Nombre de colis:",
            font=customtkinter.CTkFont(size=16, weight="bold")
        )
        colis_label.pack(side="right", padx=(20, 5), pady=10)
        
        self.colis_count_label = customtkinter.CTkLabel(
            header_frame, 
            text="0",
            font=customtkinter.CTkFont(size=16, weight="bold"),
            text_color="#00FF00"
        )
        self.colis_count_label.pack(side="right", padx=(5, 20), pady=10)

    def create_input_area(self):
        """Crée la zone de saisie avec onglets"""
        # TabView pour organiser les entrées
        self.tabview = customtkinter.CTkTabview(self.main_frame)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Créer 3 onglets pour 3 colonnes
        for i in range(3):
            tab_name = f"Colonne {i+1}"
            self.tabview.add(tab_name)
            
            # Frame scrollable pour chaque onglet
            scrollable_frame = customtkinter.CTkScrollableFrame(
                self.tabview.tab(tab_name),
                label_text=f"Numéros de suivi - {tab_name} (Lignes 1-20)"
            )
            scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Créer 20 entrées par colonne
            for j in range(20):
                entry_index = i * 20 + j
                
                # Frame pour chaque ligne avec numéro
                entry_frame = customtkinter.CTkFrame(scrollable_frame)
                entry_frame.pack(fill="x", padx=5, pady=2)
                
                # Label avec numéro de ligne
                line_label = customtkinter.CTkLabel(
                    entry_frame,
                    text=f"L{j+1:02d}:",
                    font=customtkinter.CTkFont(size=10, weight="bold"),
                    width=30
                )
                line_label.pack(side="left", padx=(5, 2), pady=5)
                
                entry = customtkinter.CTkEntry(
                    entry_frame,
                    placeholder_text=f"Scan ou tapez le numéro (max 13 car.)",
                    width=250,
                    font=customtkinter.CTkFont(size=12)
                )
                entry.pack(side="left", padx=(2, 5), pady=5, fill="x", expand=True)
                
                # Label pour afficher le nombre de caractères
                char_label = customtkinter.CTkLabel(
                    entry_frame,
                    text="0/13",
                    font=customtkinter.CTkFont(size=9),
                    width=40,
                    text_color="gray"
                )
                char_label.pack(side="right", padx=5, pady=5)
                
                # Binding spécialisé pour ZEBRA DS2278
                entry.bind('<KeyRelease>', lambda e, lbl=char_label, ent=entry, idx=entry_index: self.on_zebra_input(e, lbl, ent, idx))
                entry.bind('<Return>', lambda e, idx=entry_index: self.on_zebra_scan_complete(e, idx))
                entry.bind('<FocusIn>', lambda e, idx=entry_index: self.on_entry_focus(e, idx))
                # Binding pour détection de scan rapide (caractéristique du DS2278)
                entry.bind('<KeyPress>', lambda e, ent=entry, idx=entry_index: self.on_zebra_key_press(e, ent, idx))
                
                # Stocker les références
                self.entries.append(entry)
        
        # Sélectionner le premier onglet par défaut
        self.tabview.set("Colonne 1")

    def update_char_count(self, event, char_label, entry):
        """Met à jour le compteur de caractères pour une entrée"""
        current_length = len(entry.get())
        char_label.configure(text=f"{current_length}/13")
        
        # Changer la couleur selon la longueur
        if current_length > 13:
            char_label.configure(text_color="#FF6B6B")  # Rouge
        elif current_length == 13:
            char_label.configure(text_color="#4ECDC4")  # Vert
        elif current_length > 10:
            char_label.configure(text_color="#FFD93D")  # Jaune
        else:
            char_label.configure(text_color="gray")  # Gris

    def on_zebra_key_press(self, event, entry, entry_index):
        """Détecte le début d'un scan Zebra (saisie rapide)"""
        import time
        current_time = time.time() * 1000  # en millisecondes
        
        # Si c'est le premier caractère dans un délai court, c'est probablement un scan
        if not self.scan_in_progress and len(entry.get()) == 0:
            self.scan_in_progress = True
            self.last_scan_time = current_time
            self.zebra_scan_buffer = ""
            # Changer la couleur de fond pour indiquer un scan en cours
            entry.configure(fg_color="#2D3142")

    def on_zebra_input(self, event, char_label, entry, entry_index):
        """Gère la saisie spécialisée pour ZEBRA DS2278"""
        import time
        current_time = time.time() * 1000
        
        # Mettre à jour le compteur de caractères
        self.update_char_count(event, char_label, entry)
        
        # Détecter si c'est un scan (saisie rapide)
        if self.scan_in_progress:
            time_diff = current_time - self.last_scan_time
            if time_diff > 200:  # Plus de 200ms = saisie manuelle
                self.scan_in_progress = False
                entry.configure(fg_color=["#343638", "#212121"])  # Couleur normale
        
        # Valider toutes les entrées
        self.validate_input(event)

    def on_zebra_scan_complete(self, event, entry_index):
        """Gère la fin de scan ZEBRA DS2278 (touche Entrée automatique)"""
        current_entry = self.entries[entry_index]
        scanned_value = current_entry.get().strip()
        
        # Nettoyer la valeur (enlever les caractères de contrôle possibles)
        scanned_value = ''.join(char for char in scanned_value if char.isprintable())
        current_entry.delete(0, 'end')
        current_entry.insert(0, scanned_value)
        
        # Remettre la couleur normale
        current_entry.configure(fg_color=["#343638", "#212121"])
        self.scan_in_progress = False
        
        # Vérifier si c'est un QR code structuré
        if ZEBRA_CONFIG['qr_parsing'] and len(scanned_value) > 50:
            parse_result = self.parse_qr_code(scanned_value)
            if self.show_qr_parse_result(parse_result, entry_index):
                return  # QR code traité par la fenêtre spécialisée
        
        # Traitement normal pour codes-barres simples
        # Vérifier la longueur
        if len(scanned_value) < ZEBRA_CONFIG['min_scan_length']:
            colonne = (entry_index // 20) + 1
            ligne = (entry_index % 20) + 1
            self.show_error("Scan trop court", 
                          f"Le code scanné à la ligne {ligne}, colonne {colonne} est trop court.\n"
                          f"Longueur: {len(scanned_value)} caractères (minimum {ZEBRA_CONFIG['min_scan_length']})\n"
                          f"Valeur: '{scanned_value}'")
            current_entry.delete(0, 'end')
            return
        
        if len(scanned_value) > ZEBRA_CONFIG['max_scan_length']:
            colonne = (entry_index // 20) + 1
            ligne = (entry_index % 20) + 1
            self.show_error("Scan invalide", 
                          f"Le code scanné à la ligne {ligne}, colonne {colonne} dépasse {ZEBRA_CONFIG['max_scan_length']} caractères.\n"
                          f"Longueur: {len(scanned_value)} caractères\n"
                          f"Valeur: '{scanned_value}'")
            current_entry.delete(0, 'end')
            return
        
        # Vérifier les doublons en temps réel
        if self.check_duplicate_scan(scanned_value, entry_index):
            return
        
        # Feedback visuel de succès
        current_entry.configure(fg_color="#1B4D3E")  # Vert foncé pour succès
        self.fenetre.after(300, lambda: current_entry.configure(fg_color=["#343638", "#212121"]))
        
        # Si l'avancement automatique est activé
        if self.auto_advance and scanned_value:
            # Délai spécifique au DS2278 pour éviter les problèmes
            self.fenetre.after(ZEBRA_CONFIG['auto_advance_delay'], self.advance_to_next_entry)

    def check_duplicate_scan(self, value, current_index):
        """Vérifie les doublons en temps réel"""
        for i, entry in enumerate(self.entries):
            if i != current_index and entry.get().strip() == value:
                colonne_current = (current_index // 20) + 1
                ligne_current = (current_index % 20) + 1
                colonne_existing = (i // 20) + 1
                ligne_existing = (i % 20) + 1
                
                self.show_error("Doublon détecté", 
                              f"Le numéro '{value}' existe déjà !\n\n"
                              f"Position actuelle: Ligne {ligne_current}, Colonne {colonne_current}\n"
                              f"Position existante: Ligne {ligne_existing}, Colonne {colonne_existing}")
                
                self.entries[current_index].delete(0, 'end')
                return True
        return False

    def on_scan_complete(self, event, entry_index):
        """Gère la fin de scan d'une douchette (touche Entrée)"""
        current_entry = self.entries[entry_index]
        scanned_value = current_entry.get().strip()
        
        # Vérifier la longueur
        if len(scanned_value) > 13:
            colonne = (entry_index // 20) + 1
            ligne = (entry_index % 20) + 1
            self.show_error("Scan invalide", 
                          f"Le code scanné à la ligne {ligne}, colonne {colonne} dépasse 13 caractères.\n"
                          f"Longueur: {len(scanned_value)} caractères\n"
                          f"Valeur: {scanned_value}")
            # Effacer la valeur invalide
            current_entry.delete(0, 'end')
            return
        
        # Si l'avancement automatique est activé et qu'il y a une valeur
        if self.auto_advance and scanned_value:
            self.advance_to_next_entry()
    
    def on_entry_focus(self, event, entry_index):
        """Gère le focus sur une entrée"""
        self.current_entry_index = entry_index
        self.update_current_entry_indicator()
    
    def toggle_auto_advance(self):
        """Active/désactive l'avancement automatique"""
        self.auto_advance = not self.auto_advance
        if self.auto_advance:
            self.auto_advance_btn.configure(text="Auto: ON", fg_color="#4ECDC4")
        else:
            self.auto_advance_btn.configure(text="Auto: OFF", fg_color="#E74C3C")
    
    def focus_current_entry(self):
        """Met le focus sur l'entrée actuelle"""
        if 0 <= self.current_entry_index < len(self.entries):
            self.entries[self.current_entry_index].focus()
            self.update_current_entry_indicator()
            # Naviguer vers l'onglet correct
            colonne = (self.current_entry_index // 20) + 1
            self.tabview.set(f"Colonne {colonne}")
    
    def advance_to_next_entry(self):
        """Avance vers la prochaine entrée vide"""
        # Chercher la prochaine entrée vide
        for i in range(len(self.entries)):
            if not self.entries[i].get().strip():
                self.current_entry_index = i
                self.focus_current_entry()
                return
        
        # Si toutes les entrées sont remplies, rester sur la dernière
        self.current_entry_index = len(self.entries) - 1
        self.focus_current_entry()
    
    def update_current_entry_indicator(self):
        """Met à jour l'indicateur de l'entrée actuelle"""
        if 0 <= self.current_entry_index < len(self.entries):
            colonne = (self.current_entry_index // 20) + 1
            ligne = (self.current_entry_index % 20) + 1
            self.current_entry_label.configure(text=f"Entrée: L{ligne:02d}-C{colonne}")
    
    def create_scanner_controls(self):
        """Crée les contrôles spécifiques à la douchette"""
        scanner_frame = customtkinter.CTkFrame(self.main_frame)
        scanner_frame.pack(fill="x", padx=10, pady=5)
        
        # Instructions spécifiques au ZEBRA DS2278 avec QR codes
        instructions = customtkinter.CTkLabel(
            scanner_frame,
            text="📱 ZEBRA DS2278: Scannez QR codes ou codes-barres | Extraction auto des numéros de suivi | F1=Premier vide, F2=Auto, F5=PDF",
            font=customtkinter.CTkFont(size=11, weight="bold"),
            text_color="#4ECDC4"
        )
        instructions.pack(padx=10, pady=10)
        
        # Indicateurs d'état du scanner
        status_frame = customtkinter.CTkFrame(scanner_frame)
        status_frame.pack(pady=5)
        
        # Indicateur de scan en cours
        self.scan_status_label = customtkinter.CTkLabel(
            status_frame,
            text="🟢 Prêt à scanner",
            font=customtkinter.CTkFont(size=10, weight="bold"),
            text_color="#4ECDC4"
        )
        self.scan_status_label.pack(side="left", padx=10)
        
        # Compteur de scans valides
        self.scan_count_label = customtkinter.CTkLabel(
            status_frame,
            text="Scans: 0",
            font=customtkinter.CTkFont(size=10, weight="bold"),
            text_color="#FFD93D"
        )
        self.scan_count_label.pack(side="left", padx=10)
        
        # Boutons de navigation
        nav_frame = customtkinter.CTkFrame(scanner_frame)
        nav_frame.pack(pady=5)
        
        prev_btn = customtkinter.CTkButton(
            nav_frame,
            text="◀ Précédent",
            command=self.go_to_previous_entry,
            width=100
        )
        prev_btn.pack(side="left", padx=5)
        
        next_btn = customtkinter.CTkButton(
            nav_frame,
            text="Suivant ▶",
            command=self.go_to_next_entry,
            width=100
        )
        next_btn.pack(side="left", padx=5)
        
        first_empty_btn = customtkinter.CTkButton(
            nav_frame,
            text="🎯 Premier Vide",
            command=self.go_to_first_empty,
            width=120,
            fg_color="#FFD93D",
            text_color="black"
        )
        first_empty_btn.pack(side="left", padx=5)
        
        # Bouton pour voir les dossiers
        dossiers_btn = customtkinter.CTkButton(
            nav_frame,
            text="📁 Dossiers",
            command=self.show_dossiers,
            width=100,
            fg_color="#9B59B6",
            text_color="white"
        )
        dossiers_btn.pack(side="left", padx=5)
    
    def go_to_previous_entry(self):
        """Va à l'entrée précédente"""
        if self.current_entry_index > 0:
            self.current_entry_index -= 1
            self.focus_current_entry()
    
    def go_to_next_entry(self):
        """Va à l'entrée suivante"""
        if self.current_entry_index < len(self.entries) - 1:
            self.current_entry_index += 1
            self.focus_current_entry()
    
    def update_scan_status(self, status, color="#4ECDC4"):
        """Met à jour l'indicateur de statut du scanner"""
        if hasattr(self, 'scan_status_label'):
            self.scan_status_label.configure(text=status, text_color=color)
    
    def update_scan_count(self):
        """Met à jour le compteur de scans valides"""
        valid_scans = sum(1 for entry in self.entries if len(entry.get().strip()) >= ZEBRA_CONFIG['min_scan_length'])
        if hasattr(self, 'scan_count_label'):
            self.scan_count_label.configure(text=f"Scans: {valid_scans}")

    def show_dossiers(self):
        """Affiche la liste des numéros de dossier collectés"""
        dossier_window = customtkinter.CTkToplevel(self.fenetre)
        dossier_window.title("Numéros de dossier collectés")
        dossier_window.geometry("400x300")
        dossier_window.transient(self.fenetre)
        
        # Frame principal
        main_frame = customtkinter.CTkScrollableFrame(dossier_window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Titre
        title_label = customtkinter.CTkLabel(
            main_frame,
            text="📁 Numéros de dossier extraits des QR codes",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            text_color="#9B59B6"
        )
        title_label.pack(pady=10)
        
        if not self.dossier_numbers:
            # Aucun dossier trouvé
            no_dossier_label = customtkinter.CTkLabel(
                main_frame,
                text="Aucun numéro de dossier trouvé.\nScannez des QR codes pour voir les dossiers ici.",
                font=customtkinter.CTkFont(size=12),
                text_color="gray"
            )
            no_dossier_label.pack(pady=20)
        else:
            # Afficher la liste des dossiers
            for i, dossier in enumerate(self.dossier_numbers, 1):
                dossier_frame = customtkinter.CTkFrame(main_frame)
                dossier_frame.pack(fill="x", padx=10, pady=5)
                
                dossier_label = customtkinter.CTkLabel(
                    dossier_frame,
                    text=f"{i}. {dossier}",
                    font=customtkinter.CTkFont(size=12, weight="bold"),
                    text_color="#FFD93D"
                )
                dossier_label.pack(anchor="w", padx=10, pady=5)
        
        # Boutons
        button_frame = customtkinter.CTkFrame(main_frame)
        button_frame.pack(fill="x", padx=10, pady=20)
        
        def copy_dossiers():
            if self.dossier_numbers:
                dossiers_text = "\n".join(self.dossier_numbers)
                # Copier dans le presse-papier (si possible)
                try:
                    self.fenetre.clipboard_clear()
                    self.fenetre.clipboard_append(dossiers_text)
                    self.show_success("Copié", "Numéros de dossier copiés dans le presse-papier")
                except:
                    self.show_success("Liste des dossiers", dossiers_text)
        
        def clear_dossiers():
            self.dossier_numbers.clear()
            dossier_window.destroy()
            self.show_success("Effacé", "Liste des dossiers effacée")
        
        if self.dossier_numbers:
            copy_btn = customtkinter.CTkButton(
                button_frame,
                text="📋 Copier",
                command=copy_dossiers,
                width=100
            )
            copy_btn.pack(side="left", padx=5, pady=10)
            
            clear_btn = customtkinter.CTkButton(
                button_frame,
                text="🗑️ Effacer",
                command=clear_dossiers,
                width=100,
                fg_color="#E74C3C"
            )
            clear_btn.pack(side="right", padx=5, pady=10)
        
        close_btn = customtkinter.CTkButton(
            button_frame,
            text="Fermer",
            command=dossier_window.destroy,
            width=100
        )
        close_btn.pack(pady=10)

    def go_to_first_empty(self):
        """Va à la première entrée vide"""
        self.advance_to_next_entry()
        self.update_scan_status("🎯 Navigation vers premier vide", "#FFD93D")
        self.fenetre.after(2000, lambda: self.update_scan_status("🟢 Prêt à scanner"))

    def create_buttons(self):
        """Crée les boutons d'action"""
        button_frame = customtkinter.CTkFrame(self.main_frame)
        button_frame.pack(fill="x", padx=10, pady=(5, 10))
        
        # Bouton Générer PDF
        btn_pdf = customtkinter.CTkButton(
            button_frame,
            text="Générer PDF et Imprimer",
            command=self.generer_pdf,
            fg_color="#1E8449",
            hover_color="#27AE60",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            width=200,
            height=40
        )
        btn_pdf.pack(side="left", padx=20, pady=15)
        
        # Bouton Effacer
        btn_effacer = customtkinter.CTkButton(
            button_frame,
            text="Effacer tout",
            command=self.effacer_tout,
            fg_color="#E74C3C",
            hover_color="#C0392B",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            width=150,
            height=40
        )
        btn_effacer.pack(side="right", padx=20, pady=15)

    def validate_input(self, event=None):
        """Valide les entrées et met à jour le compteur"""
        # Compter les entrées non vides
        count = sum(1 for entry in self.entries if entry.get().strip())
        self.colis_count_label.configure(text=str(count))
        
        # Mettre à jour le compteur de scans valides
        self.update_scan_count()
        
        # Vérifier les doublons et la longueur
        entrees_values = [entry.get().strip() for entry in self.entries if entry.get().strip()]
        
        # Vérification de la longueur (pour saisie manuelle)
        for i, entry in enumerate(self.entries):
            value = entry.get().strip()
            if value and len(value) > ZEBRA_CONFIG['max_scan_length']:
                # Calculer la ligne et la colonne
                colonne = (i // 20) + 1  # 1, 2 ou 3
                ligne = (i % 20) + 1     # 1 à 20
                
                self.show_error("Erreur de saisie", 
                              f"Le numéro de suivi à la ligne {ligne}, colonne {colonne} dépasse {ZEBRA_CONFIG['max_scan_length']} caractères.\n"
                              f"Longueur actuelle: {len(value)} caractères\n"
                              f"Valeur: {value}")
                return
        
        # Vérification des doublons (pour affichage global)
        if len(entrees_values) != len(set(entrees_values)):
            doublons_info = self.find_duplicates_positions()
            if doublons_info:
                self.show_error("Doublons détectés", doublons_info)

    def find_duplicates_positions(self):
        """Trouve les doublons et retourne leurs positions"""
        value_positions = {}
        doublons = []
        
        for i, entry in enumerate(self.entries):
            value = entry.get().strip()
            if value:
                colonne = (i // 20) + 1
                ligne = (i % 20) + 1
                position = f"Ligne {ligne}, Colonne {colonne}"
                
                if value in value_positions:
                    # C'est un doublon
                    if value not in [d[0] for d in doublons]:
                        # Première fois qu'on trouve ce doublon
                        doublons.append((value, [value_positions[value], position]))
                    else:
                        # Ajouter cette position au doublon existant
                        for d in doublons:
                            if d[0] == value:
                                d[1].append(position)
                                break
                else:
                    value_positions[value] = position
        
        if doublons:
            message = "Les numéros suivants sont en double:\n\n"
            for value, positions in doublons:
                message += f"• '{value}' présent aux positions:\n"
                for pos in positions:
                    message += f"  - {pos}\n"
                message += "\n"
            return message
        
        return None

    def show_error(self, title, message):
        """Affiche une fenêtre d'erreur"""
        error_window = customtkinter.CTkToplevel(self.fenetre)
        error_window.title(title)
        
        # Calculer la taille de la fenêtre en fonction du message
        lines = message.count('\n') + 1
        width = max(400, min(800, len(message.split('\n')[0]) * 8))
        height = max(200, min(600, lines * 25 + 100))
        
        error_window.geometry(f"{width}x{height}")
        error_window.transient(self.fenetre)
        error_window.grab_set()
        
        # Frame scrollable pour les longs messages
        scrollable_frame = customtkinter.CTkScrollableFrame(error_window)
        scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Message d'erreur
        label = customtkinter.CTkLabel(
            scrollable_frame,
            text=message,
            font=customtkinter.CTkFont(size=12, weight="bold"),
            text_color="#FF6B6B",
            justify="left"
        )
        label.pack(padx=10, pady=10, anchor="w")
        
        # Frame pour le bouton
        button_frame = customtkinter.CTkFrame(error_window)
        button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Bouton OK
        ok_btn = customtkinter.CTkButton(
            button_frame,
            text="OK",
            command=error_window.destroy,
            width=100,
            fg_color="#E74C3C",
            hover_color="#C0392B"
        )
        ok_btn.pack(pady=10)

    def show_success(self, title, message):
        """Affiche une fenêtre de succès"""
        success_window = customtkinter.CTkToplevel(self.fenetre)
        success_window.title(title)
        success_window.geometry("400x150")
        success_window.transient(self.fenetre)
        success_window.grab_set()
        
        # Message de succès
        label = customtkinter.CTkLabel(
            success_window,
            text=message,
            font=customtkinter.CTkFont(size=12, weight="bold"),
            wraplength=350,
            text_color="#00FF00"
        )
        label.pack(padx=20, pady=20, expand=True)
        
        # Bouton OK
        ok_btn = customtkinter.CTkButton(
            success_window,
            text="OK",
            command=success_window.destroy,
            width=100
        )
        ok_btn.pack(pady=(0, 20))

    def generer_pdf(self):
        """Génère le PDF et l'imprime"""
        # Vérifier qu'il y a au moins une entrée
        entrees_values = [entry.get().strip() for entry in self.entries if entry.get().strip()]
        
        if not entrees_values:
            self.show_error("Erreur", "Aucun numéro de suivi saisi")
            return
        
        # Vérifier la longueur des numéros
        for i, entry in enumerate(self.entries):
            value = entry.get().strip()
            if value and len(value) > 13:
                colonne = (i // 20) + 1
                ligne = (i % 20) + 1
                self.show_error("Erreur de longueur", 
                              f"Le numéro de suivi à la ligne {ligne}, colonne {colonne} dépasse 13 caractères.\n"
                              f"Longueur actuelle: {len(value)} caractères\n"
                              f"Valeur: {value}")
                return
        
        # Vérifier les doublons
        doublons_info = self.find_duplicates_positions()
        if doublons_info:
            self.show_error("Doublons détectés", doublons_info)
            return
        
        try:
            # Préparer les données pour le PDF
            date_format_iso = date.today().isoformat()
            nom_fichier_pdf = f"Depart_Colis_Chronopost-{date_format_iso}.pdf"
            nombre_colis = len(entrees_values)
            
            # Organiser les données en 3 colonnes comme dans l'ancienne version
            donnees = [['Numéro de Suivi Chronopost', 'Numéro de Suivi Chronopost', 'Numéro de Suivi Chronopost']]
            
            for i in range(20):  # 20 lignes
                row = []
                for j in range(3):  # 3 colonnes
                    index = j * 20 + i
                    if index < len(self.entries):
                        value = self.entries[index].get().strip()
                        row.append(value)
                    else:
                        row.append("")
                donnees.append(row)
            
            # Générer le PDF
            pdf = GenPdf(donnees, nom_fichier_pdf, "RECUPERATION PAR CHRONOPOST", nombre_colis)
            pdf.generateur_pdf()
            
            # Tentative d'impression
            if WINDOWS_PRINTING:
                try:
                    printer_name = win32print.GetDefaultPrinter()
                    filepath = os.path.abspath(nom_fichier_pdf)
                    win32api.ShellExecute(0, "print", filepath, f'/d:"{printer_name}"', ".", 0)
                    self.show_success("Succès", f"PDF généré et envoyé à l'impression:\n{nom_fichier_pdf}")
                except Exception as e:
                    self.show_error("Erreur d'impression", 
                                  f"PDF généré: {nom_fichier_pdf}\nErreur d'impression: {e}")
            else:
                self.show_success("Succès", f"PDF généré avec succès:\n{nom_fichier_pdf}")
                
        except Exception as e:
            self.show_error("Erreur", f"Erreur lors de la génération du PDF:\n{e}")

    def effacer_tout(self):
        """Efface toutes les entrées"""
        for entry in self.entries:
            entry.delete(0, 'end')
        self.colis_count_label.configure(text="0")
        self.show_success("Information", "Toutes les entrées ont été effacées")

    def run(self):
        """Lance l'application"""
        self.fenetre.mainloop()


def main():
    """Fonction principale"""
    app = ChronopostApp()
    app.run()


if __name__ == "__main__":
    main()

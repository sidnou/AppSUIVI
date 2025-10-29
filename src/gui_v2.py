import customtkinter
import os
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

VERSION = "1.0.2b"
NOMBRE_SAISI = 60  # Nombre total de champs de saisie


class ChronopostApp:
    def __init__(self):
        self.entries = []
        self.nColis_var = None
        self.setup_ui()

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
        
        # En-tête avec compteur de colis
        self.create_header()
        
        # Zone de saisie avec onglets
        self.create_input_area()
        
        # Boutons d'action
        self.create_buttons()

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
            text="Application de Suivi Chronopost",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        title_label.pack(side="left", padx=20, pady=10)
        
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
                label_text=f"Numéros de suivi - {tab_name}"
            )
            scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Créer 20 entrées par colonne
            for j in range(20):
                entry_index = i * 20 + j
                entry = customtkinter.CTkEntry(
                    scrollable_frame,
                    placeholder_text=f"Numéro de suivi {entry_index + 1}",
                    width=300,
                    font=customtkinter.CTkFont(size=12)
                )
                entry.pack(padx=10, pady=3)
                entry.bind('<KeyRelease>', self.validate_input)
                self.entries.append(entry)
        
        # Sélectionner le premier onglet par défaut
        self.tabview.set("Colonne 1")

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
        
        # Vérifier les doublons et la longueur
        entrees_values = [entry.get().strip() for entry in self.entries if entry.get().strip()]
        
        # Vérification de la longueur (13 caractères)
        for entry in self.entries:
            value = entry.get().strip()
            if value and len(value) > 13:
                self.show_error("Erreur de saisie", 
                              "Les numéros de suivi doivent faire exactement 13 caractères")
                return
        
        # Vérification des doublons
        if len(entrees_values) != len(set(entrees_values)):
            # Il y a des doublons, mais on ne va pas montrer l'erreur à chaque frappe
            pass

    def show_error(self, title, message):
        """Affiche une fenêtre d'erreur"""
        error_window = customtkinter.CTkToplevel(self.fenetre)
        error_window.title(title)
        error_window.geometry("400x150")
        error_window.transient(self.fenetre)
        error_window.grab_set()
        
        # Message d'erreur
        label = customtkinter.CTkLabel(
            error_window,
            text=message,
            font=customtkinter.CTkFont(size=12, weight="bold"),
            wraplength=350
        )
        label.pack(padx=20, pady=20, expand=True)
        
        # Bouton OK
        ok_btn = customtkinter.CTkButton(
            error_window,
            text="OK",
            command=error_window.destroy,
            width=100
        )
        ok_btn.pack(pady=(0, 20))

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
        
        # Vérifier les doublons
        if len(entrees_values) != len(set(entrees_values)):
            self.show_error("Erreur", "Il y a des numéros de suivi en double")
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

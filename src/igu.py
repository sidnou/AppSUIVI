# Interface Graphique Utilisateur
# Version propre du code


import os
from logging import root
from tkinter import Tk, Entry
from tkinter import font
from datetime import date


COULEUR_AR_PLAN = "dodgerblue2"

"""
Description:
    Fenètre Principale :
        Dimension de l'interface graphique 
            - plein écran
        Il 4 Cadres :
            - Nombre colis
            - Tableau des numéro suivi
            - Groupe de boutons 
                * Imprimer
                * Effacer
            - Cellule de saisi de QrCode ou Manuel 
    Fenètre des Erreurs 
        Dimension:
            - 15% de la taille plein écran
        Type erreur:
            - Doublon
            - Aucun Numèro suivi trouver   

"""

#### Fenètre Principal
fenetre_principal = Tk()
largeur_ecran = fenetre_principal.winfo_screenwidth()
longeur_ecran = fenetre_principal.winfo_screenheight()
fenetre_principal.geometry(f"{largeur_ecran}x{longeur_ecran}")
fenetre_principal.title('Application Suivi Chronopost')
fenetre_principal.config(bg=COULEUR_AR_PLAN)
entree = Entry(fenetre_principal)
entree.grid(column=2,row=2)

print(largeur_ecran)













fenetre_principal.mainloop()
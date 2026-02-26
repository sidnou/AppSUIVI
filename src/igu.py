# Interface Graphique Utilisateur
# Version propre du code


import os
import tkinter as tk
from tkinter import font
from datetime import date


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
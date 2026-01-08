import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, Frame, StringVar
import tkinter.font as font
from gen_pdf import GenPdf
import os
from datetime import date
import win32print
import win32api

VERSION = "0.1.0"
BACKGROUND_GENERAL = "#2285D6"
DIMENSION_FENETRE_PRINCIPAL =  "1024x768"  
NOMBRE_SAISI = 60


################ Fenêtre Principale ###############
fenetre_main = tk.Tk()
# Titre de la fenêtre Principale
fenetre_main.title("Suivi Envoi Chronopost")
# Dimension fenêtre Principale
fenetre_main.geometry(DIMENSION_FENETRE_PRINCIPAL)
# Icone de la fenetre principale 
fenetre_main.iconbitmap("src/chronopost.ico")


##################### Boutons #####################
# Bouton Impression
# Bouton Effacement

fenetre_main.mainloop()
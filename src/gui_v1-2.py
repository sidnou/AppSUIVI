import tkinter 
from tkinter import Toplevel, Label, Button, Entry, Frame, StringVar
import tkinter.font as font
from gen_pdf import GenPdf
import os
from datetime import date
from sys import platform

if platform.capitalize() == 'Windows':
    import win32print
    import win32api




VERSION = "0.1.0"
BACKGROUND_GENERAL = "#2285D6"
DIMENSION_FENETRE_PRINCIPAL =  "1024x768"
DIM_LISTE = [1920,1024] # Dimension en liste   
NOMBRE_SAISI = 60


################ Fenêtre Principale ###############
# Configuration 
fenetre_main = tkinter.Tk()
fenetre_main.attributes('-fullscreen',True) # Mode plein écran
# Titre de la fenêtre Principale
fenetre_main.title("Suivi Envoi Chronopost")
# Dimension fenêtre Principale
fenetre_main.geometry(DIMENSION_FENETRE_PRINCIPAL)
# Taille de la fenêtre principale 
fenetre_main.minsize(DIM_LISTE[0],DIM_LISTE[1])
fenetre_main.maxsize(DIM_LISTE[0],DIM_LISTE[1])
# Icone de la fenetre principale 
# fenetre_main.iconbitmap(r"src\chronopost.ico") # todo : Ne fonction pas sur linux 
# Fond ecran 
fenetre_main.config(background=BACKGROUND_GENERAL)
# A propos de l'application
label_version = Label(fenetre_main, text=VERSION, background=BACKGROUND_GENERAL,fg="white",font=("Helvetica", 11,"bold"))
label_version.place(x=1880,y=1060)

# Cadre
cadre = Frame(fenetre_main, width=1300, height=800, relief="solid", bd=1)
cadre.pack(expand=True)

# Cadre pour nombre de colis scanné 
card_nombre_colis = Frame(fenetre_main, width=200, height=200.00)
card_nombre_colis.place(x=1700,y=200)
label_card_colis = Label(card_nombre_colis,text="Nombre de Colis",font=('Couriel', 14,"bold"))
label_card_colis.place(x=10,y=10)
nombre_colis = StringVar()
nombre_colis.set("O")
label_nombre_colis = Label(card_nombre_colis ,textvariable=nombre_colis,font=("Couriel", 50,"bold"))
label_nombre_colis.place(x=60,y=50)

##################### Boutons #####################
# Bouton Impression
btn_imp = Button(fenetre_main,text="Impression",bg="#0DE019",fg='white', width=30,border=0.5, font=("Couriel", 15 ,"bold") )
btn_imp.pack()
# Bouton Effacement

fenetre_main.mainloop()
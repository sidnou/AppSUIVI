import tkinter 
from tkinter import Toplevel, Label, Button, Entry, Frame, StringVar
import tkinter.font as font
from gen_pdf import GenPdf
import os
from datetime import date
from sys import platform
from verif_scan import scan_verif
if platform.capitalize() == 'Windows':
    import win32print
    import win32api

from pprint import pprint



VERSION = "0.1.0"
BACKGROUND_GENERAL = "#2285D6"
DIMENSION_FENETRE_PRINCIPAL =  "1024x768"
DIM_LISTE = [1920,1024] # Dimension en liste   
NOMBRE_SAISI = 60

# Todo : Bug quand on saisi apartir de la  6ème celule . Gros ralentissement de l'application temps excution trop long , 
# quand il y a des espace entre les celules il insert None ou 0 en fonction de verifaction du numéro saisi. 



########## Fonction ###############
def valide_numero_suivi(*args):
    # print(scan_verif(str(numero_suivi[0].get())))
    # print(str(numero_suivi[0].get()))
    nombre_colis.set(str(sum(numero_suivi[nombre_saisi].get() != "" for nombre_saisi in range(NOMBRE_SAISI))))
    # print(nombre_colis.get())
    # print(len(numero_suivi))

    # TODO: Il faut une varable qui récupère la clé du dictionnaire grille dont il y a une numero suivi entrée 
    # cle_grille = [grille[10]]
    # print(cle_grille)

    # print(numero_suivi[10].get())

    pprint(args)
    
    for n in range(int(nombre_colis.get())):
    
        # print(n)
        if numero_suivi[n].get() != "" or numero_suivi[n].get() != None:
            numero_suivi[n].set(scan_verif(numero_suivi[n].get()))
            # print(numero_suivi[n].get())

    # TODO: Verification ligne vide 

    # TODO: Vérifiction de la longueur valeur scanner 

    # TODO: Vérification des doublon 
    ...


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

# Cadre des suivis Colis 
cadre = Frame(fenetre_main, width=1300, height=800, relief="solid", bd=1)
cadre.pack(expand=True)

numero_suivi = {}
for n in range(NOMBRE_SAISI):
    numero_suivi[n] = StringVar()
    numero_suivi[n].trace_add("write",valide_numero_suivi) ## TODO: Créer une fonction pour validé numéro suivi saisi par l'utilisateur 
    pprint(numero_suivi[n].get())
    

# Grille pour les entrées de numéro de suivi
grille = dict.fromkeys(list(range(0,NOMBRE_SAISI)))



# Boucle des entrée des numero_suivi
# Colone 1
for n in range(0,20):
    
    grille[n] = Entry(cadre,textvariable=numero_suivi[n],font=font.Font(family='arial', size=12,weight="bold"))
    grille[n].grid(row=n,column=0,sticky="W") # type: ignore

# Colone 2 
for n in range(20,40):
    
    grille[n] = Entry(cadre,textvariable=numero_suivi[n],font=font.Font(family='arial', size=12,weight="bold"))
    grille[n].grid(row=n - 20,column=1,sticky="W") # type: ignore
   
# Colone 3
for n in range(40,60):
    
    grille[n] = Entry(cadre,textvariable=numero_suivi[n],font=font.Font(family='arial', size=12,weight="bold"))
    grille[n].grid(row=n - 40,column=2,sticky="W") # type: ignore

# pprint(grille)

# Cadre pour nombre de colis scanné 
card_nombre_colis = Frame(fenetre_main, width=200, height=200.00)
card_nombre_colis.place(x=1700,y=200)
label_card_colis = Label(card_nombre_colis,text="Nombre de Colis",font=('Couriel', 14,"bold"))
label_card_colis.place(x=10,y=10)
nombre_colis = StringVar()
nombre_colis.set("0")
label_nombre_colis = Label(card_nombre_colis ,textvariable=nombre_colis,font=("Couriel", 50,"bold"))
if int(nombre_colis.get()) >= 10:
    label_nombre_colis.place(x=50,y=50)
elif int(nombre_colis.get()) >= 100:
    label_nombre_colis.place(x=40,y=50)
else:
    label_nombre_colis.place(x=60,y=50)

################### Fonction ##############
def quitter():
    fenetre_main.destroy()

##################### Boutons #####################
# Bouton Impression
btn_imp = Button(fenetre_main,text="Impression",bg="#0DE019",fg='white', width=30,border=0.5, font=("Couriel", 15 ,"bold") )
btn_imp.pack()
# Bouton Effacement
btn_eff = Button(fenetre_main,text="Tout Effacer",bg="red", fg='white',width=30,border=0.5,font=("Couriel", 15 ,"bold"))
btn_eff.pack()
# Bouton Quitter
btn_quitter = Button(fenetre_main,text="Quitter",bg="red", fg="white",width=10,border=0.5,command=quitter,font=("Couriel", 11 ,"bold") )
btn_quitter.place(x=1800,y=5)

fenetre_main.mainloop()
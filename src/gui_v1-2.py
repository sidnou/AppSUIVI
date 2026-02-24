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




VERSION = "0.1.0"
BACKGROUND_GENERAL = "#2285D6"
DIMENSION_FENETRE_PRINCIPAL =  "1024x768"
DIM_LISTE = [1920,1024] # Dimension en liste   
NOMBRE_SAISI = 60





########## Fonction ###############
def valide_numero_suivi(*args):
    # print(scan_verif(str(numero_suivi[0].get())))
    # print(str(numero_suivi[0].get()))
    nombre_colis.set(str(sum(numero_suivi[nombre_saisi].get() != "" for nombre_saisi in range(NOMBRE_SAISI))))
    print(nombre_colis.get())
    print(len(numero_suivi))
    for n in range(int(nombre_colis.get())):
        print(n)
        numero_suivi[n].set(scan_verif((numero_suivi[n].get())))
        print(numero_suivi[n].get())

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
    numero_suivi[n].trace("w",valide_numero_suivi) ## TODO: Créer une fonction pour validé numéro suivi saisi par l'utilisateur 
    

# Grille pour les entrées de numéro de suivi
grille = dict.fromkeys(list(range(15,NOMBRE_SAISI + 1)))
print(grille)


# Colone 1
entree1 = Entry(cadre, textvariable=numero_suivi[0],font=font.Font(family='arial', size=12,weight="bold"))
entree1.grid(row=0,column=0,sticky="W")
# entree1.bind("<Tab>")
entree2 = Entry(cadre,textvariable=numero_suivi[1],font=font.Font(family='arial', size=12,weight="bold"))
entree2.grid(row=1,column=0,sticky="W")
entree3 = Entry(cadre,textvariable=numero_suivi[2],font=font.Font(family='arial', size=12,weight="bold"))
entree3.grid(row=2,column=0,sticky="W")
entree4 = Entry(cadre,textvariable=numero_suivi[3],font=font.Font(family='arial', size=12,weight="bold"))                 
entree4.grid(row=3,column=0,sticky="W")
entree5 = Entry(cadre,textvariable=numero_suivi[4],font=font.Font(family='arial', size=12,weight="bold"))
entree5.grid(row=4,column=0,sticky="W")
entree6 = Entry(cadre,textvariable=numero_suivi[5],font=font.Font(family='arial', size=12,weight="bold"))
entree6.grid(row=5,column=0,sticky="W")
entree7 = Entry(cadre,textvariable=numero_suivi[6],font=font.Font(family='arial', size=12,weight="bold"))
entree7.grid(row=6,column=0,sticky="W")
entree8 = Entry(cadre,textvariable=numero_suivi[7],font=font.Font(family='arial', size=12,weight="bold"))
entree8.grid(row=7,column=0,sticky="W")
entree9 = Entry(cadre,textvariable=numero_suivi[8],font=font.Font(family='arial', size=12,weight="bold"))
entree9.grid(row=8,column=0,sticky="W")
entree10 = Entry(cadre,textvariable=numero_suivi[9],font=font.Font(family='arial', size=12,weight="bold"))
entree10.grid(row=9,column=0,sticky="W")
entree11 = Entry(cadre,textvariable=numero_suivi[10],font=font.Font(family='arial', size=12,weight="bold"))
entree11.grid(row=10,column=0,sticky="W")
entree12 = Entry(cadre,textvariable=numero_suivi[11],font=font.Font(family='arial', size=12,weight="bold"))
entree12.grid(row=11,column=0,sticky="W")
entree13 = Entry(cadre,textvariable=numero_suivi[12],font=font.Font(family='arial', size=12,weight="bold"))
entree13.grid(row=12,column=0,sticky="W")
entree14 = Entry(cadre,textvariable=numero_suivi[13],font=font.Font(family='arial', size=12,weight="bold"))
entree14.grid(row=13,column=0,sticky="W")
entree15 = Entry(cadre,textvariable=numero_suivi[14],font=font.Font(family='arial', size=12,weight="bold"))
entree15.grid(row=14,column=0,sticky="W")
# Colone 2 
# Boucle des entrée des numero_suivi

for n in range(15,30):
    
    grille[n] = Entry(cadre,textvariable=numero_suivi[n],font=font.Font(family='arial', size=12,weight="bold"))
    grille[n].grid(row=n - 15,column=1,sticky="W")
   
# Colone 3


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
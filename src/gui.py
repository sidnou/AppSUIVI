from tkinter import *
import tkinter.font as font
from gen_pdf import *
import win32print
import win32api
import os
from datetime import date

DATE_FORMAT_ISO = date.today().isoformat()
VERSION = "0.0.1b"
NOM_FICHIER_PDF = f"Depart_Colis_Chronopost-{DATE_FORMAT_ISO}.pdf"

# fenêtre
fenetre = Tk()
fenetre.title("Suivi Envoi Chronopost")  # Titre de la fenêtre
fenetre.geometry("800x600")  # Dimension de la fenêtre
# fenetre.iconbitmap() # Icone de l'application
fenetre.minsize(800, 600)
fenetre.maxsize(800, 600)
fenetre.config(background="#0072B5")
# Police  ou Font
MON_FONT = font.Font(family='Couriel', size=15,
                     weight="bold")  # Police du Text
MON_FONT_1 = font.Font(family='arial', size=12,
                       weight="bold")  # Police du Text
MON_FONT_2 = font.Font(family='arial', size=10,
                       weight="bold")  # Police du Text
# Version de l'application
labelVersion = Label(fenetre, text=VERSION, background="#0072B5")
labelVersion.place(x=760, y=0)
# Cadre
cadre = Frame(fenetre, width=100, height=700, relief="solid", bd=1)
cadre.pack(expand=YES)
cadre2 = Frame(fenetre, width=200, height=25)
cadre2.pack()
cadre3 = Frame(fenetre, width=200, height=25)
cadre3.pack()
# Numero de Suivi
NOMBRE_SAISI = 40
nSuivi = {saisi: StringVar() for saisi in range(NOMBRE_SAISI)}


entree1 = Entry(cadre, textvariable=nSuivi[0], font=MON_FONT_2)
entree1.grid(row=0, column=0, sticky="W")
entree2 = Entry(cadre, textvariable=nSuivi[1], font=MON_FONT_2)
entree2.grid(row=1, column=0, sticky="W")
entree3 = Entry(cadre, textvariable=nSuivi[2], font=MON_FONT_2)
entree3.grid(row=2, column=0, sticky="W")
entree4 = Entry(cadre, textvariable=nSuivi[3], font=MON_FONT_2)
entree4.grid(row=3, column=0, sticky="W")
entree5 = Entry(cadre, textvariable=nSuivi[4], font=MON_FONT_2)
entree5.grid(row=4, column=0, sticky="W")
entree6 = Entry(cadre, textvariable=nSuivi[5], font=MON_FONT_2)
entree6.grid(row=5, column=0, sticky="W")
entree7 = Entry(cadre, textvariable=nSuivi[6], font=MON_FONT_2)
entree7.grid(row=6, column=0, sticky="W")
entree8 = Entry(cadre, textvariable=nSuivi[7], font=MON_FONT_2)
entree8.grid(row=7, column=0, sticky="W")
entree9 = Entry(cadre, textvariable=nSuivi[8], font=MON_FONT_2)
entree9.grid(row=8, column=0, sticky="W")
entree10 = Entry(cadre, textvariable=nSuivi[9], font=MON_FONT_2)
entree10.grid(row=9, column=0, sticky="W")
entree11 = Entry(cadre, textvariable=nSuivi[10], font=MON_FONT_2)
entree11.grid(row=10, column=0, sticky="W")
entree12 = Entry(cadre, textvariable=nSuivi[11], font=MON_FONT_2)
entree12.grid(row=11, column=0, sticky="W")
entree13 = Entry(cadre, textvariable=nSuivi[12], font=MON_FONT_2)
entree13.grid(row=12, column=0, sticky="W")
entree14 = Entry(cadre, textvariable=nSuivi[13], font=MON_FONT_2)
entree14.grid(row=13, column=0, sticky="W")
entree15 = Entry(cadre, textvariable=nSuivi[14], font=MON_FONT_2)
entree15.grid(row=14, column=0, sticky="W")
entree16 = Entry(cadre, textvariable=nSuivi[15], font=MON_FONT_2)
entree16.grid(row=15, column=0, sticky="W")
entree17 = Entry(cadre, textvariable=nSuivi[16], font=MON_FONT_2)
entree17.grid(row=16, column=0, sticky="W")
entree18 = Entry(cadre, textvariable=nSuivi[17], font=MON_FONT_2)
entree18.grid(row=17, column=0, sticky="W")
entree19 = Entry(cadre, textvariable=nSuivi[18], font=MON_FONT_2)
entree19.grid(row=18, column=0, sticky="W")
entree20 = Entry(cadre, textvariable=nSuivi[19], font=MON_FONT_2)
entree20.grid(row=19, column=0, sticky="W")
entree21 = Entry(cadre, textvariable=nSuivi[20], font=MON_FONT_2)
entree21.grid(row=0, column=1, sticky="W")
entree22 = Entry(cadre, textvariable=nSuivi[21], font=MON_FONT_2)
entree22.grid(row=1, column=1, sticky="W")
entree23 = Entry(cadre, textvariable=nSuivi[22], font=MON_FONT_2)
entree23.grid(row=2, column=1, sticky="W")
entree24 = Entry(cadre, textvariable=nSuivi[23], font=MON_FONT_2)
entree24.grid(row=3, column=1, sticky="W")
entree25 = Entry(cadre, textvariable=nSuivi[24], font=MON_FONT_2)
entree25.grid(row=4, column=1, sticky="W")
entree26 = Entry(cadre, textvariable=nSuivi[25], font=MON_FONT_2)
entree26.grid(row=5, column=1, sticky="W")
entree27 = Entry(cadre, textvariable=nSuivi[26], font=MON_FONT_2)
entree27.grid(row=6, column=1, sticky="W")
entree28 = Entry(cadre, textvariable=nSuivi[27], font=MON_FONT_2)
entree28.grid(row=7, column=1, sticky="W")
entree29 = Entry(cadre, textvariable=nSuivi[28], font=MON_FONT_2)
entree29.grid(row=8, column=1, sticky="W")
entree30 = Entry(cadre, textvariable=nSuivi[29], font=MON_FONT_2)
entree30.grid(row=9, column=1, sticky="W")
entree31 = Entry(cadre, textvariable=nSuivi[30], font=MON_FONT_2)
entree31.grid(row=10, column=1, sticky="W")
entree32 = Entry(cadre, textvariable=nSuivi[31], font=MON_FONT_2)
entree32.grid(row=11, column=1, sticky="W")
entree33 = Entry(cadre, textvariable=nSuivi[32], font=MON_FONT_2)
entree33.grid(row=12, column=1, sticky="W")
entree34 = Entry(cadre, textvariable=nSuivi[33], font=MON_FONT_2)
entree34.grid(row=13, column=1, sticky="W")
entree35 = Entry(cadre, textvariable=nSuivi[34], font=MON_FONT_2)
entree35.grid(row=14, column=1, sticky="W")
entree36 = Entry(cadre, textvariable=nSuivi[35], font=MON_FONT_2)
entree36.grid(row=15, column=1, sticky="W")
entree37 = Entry(cadre, textvariable=nSuivi[36], font=MON_FONT_2)
entree37.grid(row=16, column=1, sticky="W")
entree38 = Entry(cadre, textvariable=nSuivi[37], font=MON_FONT_2)
entree38.grid(row=17, column=1, sticky="W")
entree39 = Entry(cadre, textvariable=nSuivi[38], font=MON_FONT_2)
entree39.grid(row=18, column=1, sticky="W")
entree40 = Entry(cadre, textvariable=nSuivi[39], font=MON_FONT_2)
entree40.grid(row=19, column=1, sticky="W")

label = Label(cadre2, text='Nombre de Colis:',
              background="#0072B5", font=MON_FONT)
nColis = StringVar()
nColis.set("0")
label1 = Label(cadre2, textvariable=nColis, font=MON_FONT_1)
label.pack(side=LEFT)
label1.pack(side=RIGHT)
valeurDoublon = StringVar()
valeurDoublon.set("0")
label2 = Label(cadre3, text='Valeurs en doublon',
               background="#0072B5", font=MON_FONT_1)
label2.pack(side=LEFT)
label3 = Label(cadre3, textvariable=valeurDoublon, font=MON_FONT_1)
label3.pack(side=RIGHT)
# Vérification des numèro suivi saisi pas de doublon


def verif_doublon():
    # Compte le colis saisi
    nc = sum(nSuivi[saisi].get() != "" for saisi in range(NOMBRE_SAISI))
    nColis.set(nc)
    # Verification des doublons
    doublon = set()
    entreeSaisi = []
    for n in range(NOMBRE_SAISI):
        # print(nc)
        # print(n)
        # print(nSuivi[n].get())
        if nSuivi[n].get() != "":
            entreeSaisi.append(nSuivi[n].get())
            print(entreeSaisi)
    # print(entreeSaisi)
    for el in entreeSaisi:
        if entreeSaisi.count(el) > 1:
            doublon.add(el)

    print(doublon)  # affichage des valeurs en doublons
    print(type(doublon))
    # if doublon == set():
    if not doublon:
        valeurDoublon.set("0")
    else:
        valeurDoublon.set(doublon)


# Impression de la feuille de suivi Chronopost
def impression():
    nc = sum(nSuivi[saisi].get() != "" for saisi in range(NOMBRE_SAISI))
    data = [
        ['Numéro de Suivi Chronopost', 'Numéro de Suivi Chronopost'],
        [nSuivi[0].get(), nSuivi[20].get()],
        [nSuivi[1].get(), nSuivi[21].get()],
        [nSuivi[2].get(), nSuivi[22].get()],
        [nSuivi[3].get(), nSuivi[23].get()],
        [nSuivi[4].get(), nSuivi[24].get()],
        [nSuivi[5].get(), nSuivi[25].get()],
        [nSuivi[6].get(), nSuivi[26].get()],
        [nSuivi[7].get(), nSuivi[27].get()],
        [nSuivi[8].get(), nSuivi[28].get()],
        [nSuivi[9].get(), nSuivi[29].get()],
        [nSuivi[10].get(), nSuivi[30].get()],
        [nSuivi[11].get(), nSuivi[31].get()],
        [nSuivi[12].get(), nSuivi[32].get()],
        [nSuivi[13].get(), nSuivi[33].get()],
        [nSuivi[14].get(), nSuivi[34].get()],
        [nSuivi[15].get(), nSuivi[35].get()],
        [nSuivi[16].get(), nSuivi[36].get()],
        [nSuivi[17].get(), nSuivi[37].get()],
        [nSuivi[18].get(), nSuivi[38].get()],
        [nSuivi[19].get(), nSuivi[39].get()]
    ]
    print(len(data))
    pdf = GenPdf(data, NOM_FICHIER_PDF, "Suivi Colis Chronopost", nc)
    pdf.generateur_pdf()

    # Impression du fichier PDF
    # Imprimez le PDF avec win32print
    printer_name = win32print.GetDefaultPrinter()
    filepath = os.path.abspath(NOM_FICHIER_PDF)
    win32api.ShellExecute(0, "print", filepath, f'/d:"{printer_name}"', ".", 0)
    print("Document imprimé!")
   

def effacerValeur():
    for n in range(NOMBRE_SAISI):
        nSuivi[n].set("")


# Bouton de vérification des doublons
bouton1 = Button(fenetre, text='Vérification', command=verif_doublon,
                 bg="#12D292", fg="white", font=MON_FONT, width=20)
bouton1.pack()
# Bouton d'Impression
bouton2 = Button(fenetre, text='Impression', command=impression,
                 bg='#DFA80B', fg="white", font=MON_FONT, width=20)
bouton2.pack()
# Bouton d'éffacement des valeurs saisis
bouton3 = Button(fenetre, text='Efface', command=effacerValeur,
                 bg='red', fg='white', font=MON_FONT, width=20)
bouton3.pack()

fenetre.mainloop()

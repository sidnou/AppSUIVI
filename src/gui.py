from tkinter import *
import tkinter.font as font
from gen_pdf import *
import win32print
import win32api
import os
from datetime import date

VERSION = "0.0.2b"
BACKGROUND_GENERAL = "#0072B5"
# fenêtre
fenetre = Tk()
fenetre.title("Suivi Envoi Chronopost")  # Titre de la fenêtre
fenetre.geometry("1024x768")  # Dimension de la fenêtre
# fenetre.iconbitmap("src\chronopost.ico") # Icone de l'application
fenetre.minsize(1024, 768)
fenetre.maxsize(1024, 768)
fenetre.config(background=BACKGROUND_GENERAL)
# Police  ou Font
MON_FONT = font.Font(family='Couriel', size=15,
                     weight="bold")  # Police du Text
MON_FONT_1 = font.Font(family='arial', size=12,
                       weight="bold")  # Police du Text
MON_FONT_2 = font.Font(family='arial', size=12,
                       weight="bold")  # Police du Text
# Police et coleur de font
FONT_TOP_WIND = font.Font(family="arial", size=20, weight="bold", slant="italic")
BG_TOP_WIND = "red"
FONT_COLOR = "white"

# Version de l'application
labelVersion = Label(fenetre, text=VERSION, background=BACKGROUND_GENERAL)
labelVersion.place(x=980)
# Cadre
cadre = Frame(fenetre, width=100, height=700, relief="solid", bd=1)
cadre.pack(expand=YES)
cadre2 = Frame(fenetre, width=200, height=25, background=BACKGROUND_GENERAL)
cadre2.pack()


# def verif_doublon():
#     # Compte le colis saisi
#     nColis.set(str(sum(nSuivi[s].get() != "" for s in range(NOMBRE_SAISI))))
#     entree_saisi = []
#     for n in range(NOMBRE_SAISI):
#         if nSuivi[n].get() != "":
#             entree_saisi.append(nSuivi[n].get())
#             print(type(entree_saisi))
#     if doublon := {el for el in entree_saisi if entree_saisi.count(el) > 1}:
#         valeurDoublon.set(str(tuple(doublon)))
#     else:
#         valeurDoublon.set("0")


# validation des saisis
def valide(*args):
    print(args)
    nColis.set(str(sum(nSuivi[sa].get() != "" for sa in range(NOMBRE_SAISI))))
    entree_saisi = []  # Les valeurs saisi
    # Boucle des valeurs saisi
    for n in range(NOMBRE_SAISI):
        if nSuivi[n].get() != "":  # Ignore les entrées vide ou ""
            entree_saisi.append(nSuivi[n].get())
            if len(nSuivi[n].get()) > 13:  # Affiche message d'erreur si la longeur ne correspond pas
                top_fenetre = Toplevel(fenetre)
                top_fenetre.config(background=BG_TOP_WIND)
                Label(top_fenetre, text="!!! Entrée N° suivi de 13 caractères !!!", background=BG_TOP_WIND,
                      font=FONT_TOP_WIND, fg=FONT_COLOR).pack(padx=5, pady=5)
                Button(top_fenetre, text='OK', command=top_fenetre.destroy).pack(padx=5, pady=5)



    # Vérification des doublon
    for ed in entree_saisi:  # Boucle des entrées saisi
        if entree_saisi.count(ed) > 1:  # vérification qu'il n'y a pas plus du 1 valeur saisi
            top_fenetre = Toplevel(fenetre)
            top_fenetre.config(background=BG_TOP_WIND)
            Label(top_fenetre, text="!!! Ce numéro de suivi est déja Saisi !!!", background=BG_TOP_WIND,
                  font=FONT_TOP_WIND, fg=FONT_COLOR).pack(padx=5, pady=5)
            Button(top_fenetre, text='OK', command=top_fenetre.destroy).pack(padx=5, pady=5)
            break

    # # Exemple de *args : XS124909456FR longeur 13
    # for s in range(NOMBRE_SAISI):
    #     print(nSuivi[s].get())
    #     print(len(nSuivi[s].get()))
    #     if len(nSuivi[s].get()) == 13:
    #         continue
    #     elif len(nSuivi[s].get()) > 13:
    #         top_fenetre1 = Toplevel(fenetre)
    #         Label(top_fenetre1, text="Entre un suivi de 13 caractères").pack(padx=5, pady=5)
    #         Button(top_fenetre1, text='OK', command=top_fenetre1.destroy).pack(padx=5, pady=5)
    #         return False
    #     elif len(nSuivi[s].get()) == 0:
    #         break
    # else:
    #     top_fenetre = Toplevel(fenetre)
    #     Label(top_fenetre, text="Entrée un suiuvi Valide").pack(padx=5, pady=5)
    #     Button(top_fenetre, text='OK', command=top_fenetre.destroy).pack(padx=5, pady=5)
    #     return False


# Numero de Suivi
NOMBRE_SAISI = 40
# nSuivi = {saisi: StringVar() for saisi in range(NOMBRE_SAISI)}
nSuivi = {}
for s in range(NOMBRE_SAISI):
    nSuivi[s] = StringVar()
    nSuivi[s].trace_variable("w", valide)

NOMBRE_LIGNE = 20
NOMBRE_COLONNE = 3
entreeSaisi = []

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
label1 = Label(cadre2, textvariable=nColis, font=MON_FONT_1, background=BACKGROUND_GENERAL)
label.pack(side=LEFT)
label1.pack(side=RIGHT)

# Vérification des numèro suivi saisi pas de doublon


# Impression de la feuille de suivi Chronopost
def impression():
    date_format_iso = date.today().isoformat()
    nom_fichier_pdf = f"Depart_Colis_Chronopost-{date_format_iso}.pdf"
    nombre_colis = sum(nSuivi[e].get() != "" for e in range(NOMBRE_SAISI))
    donnees = [
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

    pdf = GenPdf(donnees, nom_fichier_pdf, "Suivi Colis Chronopost", nombre_colis)
    pdf.generateur_pdf()

    # # Impression du fichier PDF
    # # Imprimez le PDF avec win32print
    printer_name = win32print.GetDefaultPrinter()
    filepath = os.path.abspath(nom_fichier_pdf)
    win32api.ShellExecute(0, "print", filepath, f'/d:"{printer_name}"', ".", 0)
    print("Document imprimé!")
    return 0


def effacer_valeur():
    for n in range(NOMBRE_SAISI):
        nSuivi[n].set("")


# Bouton d'Impression
bouton2 = Button(fenetre, text='Impression', command=impression,
                 bg='#DFA80B', fg="white", font=MON_FONT, width=20)
bouton2.pack()
# Bouton d'éffacement des valeurs saisis
bouton3 = Button(fenetre, text='Efface', command=effacer_valeur,
                 bg='red', fg='white', font=MON_FONT, width=20)
bouton3.pack()

fenetre.mainloop()

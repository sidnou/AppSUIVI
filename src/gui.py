from tkinter import *

#####################################################################
# ## Exemple
# # Code
# fenetre = Tk()
# fenetre.title("Interface Utilisateur")
# fenetre.geometry("600x600") # Dimension de la fenêtre
# # Label
# label = Label(fenetre, text="Bonjour le Monde")
# label.pack()
# # Canvas
# canvas = Canvas(fenetre,width=400,height=400,background='white')
# canvas.pack(side=TOP)

# # Bouton
# bouton = Button(fenetre,text="Impression")
# bouton.pack()

# # Entrée
# valeur = StringVar() # Déclaration de la valeur
# valeur.set("Valeur")
# entree = Entry(fenetre,textvariable=valeur,width=30)
# entree.pack()

# fenetre.mainloop()

######################################################################
######################################################################

fenetre = Tk()  # fenêtre

fenetre.title("Suivi Envoi Chronopost")  # Titre de la fenêtre

fenetre.geometry("600x850")  # Dimension de la fenêtre

cadre = Frame(fenetre, width=500, height=600, bg="white", relief="solid", bd=1)
cadre.place(x=50, y=20)
# cadre.pack()
# Saisi des numèros de suivi
nSuivi1 = StringVar()
nSuivi2 = StringVar()
nSuivi3 = StringVar()
nSuivi4 = StringVar()
nSuivi5 = StringVar()
nSuivi6 = StringVar()
nSuivi7 = StringVar()
nSuivi8 = StringVar()
nSuivi9 = StringVar()
nSuivi10 = StringVar()
nSuivi11 = StringVar()
nSuivi12 = StringVar()
nSuivi13 = StringVar()
nSuivi14 = StringVar()
nSuivi15 = StringVar()
nSuivi16 = StringVar()
nSuivi17 = StringVar()
nSuivi18 = StringVar()
nSuivi19 = StringVar()
nSuivi20 = StringVar()
nSuivi21 = StringVar()
nSuivi22 = StringVar()
nSuivi23 = StringVar()
nSuivi24 = StringVar()
nSuivi25 = StringVar()
nSuivi26 = StringVar()
nSuivi27 = StringVar()
nSuivi28 = StringVar()
nSuivi29 = StringVar()
nSuivi30 = StringVar()
nSuivi31 = StringVar()
nSuivi32 = StringVar()
nSuivi33 = StringVar()
nSuivi34 = StringVar()
nSuivi35 = StringVar()
nSuivi36 = StringVar()
nSuivi37 = StringVar()
nSuivi38 = StringVar()
nSuivi39 = StringVar()
nSuivi40 = StringVar()

entree1 = Entry(cadre, textvariable=nSuivi1)
entree1.pack()
entree2 = Entry(cadre, textvariable=nSuivi2)
entree2.pack()
entree3 = Entry(cadre, textvariable=nSuivi3)
entree3.pack()
entree4 = Entry(cadre, textvariable=nSuivi4)
entree4.pack()
entree5 = Entry(cadre, textvariable=nSuivi5)
entree5.pack()
entree6 = Entry(cadre, textvariable=nSuivi6)
entree6.pack()
entree7 = Entry(cadre, textvariable=nSuivi7)
entree7.pack()
entree8 = Entry(cadre, textvariable=nSuivi8)
entree8.pack()
entree9 = Entry(cadre, textvariable=nSuivi9)
entree9.pack()
entree10 = Entry(cadre, textvariable=nSuivi10)
entree10.pack()
entree11 = Entry(cadre, textvariable=nSuivi11)
entree11.pack()
entree12 = Entry(cadre, textvariable=nSuivi12)
entree12.pack()
entree13 = Entry(cadre, textvariable=nSuivi13)
entree13.pack()
entree14 = Entry(cadre, textvariable=nSuivi14)
entree14.pack()
entree15 = Entry(cadre, textvariable=nSuivi15)
entree15.pack()
entree16 = Entry(cadre, textvariable=nSuivi16)
entree16.pack()
entree17 = Entry(cadre, textvariable=nSuivi17)
entree17.pack()
entree18 = Entry(cadre, textvariable=nSuivi18)
entree18.pack()
entree19 = Entry(cadre, textvariable=nSuivi19)
entree19.pack()
entree20 = Entry(cadre, textvariable=nSuivi20)
entree20.pack()
entree21 = Entry(cadre, textvariable=nSuivi21)
entree21.pack()
entree22 = Entry(cadre, textvariable=nSuivi22)
entree22.pack()
entree23 = Entry(cadre, textvariable=nSuivi23)
entree23.pack()
entree24 = Entry(cadre, textvariable=nSuivi24)
entree24.pack()
entree25 = Entry(cadre, textvariable=nSuivi25)
entree25.pack()
entree26 = Entry(cadre, textvariable=nSuivi26)
entree26.pack()
entree27 = Entry(cadre, textvariable=nSuivi27)
entree27.pack()
entree28 = Entry(cadre, textvariable=nSuivi28)
entree28.pack()
entree29 = Entry(cadre, textvariable=nSuivi29)
entree29.pack()
entree30 = Entry(cadre, textvariable=nSuivi30)
entree30.pack()
entree31 = Entry(cadre, textvariable=nSuivi31)
entree31.pack()
entree32 = Entry(cadre, textvariable=nSuivi32)
entree32.pack()
entree33 = Entry(cadre, textvariable=nSuivi33)
entree33.pack()
entree34 = Entry(cadre, textvariable=nSuivi34)
entree34.pack()
entree35 = Entry(cadre, textvariable=nSuivi35)
entree35.pack()
entree36 = Entry(cadre, textvariable=nSuivi36)
entree36.pack()
entree37 = Entry(cadre, textvariable=nSuivi37)
entree37.pack()
entree38 = Entry(cadre, textvariable=nSuivi38)
entree38.pack()
entree39 = Entry(cadre, textvariable=nSuivi39)
entree39.pack()
entree40 = Entry(cadre, textvariable=nSuivi40)
entree40.pack()


def verif_doublon():
    print(nSuivi1.get())
    print(nSuivi2.get())


# Bouton de vérification des doublons
bouton1 = Button(fenetre, text='Vérification', command=verif_doublon)
bouton1.pack(side=BOTTOM)
bouton2 = Button(fenetre, text='Impression')
bouton2.pack(side=BOTTOM)

fenetre.mainloop()

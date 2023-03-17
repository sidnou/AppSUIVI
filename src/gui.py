from tkinter import *
import tkinter.font as font
VERSION = "0.0.1b"
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
# fenêtre 
fenetre = Tk()
fenetre.title("Suivi Envoi Chronopost")  # Titre de la fenêtre
fenetre.geometry("800x600")  # Dimension de la fenêtre
# fenetre.iconbitmap() # Icone de l'application 
fenetre.minsize(800, 600)
fenetre.maxsize(800,600)
fenetre.config(background="#0072B5")
# Version de l'application 
labelVersion = Label(fenetre,text=VERSION,background="#0072B5")
labelVersion.place(x=760,y=0)
# Cadre 
cadre = Frame(fenetre, width=100, height=700, bg="red", relief="solid", bd=1)
cadre.pack(expand=YES)
cadre2 = Frame(fenetre,width=100,height=50)
cadre2.pack()
# Numero de Suivi 
NOMBRE_SAISI = 40
nSuivi = {saisi: StringVar() for saisi in range(NOMBRE_SAISI)}
# nSuivi1 = StringVar()
# nSuivi2 = StringVar()
# nSuivi3 = StringVar()
# nSuivi4 = StringVar()
# nSuivi5 = StringVar()
# nSuivi6 = StringVar()
# nSuivi7 = StringVar()
# nSuivi8 = StringVar()
# nSuivi9 = StringVar()
# nSuivi10 = StringVar()
# nSuivi11 = StringVar()
# nSuivi12 = StringVar()
# nSuivi13 = StringVar()
# nSuivi14 = StringVar()
# nSuivi15 = StringVar()
# nSuivi16 = StringVar()
# nSuivi17 = StringVar()
# nSuivi18 = StringVar()
# nSuivi19 = StringVar()
# nSuivi20 = StringVar()
# nSuivi21 = StringVar()
# nSuivi22 = StringVar()
# nSuivi23 = StringVar()
# nSuivi24 = StringVar()
# nSuivi25 = StringVar()
# nSuivi26 = StringVar()
# nSuivi27 = StringVar()
# nSuivi28 = StringVar()
# nSuivi29 = StringVar()
# nSuivi30 = StringVar()
# nSuivi31 = StringVar()
# nSuivi32 = StringVar()
# nSuivi33 = StringVar()
# nSuivi34 = StringVar()
# nSuivi35 = StringVar()
# nSuivi36 = StringVar()
# nSuivi37 = StringVar()
# nSuivi38 = StringVar()
# nSuivi39 = StringVar()
# nSuivi40 = StringVar()

entree1 = Entry(cadre, textvariable=nSuivi[0])
entree1.grid(row=0, column=0, sticky="W")
entree2 = Entry(cadre, textvariable=nSuivi[1])
entree2.grid(row=1, column=0, sticky="W")
entree3 = Entry(cadre, textvariable=nSuivi[2])
entree3.grid(row=2, column=0, sticky="W")
entree4 = Entry(cadre, textvariable=nSuivi[3])
entree4.grid(row=3, column=0, sticky="W")
entree5 = Entry(cadre, textvariable=nSuivi[4])
entree5.grid(row=4, column=0, sticky="W")
entree6 = Entry(cadre, textvariable=nSuivi[5])
entree6.grid(row=5, column=0, sticky="W")
entree7 = Entry(cadre, textvariable=nSuivi[6])
entree7.grid(row=6, column=0, sticky="W")
entree8 = Entry(cadre, textvariable=nSuivi[7])
entree8.grid(row=7, column=0, sticky="W")
entree9 = Entry(cadre, textvariable=nSuivi[8])
entree9.grid(row=8, column=0, sticky="W")
entree10 = Entry(cadre, textvariable=nSuivi[9])
entree10.grid(row=9, column=0, sticky="W")
entree11 = Entry(cadre, textvariable=nSuivi[10])
entree11.grid(row=10, column=0, sticky="W")
entree12 = Entry(cadre, textvariable=nSuivi[11])
entree12.grid(row=11, column=0, sticky="W")
entree13 = Entry(cadre, textvariable=nSuivi[12])
entree13.grid(row=12, column=0, sticky="W")
entree14 = Entry(cadre, textvariable=nSuivi[13])
entree14.grid(row=13, column=0, sticky="W")
entree15 = Entry(cadre, textvariable=nSuivi[14])
entree15.grid(row=14, column=0, sticky="W")
entree16 = Entry(cadre, textvariable=nSuivi[15])
entree16.grid(row=15, column=0, sticky="W")
entree17 = Entry(cadre, textvariable=nSuivi[16])
entree17.grid(row=16, column=0, sticky="W")
entree18 = Entry(cadre, textvariable=nSuivi[17])
entree18.grid(row=17, column=0, sticky="W")
entree19 = Entry(cadre, textvariable=nSuivi[18])
entree19.grid(row=18, column=0, sticky="W")
entree20 = Entry(cadre, textvariable=nSuivi[19])
entree20.grid(row=19, column=0, sticky="W")
entree21 = Entry(cadre, textvariable=nSuivi[20])
entree21.grid(row=0, column=1, sticky="W")
entree22 = Entry(cadre, textvariable=nSuivi[21])
entree22.grid(row=1, column=1, sticky="W")
entree23 = Entry(cadre, textvariable=nSuivi[22])
entree23.grid(row=2, column=1, sticky="W")
entree24 = Entry(cadre, textvariable=nSuivi[23])
entree24.grid(row=3, column=1, sticky="W")
entree25 = Entry(cadre, textvariable=nSuivi[24])
entree25.grid(row=4, column=1, sticky="W")
entree26 = Entry(cadre, textvariable=nSuivi[25])
entree26.grid(row=5, column=1, sticky="W")
entree27 = Entry(cadre, textvariable=nSuivi[26])
entree27.grid(row=6, column=1, sticky="W")
entree28 = Entry(cadre, textvariable=nSuivi[27])
entree28.grid(row=7, column=1, sticky="W")
entree29 = Entry(cadre, textvariable=nSuivi[28])
entree29.grid(row=8, column=1, sticky="W")
entree30 = Entry(cadre, textvariable=nSuivi[29])
entree30.grid(row=9, column=1, sticky="W")
entree31 = Entry(cadre, textvariable=nSuivi[30])
entree31.grid(row=10, column=1, sticky="W")
entree32 = Entry(cadre, textvariable=nSuivi[31])
entree32.grid(row=11, column=1, sticky="W")
entree33 = Entry(cadre, textvariable=nSuivi[32])
entree33.grid(row=12, column=1, sticky="W")
entree34 = Entry(cadre, textvariable=nSuivi[33])
entree34.grid(row=13, column=1, sticky="W")
entree35 = Entry(cadre, textvariable=nSuivi[34])
entree35.grid(row=14, column=1, sticky="W")
entree36 = Entry(cadre, textvariable=nSuivi[35])
entree36.grid(row=15, column=1, sticky="W")
entree37 = Entry(cadre, textvariable=nSuivi[36])
entree37.grid(row=16, column=1, sticky="W")
entree38 = Entry(cadre, textvariable=nSuivi[37])
entree38.grid(row=17, column=1, sticky="W")
entree39 = Entry(cadre, textvariable=nSuivi[38])
entree39.grid(row=18, column=1, sticky="W")
entree40 = Entry(cadre, textvariable=nSuivi[39])
entree40.grid(row=19, column=1, sticky="W")

label = Label(cadre2,text='Nombre de Colis:')
nColis = StringVar()
nColis.set("0")
label1 = Label(cadre2,textvariable=nColis)
label.pack(side=LEFT)
label1.pack(side=RIGHT)

# Vérification des numèro suivi saisi pas de doublon
def verif_doublon():
    # Verification des doublons 
    
    
    # Compte le colis saisi
    nc = sum(nSuivi[saisi].get() != "" for saisi in range(NOMBRE_SAISI))
    nColis.set(nc)
    
        
            
         


# Impression de la feuille de suivi Chronopost
def impression():
    pass

def effacerValeur():
    pass


# Bouton de vérification des doublons
monFont = font.Font(family='Couriel',size=18,weight="bold") # Police du Text 
bouton1 = Button(fenetre, text='Vérification', command=verif_doublon, bg="#12D292",fg="white", font=monFont)
bouton1.pack(fill="x")
# Bouton d'Impression 
bouton2 = Button(fenetre, text='Impression', command=impression, bg='#DFA80B', fg="white", font=monFont)
bouton2.pack(fill='x')
# Bouton d'éffacement des valeurs saisis 
bouton3 = Button(fenetre,text='Efface', command=effacerValeur)
bouton3.pack()

fenetre.mainloop()

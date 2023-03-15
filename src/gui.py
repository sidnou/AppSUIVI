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

fenetre = Tk() # fenêtre 

fenetre.title("Suivi Envoi Chronopost") # Titre de la fenêtre

fenetre.geometry("600x850") # Dimension de la fenêtre

cadre = Frame(fenetre,width=500,height=600,bg="white",relief="solid", bd=1)
cadre.place(x=50,y=20)
# cadre.pack()

entree1 = Entry(cadre)
entree1.pack()
entree2 = Entry(cadre)
entree2.pack()
entree3= Entry(cadre)
entree3.pack()
entree4= Entry(cadre)
entree4.pack()
entree5= Entry(cadre)
entree5.pack()
entree6= Entry(cadre)
entree6.pack()
entree7= Entry(cadre)
entree7.pack()
entree8= Entry(cadre)
entree8.pack()
entree9= Entry(cadre)
entree9.pack()
entree10= Entry(cadre)
entree10.pack()
entree11= Entry(cadre)
entree11.pack()
entree12= Entry(cadre)
entree12.pack()
entree13= Entry(cadre)
entree13.pack()
entree14= Entry(cadre)
entree14.pack()
entree15= Entry(cadre)
entree15.pack()
entree16= Entry(cadre)
entree16.pack()
entree17= Entry(cadre)
entree17.pack()
entree18= Entry(cadre)
entree18.pack()
entree19= Entry(cadre)
entree19.pack()
entree20= Entry(cadre)
entree20.pack()

bouton1 = Button(fenetre,text='Vérification')
bouton1.pack()
bouton2 = Button(fenetre,text='Impression')
bouton2.pack()


fenetre.mainloop()


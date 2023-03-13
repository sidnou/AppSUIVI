from tkinter import *


# Code
fenetre = Tk()
fenetre.geometry("800x800") # Dimension de la fenêtre
# Label 
label = Label(fenetre, text="Bonjour le Monde")
label.pack()
# Canvas 
canvas = Canvas(fenetre,width=400,height=400,background='white')
canvas.pack(side=TOP)
# Bouton
bouton = Button(fenetre,text="Impression")
bouton.pack()


fenetre.mainloop()
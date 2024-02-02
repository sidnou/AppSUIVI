import customtkinter

# def bouton_callback():
#     print("Bouton pressé")
#
#
# customtkinter.set_appearance_mode("dark")  # apparence de la fenêtre
# app = customtkinter.CTk()
# app.title("Gui V2")  # Titre de la fenêtre
# app.geometry("400x150")  # Dimension de la fenêtre
# mon_font = customtkinter.CTkFont(family="Times New Roman", size=15, weight="bold")  # Font text
# bouton = customtkinter.CTkButton(app, text="Bouton", command=bouton_callback, fg_color="#1E8449",
#                                  text_color="#F7F9F9", font=mon_font)  # Bouton
# bouton.grid(row=0, column=0, padx=20, pady=20) # Possition du bouton
# bouton.grid_columnconfigure(0, weight=1)
# app.mainloop()

VERSION = "1.0.2b"
COULEUR_ARRIERE_PLAN = ""
# Fenêtre Principal
customtkinter.set_appearance_mode("dark")  # apparence de la fenêtre noire
fenetre = customtkinter.CTk()
fenetre.title("Suivis Envoi Chronopost")  # Titre de la fenêtre
fenetre.geometry("1024x768+512+200")  # Dimension de la fenêtre
fenetre.minsize(1024, 768)
fenetre.maxsize(1920, 1080)
fenetre.iconbitmap("chronopost.ico")  # Icone de l'application
# Table
table = customtkinter.CTkTabview(master=fenetre)
table.pack(padx=10, pady=10)

table.add("tabl 1")
table.set("tabl 1")
# Entrée de valeur
entry = customtkinter.CTkEntry(master=fenetre, placeholder_text="Entrée une valeur")
entry.pack(padx=40, pady=40)
fenetre.mainloop()

import customtkinter


def bouton_callback():
    print("Bouton pressé")


customtkinter.set_appearance_mode("dark")  # apparence de la fenêtre
app = customtkinter.CTk()
app.title("Gui V2")  # Titre de la fenêtre
app.geometry("400x150")  # Dimension de la fenêtre
mon_font = customtkinter.CTkFont(family="Times New Roman", size=10, weight="bold")  # Font text
bouton = customtkinter.CTkButton(app, text="Bouton", command=bouton_callback, fg_color="#1E8449",
                                 text_color="#F7F9F9", font=mon_font)  # Bouton
bouton.grid(row=0, column=0, padx=20, pady=20) # Possition du bouton
bouton.grid_columnconfigure(0, weight=1)
app.mainloop()

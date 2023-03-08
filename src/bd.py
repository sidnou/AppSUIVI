import sqlite3

def creation_db():
    connex = sqlite3.connect('suivi-Chronopost.db')
    c = connex.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS suivi_chronopost (id INTEGER PRIMARY KEY AUTOINCREMENT, numero_suivi INTEGER UNIQUE, numero_dossier VARCHAR)""")

    connex.commit()
    connex.close

class DataBase():
    pass
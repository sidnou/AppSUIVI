import sqlite3

connex = sqlite3.connect('suivi-Chronopost.db')
c = connex.cursor()


c.execute(""" CREATE TABLE IF NOT EXISTS suivi_chronopost (id INTEGER PRIMARY KEY AUTOINCREMENT, numero_suivi INTEGER UNIQUE, numero_dossier VARCHAR)""")

connex.commit()
connex.close
import sqlite3


def creation_db():
    connex = sqlite3.connect('suivi-Chronopost.db')
    c = connex.cursor()

    c.execute(
        """ CREATE TABLE IF NOT EXISTS suivi_chronopost (id INTEGER PRIMARY KEY AUTOINCREMENT,
         numero_suivi INTEGER UNIQUE, 
         numero_dossier VARCHAR """)

    connex.commit()
    connex.close()


class DataBase:
    connex = sqlite3.connect('suivi-Chronopost.db')
    c = connex.cursor()

    def check_data(self, suivi):
        connex.execute("""SELECT COUNT(*) FROM suivi_chronopost WHERE numero_suivi = ?""", suivi)
        if connex.fetchone()[0] > 0:
            print("Le numèro de suivi existe déjà")

    # Ajout de donnée
    def add_data(self, numero_suivi, numero_dossier):
        connex.execute("INSERT INTO suivi_chronopost (numero_dossier,numero_suivi) VALUES (?,?)", numero_dossier,
                       numero_suivi)

    # suppression de donnée
    def supr_data(self):
        pass


if __name__ == '__main__':
    creation_db()

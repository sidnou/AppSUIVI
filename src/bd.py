import sqlite3


def creation_db():
    try:
        connex = sqlite3.connect('suivi-Chronopost.db')
        c = connex.cursor()

        c.execute(
            '''CREATE TABLE IF NOT EXISTS suivi_chronopost(id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_suivi INTEGER UNIQUE,
             numero_dossier TEXT )''')

        connex.commit()
        connex.close()
    except Exception:
        print("Existe déjà ")


class DataBase:
    def __init__(self):
        self.connex = sqlite3.connect('suivi-Chronopost.db')
        self.cur = self.connex.cursor()

    def check_data(self, suivi):
        db_check = [suivi]
        self.res = self.cur.execute("""SELECT COUNT(*) FROM suivi_chronopost WHERE numero_suivi = ?""", db_check)
        print(self.res.fetchone())
        self.t_res = self.res.fetchone()[0]
        if self.t_res > 0:
            print("Le numèro de suivi existe déjà")
        return 1

    def __getitem__(self, key):
        return self.__dict__[key]

    # Ajout de donnée
    def add_data(self, numero_suivi, numero_dossier):
        db_suivi = [numero_dossier, numero_suivi]

        self.cur.execute("INSERT INTO suivi_chronopost (numero_dossier,numero_suivi) VALUES (?,?)", db_suivi)
        self.connex.commit()
        # self.connex.close()

    # suppression de donnée
    def supr_data(self):
        pass


if __name__ == '__main__':
    creation_db()
    db = DataBase()
    db.check_data(822445246)
    db.add_data(822445246, "M67S-9999-99999")
    db.connex.close()

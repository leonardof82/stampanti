import sqlite3
conn = sqlite3.connect('stampante.db')
curs = conn.cursor()

curs.execute("CREATE table stampante (nome_modello,char(30),descrizione char(30),dipartimento_az char(30), catalogo,char(30))")


class Catalogo():
    def __init__(self, dipartimento_az, cursore):
        self.dipartimento_az = dipartimento_az
        self.modelli = list()
        self.cursore = cursore

    def aggiungi_stampante(self, stampante):
        self.modelli.append(stampante)
        row = (stampante.nome_modello, stampante.descrizione,stampante.dipartimento_az)
        self.cursore.execute("insert into stampante values (?, ?, ?)",row)
        print("stampante aggiunta")

    def cancella_stampante(self, stampante):
        if stampante in self.modelli:
            self.modelli.delete(stampante)
            self.cursore.execute("delete from stampante where riferimento = ?",(stampante.nome_modello,))
            print("stampante rimossa")
        else:
            print("stampante non è presente nel catalogo")

    def cerca_stampante(self, nome_modello):
        for stampante in self.modelli:
            if stampante.nome_modello == nome_modello:
                print("stampante trovata:")
                stampante.stampa_info()
        print("dal database:")
        self.cursore.execute("SELECT * FROM stampante WHERE nome_modello = ?",(stampante.nome_modello, ))
        for row in self.cursore.fetchall():
            print(row)

    def stampa_catalogo(self):
        for stampante in self.modelli:
            stampante.stampa_info()

        print("dal database:")
        self.cursore.execute("SELECT * FROM stampante")
        for row in self.cursore.fetchall():
            print(row)

generale = Catalogo("generale", curs)
stampante1 = Stampante ("canon", "3d", "Roma")
stampante2 = Stampante("epson","3d", "Vicenza")
generale.aggiungi_stampante(stampante1)
generale.aggiungi_stampante(stampante2)
generale.stampa_catalogo()
generale.cerca_stampante("Roma")
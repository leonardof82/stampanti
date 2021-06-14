class Stampante():
    def __init__(self, nome_modello, descrizione, dipartimento_az):
        self.nome_modello = nome_modello
        self.descrizione = descrizione
        self.dipartimento_az = dipartimento_az
        
    def modifica_modello(self, nome_modello):
        self.nome_modello = nome_modello
        print("il modello è stato  aggiornato")
    
    def cancellazione_modello(self, nome_modello):
        self.nome_modello = nome_modello
        print("il modello è stato  aggiornato")
    
    def stampa_info(self):
        print("la stampante modello  %s, %s dipartimento di   %s" % (self.nome_modello, self. descrizione,self.dipartimento_az))

class Catalogo():
    def __init__(self, dipartimento_az):
        self.dipartimento_az = dipartimento_az
        self.modelli = list() 

    def aggiungi_stampante(self, stampante):
        self.modelli.append(stampante)
        print("stampante aggiunta")

    def cancella_stampante(self, stampante):
        if stampante in self.modelli:
            self.modelli.delete(stampante)
            print("stampante rimossa")
        else:
            print("stampante non è presente nel catalogo")

    def cerca_stampante(self, nome_modello):
        for stampante in self.modelli:
            if stampante.nome_modello == nome_modello:
                print("stampante trovata:")
                immobile.stampa_info()
    def stampa_catalogo(self):
        for stampante in self.modelli:
            stampante.stampa_info()

generale = Catalogo("generale")
stampante1 = Stampante ("canon", "3d", "Roma")
stampante2 = Stampante("epson","3d", "Vicenza")
generale.aggiungi_stampante(stampante1)
generale.aggiungi_stampante(stampante2)
generale.stampa_catalogo()
generale.cerca_stampante("Roma")


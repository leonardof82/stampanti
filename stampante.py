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
        print("la stampante modello  %s, %s di  %s" % (self.nome_modello, self. descrizione,self.dipartimento_az))
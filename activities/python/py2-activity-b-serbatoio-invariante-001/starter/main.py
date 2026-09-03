class Serbatoio:
    def __init__(self, capacita):
        self.capacita = capacita
        self.livello = 0

    def aggiungi(self, quantita):
        self.livello += quantita
        return True

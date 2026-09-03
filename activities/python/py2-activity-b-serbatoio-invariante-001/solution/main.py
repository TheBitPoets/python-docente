class Serbatoio:
    def __init__(self, capacita):
        self.capacita = capacita
        self.livello = 0

    def aggiungi(self, quantita):
        if quantita < 0:
            return False
        if self.livello + quantita > self.capacita:
            return False
        self.livello += quantita
        return True

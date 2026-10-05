class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        # self.sijainti = None
        self.inventaario = []

    def lisaa(self,esine):
        self.inventaario.append(esine)
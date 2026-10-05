class Huone:
    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus

        self.reitit = {}
        self.esineet = []

    def lisaa_reitti(self, numero, huone):
        self.reitit[numero] = huone

    def lisaa_esine(self, esine):
        self.esineet.append(esine)
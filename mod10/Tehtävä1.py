class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros
    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        print("Hissi on kerroksessa", self.kerros)
    def kerros_alas(self):
        self.kerros = self.kerros -1
        print("Hissi on kerroksessa", self.kerros)
    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()
        while self.kerros > kohde:
            self.kerros_alas()

h=Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
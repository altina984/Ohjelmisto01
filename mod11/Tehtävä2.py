class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.nopeus=0
        self.kuljettu_matka=0
    
    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        
        if self.nopeus < 0:
            self.nopeus=0
    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti=akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bensatankin_koko=bensatankin_koko


sahkoauto=Sahkoauto("ABC-15", 180, 52-5)
polttomoottoriauto=Polttomoottoriauto("ABC-123", 165, 32.3)

sahkoauto.kiihdyta(100)
polttomoottoriauto.kiihdyta(80)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)
print("Sähköauton matkamittarilukema:", sahkoauto.kuljettu_matka, "km")
print("Polttomoottoriauton matkamittarilukema:", polttomoottoriauto.kuljettu_matka, "km")

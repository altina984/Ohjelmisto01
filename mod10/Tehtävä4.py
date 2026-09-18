import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
     self.rekisteritunnus=rekisteritunnus
     self.huippunopeus=huippunopeus
     self.nykynopeus=0
     self.kuljettumatka=0
     
    def kiihdytä(self, muutos):
         self.nykynopeus = self.nykynopeus + muutos
        
         if self.nykynopeus > self.huippunopeus:
            self.nykynopeus=self.huippunopeus
         if self.nykynopeus < 0:
            self.nykynopeus = 0
    
    def kulje(self, tunnit):
           self.kuljettumatka = self.kuljettumatka + self.nykynopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)
    def tulosta_tilanne(self):
        print("Rekisteri\tHuippunopeus\tNykynopeus\tKuljettu matka")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus}\t\t{auto.huippunopeus}\t\t{auto.nykynopeus}\t\t{auto.kuljettumatka}")
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettumatka >= self.pituus:
                return True
            return False
autot = []

for i in range(10):
   rekisteritunnus = "ABC-" + str(i + 1)
   huippunopeus = random.randint(100, 200)
   auto = Auto(rekisteritunnus, huippunopeus)
   autot.append(auto)
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
  
tunnit = 0
while not kilpailu.kilpailu_ohi():
       kilpailu.tunti_kuluu()
       tunnit = tunnit + 1
       if tunnit % 10 == 0:
           kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()
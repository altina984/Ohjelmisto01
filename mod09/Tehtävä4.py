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
     
autot = []

for i in range(10):
   rekisteritunnus = "ABC-" + str(i + 1)
   huippunopeus = random.randint(100, 200)
   auto = Auto(rekisteritunnus, huippunopeus)
   autot.append(auto)
while True:
   for auto in autot:
      muutos = random.randint(-10, 15)
      auto.kiihdytä(muutos)
      auto.kulje(1)

   if any(auto.kuljettumatka >= 10000 for auto in autot):
     break
print("Rekisteri\tHuippunopeus\tNykynopeus\tKuljettu matka")
for auto in autot:
      print(f"{auto.rekisteritunnus}\t\t{auto.huippunopeus}\t\t{auto.nykynopeus}\t\t{auto.kuljettumatka}")
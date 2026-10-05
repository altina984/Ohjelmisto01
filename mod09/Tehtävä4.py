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
     
import random
autot = []
for i in range(10):
   rekisteri = f"ABC-{i + 1}"
   huippunopeus = random.randint(100, 200)
   auto = Auto(rekisteri, huippunopeus)
   autot.append(auto)

kilpailu_jatkuu = True

while kilpailu_jatkuu:
   for auto in autot:
      auto.kiihdyta(random.randint(-10, 15))
      auto.kulje(1)

      if auto.kuljettu_matka >= 10000:
         kilpailu_jatkuu = False

for auto in autot:
   print(auto.rekisteritunnus,
         auto.huippunopeus,
         auto.nopeus,
         auto.kuljettu_matka)
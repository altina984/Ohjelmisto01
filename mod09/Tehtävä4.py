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
     

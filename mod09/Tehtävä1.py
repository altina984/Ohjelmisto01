class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
     self.rekisteritunnus=rekisteritunnus
     self.huippunopeus=huippunopeus
     self.nykynopeus=0
     self.kuljettumatka=0
auto = Auto("ABC-123",142)
print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nykynopeus)
print(auto.kuljettumatka)
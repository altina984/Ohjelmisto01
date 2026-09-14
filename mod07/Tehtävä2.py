import random 
def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input('Anna nopan tahkojen määrä: '))
luku = 0

while luku != maksimi:
    luku = heitä_noppaa(maksimi)
    print(luku)
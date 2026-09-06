import math
luku= 1

while luku <= 1000:
   if luku % 3 == 0:
      print(luku)
   luku = luku + 1


tuumat = float(input("Anna tuumamäärä: "))

while tuumat >= 0: 
   sentit = tuumat * 2.54
   print("Senttimetreinä:", sentit)
   tuumat = float(input("Anna tuumamäärä: "))


pienin = None
suurin = None 
syote = input("Anna luku (Enter lopettaa): ")
while syote != "":
   luku = float(syote)

   if pienin is None or luku < pienin:
      pienin = luku

   if suurin is None or luku > suurin:
      suurin = luku 

   syote = input("Anna luku (Enter lopettaa): ")

   print("Pienin luku:", pienin)
   print("Suurin luku:", suurin)
   


import random 
oikea_luku = random.randint(1,10)

arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != oikea_luku:
    if arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa uudelleen: "))
    print("Oikein")


yritykset= 0
while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    yritykset = yritykset + 1 

    if yritykset == 5:
        print("Pääsy evätty")


import random
pisteet = int(input("Anna arvottavien pisteiden määrä: "))
i = 0
sisalla = 0

while i < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        sisalla = sisalla + 1

    i = i + 1
pii = 4 * sisalla / pisteet 
print("Piin likiarvo on:", pii)
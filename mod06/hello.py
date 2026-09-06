import random 
maara = int(input("Kuinka monta arpakuutiota? "))
summa = 0
for i in range(maara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku
    print("Silmälukujen summa on:", summa)


luvut = []
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break
    luvut.append(float(syote))
    luvut.sort(reverse=True)
    for luku in luvut[:5]:
        print(luku)


luku = int(input("Anna kokonaisluku: "))
alkuluku = True
if luku < 2:
    alkuluku = False
else:
    for i in range(2, luku):
      if luku % i == 0:
         alkuluku = False
         break
      if alkuluku:
         print("Luku on alkuluku.")
    else: 
       print("Luku ei ole alkuluku.")


kaupungit = []
for i in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)
    for kaupunki in kaupungit:
        print(kaupunki)
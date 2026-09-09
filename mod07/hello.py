import random
def heitä_noppaa():
    return random.randint(1, 6)

luku = 0

while luku != 6:
    luku=heitä_noppaa()
    print(luku)



def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input('Anna nopan tahkojen määrä: '))
luku = 0

while luku != maksimi:
    luku = heitä_noppaa(maksimi)
    print(luku)




def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

gallonat = float(input('Anna gallonmäärä: '))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print('Litroins:', litrat)

    gallonat = float(input('Anna gallonmäärä: '))




def laske_summa(lista):
    summa = 0

    for luku in lista:
        summa += luku

    return summa

luvut = [1,2,3,4,5]

tulos = laske_summa(luvut)

print('Summa on',tulos)





def poista_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista

luvut = [1,2,3,4,5,6,7,8]

karsittu_lista = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu_lista)




import math
def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    pinta_ala_m2 = pinta_ala / 10000
    return hinta / pinta_ala_m2

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€)"))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle. ")


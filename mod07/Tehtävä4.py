def laske_summa(lista):
    summa = 0

    for luku in lista:
        summa += luku

    return summa

luvut = [1,2,3,4,5]

tulos = laske_summa(luvut)

print('Summa on',tulos)
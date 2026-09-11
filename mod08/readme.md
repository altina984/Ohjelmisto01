## Tunti tehtävät


#Monikko
#Joukko
#Sanakirja

#tup = (3, 5, 8, 10, (24, 25),'Moi!', 200)

#Pituus on 7 
#Mikä on kympin indeksi
#Onko tupissa numero 10? Entä numero 210
#Printaa kaikki alkiot, yksi kerralla. 
#Tee toinen tup, jonka alkiota ovat samat kuin tup, mutta väärässä järjestyksessä.

#t= (3, 5, 8, 10, (24, 25),'Moi!', 200)
#print(len(t))


#1. print(len(tup))
#thistuple
#x=thistuple.index(8)
#print(x)

#print(tup.index(10))

#print(10 in tup)

#print(210 in tup)

#for alkio in tup:
    #print(alkio)

#print(tup[::-1])

#print(tup[::-1])



numbers = {"Viivi": "05049679357",
           "Ahmed": "57979578975",
           "Pekka": "59769739759",
           "George": "7597937699"}

#nimi= input("Anna nimi: ")
#if nimi in numbers: 
      #print(f" Henkilön {nimi} puhelinnumero on {numbers[nimi]}")

#for key in numbers:
      #print(f'{key}:n puhelinnumero on {numbers[key]}')

#print('James' in numbers)


#nimi= input("Anna kaverin nimi: ")
#if nimi in numbers:
    #print(f'{nimi} löytyy, sen number on {numbers[nimi]}')
#else:
    #print(f'{nimi} ei löytynyt luettelosta.')

#numbers['Viivi'] = '579679769769'
#print(numbers)

#numbers['James'] = '579679769769'
#print(numbers)
import math
a=5
b=0

c=3
d=4

#a/b

#x=False
#y=True
#z=True
#z1=True
#print(x and y and z and z1)


#if (c<d and a/b):
    #print('Moi!')

#def f():
    #print('Moi!')
#f()

#li = [2, 3, 2, 6, 7, 3, 3]
#s1 = set(li)
#print(s1)
#l2 = list(s1)
#print(l2)
#print(type(students[0]))

hedelmat = ('Omena', 'Appelsiini', 'Vesimeloni')
print('omena' in hedelmat)

students =[
{"name": "Ella", "Age": 14, "grade":"9"},
{"name": "Leo", "age": 15, "grade": "8"},
{"name": "Aino", "age": 14, "grade": "10"},
]

for item in students:
    print(f'{item}:n arvosana on {numbers}')


print(students[2]['name'])
print(students[2]['grade'])
print(f'{students[2]['name']}n arvo sana on {students[2]['grade']}')
for student in students:
    print(f'{students['name']}n arvo sana on {student['grade']}')
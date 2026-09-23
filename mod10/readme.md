r1 instanssi

properties adjektiivi
methods verbs
self voi olla mikä hyvänsä

class Rectangle: 
    #def __init__(self, pituus, leveys):
     #self.pituus = pituus
     #self.leveys = leveys 
    

    #def piiri(self):
      # piiri=self.pituus * 2 + self.leveys*2
       #print(f'Suorakulmaisen piiri on {self.pituus*2 + self.leveys*2}')
       #return piiri
    #print(R1.piiri())


    #R1 = Rectangle(3, 4)
    #R2 = Rectangle(5, 10)


#class Asukas:
    #def __init__(self, nimi):
        #self.nimi=nimi
#a1=Asukas('Helena')
#a2=Asukas('Elsa')
#a3=Asukas('Alice')
#print(a3.nimi)
#k1.asu.nimi
#class Kaupunki:
# def __init__(self, nimi, asukas):
        #self.nimi=nimi
        #self.asukas=asukas
    #def kuka(self):
        #print(f'Asukas {self.asukas.nimi} asuu kaupungissa {self.nimi}')
        #pass

#k1=Kaupunki('Helsinki', a1)
#k2=Kaupunki('Tampere', a2)

#k1.kuka()







#class Kirjailija:
    #def __init__(self, nimi):
      #self.nimi=nimi

#class Kirja: 
    #def __init__(self, nimi, kirjailija):
      # self.nimi= nimi
       #self.kirjailija = kirjailija
                 
#k1 = Kirjailija('k1')
#k2 = Kirjailija('k2')
#ki1= Kirja('ki1', k1)
#ki2= Kirja('ki2', k2)

#print(ki1.kirjailija.nimi)

#print(f'Kirjan nimi on {k1.nimi} ja sen kirjailija on {ki1.kirjailija.nimi}')
#def walk(self):
     #print
     #R1.walk()


#luo 3 kirjaa
#class Book:
    #def __init__(self, kirjailija, nimi, sivut = 100):
        #self.kirjailija=kirjailija
        #self.nimi=nimi
        #self.sivut=sivut

#b1= Book('Matti Menninkäinen', 'Avaruus', '205')
#b2= Book('Elias Elollinen', 'Maailma', '102')
#b3= Book('Alina Allinen', 'Kaunis paikka', '150')
#b4= Book('10', '04')

#def f(a= 100,b= 4):
 # print(a)
 # print(b)
#f(100)


#print(b4.sivut)

#class Ope:
    #def __init__(self, nimi):
        #self.nimi=nimi
    #def mun_stu(self, opis):
     #print(f'Mä oon {self.nimi} ja mun opiskelijan nimi on {opis.nimi}')
   
#o1=Ope('Helena')


#class Opiskelija:
    #def __init__(self, nimi):
       # self.nimi=nimi 

#op1=Opiskelija('Elsa')
#op2=Opiskelija('Tatu')
#o1.mun_stu(op1)
#o2=('James')

class Person: 
    #def __init__(self, nimi, sukunimi, ika):
        #self.nimi= nimi
        #self.ika =ika

    #print(f'{self.nimi} kävelee')

    #p1=('Matti','joku','35')
    #p2=('Heikki','joku', '17')

    #print(f"{p1.nimi} kävelee")

    #def is_adult(self):
        #if self.ika < 18:
           # print(f'{self.nimi} ei ole aikuinen')
        #else:
            #print(f'{self.nimi} on aikuinen')

    #p1.is_adult()
    
    
    #Lisää methodi is adult
    #jos 18 tai yli se kirjoittaa on aikuinen
    #muuten ei ole 


#class Tili:
   # def __init__(self, saldo):
        #self.saldo=saldo
    #def talletus(self,maara):
       # self.saldo = self.saldo + maara
       # pass
    #def nosto(self,maara):
        #pass
        #self.saldo = self.saldo - maara

#t1= Tili(200)
#t1.talletus(50)
#t1.nosto(50)

#t2=Tili(300)
#t1.talletus(20)
#t1.nosto(30)
#print(t1.saldo)
#print(t2.saldo)


class Kirja:
    def __init__(self, nimi):
        self.nimi=nimi

class Kirjasto:
    def __init__(self, nimi):
        self.nimi=nimi
        self.kirjat = []

    def lisaa(self.krj):
        self.kirjat.append(krj)
k1 = Kirja('Maila')
k2 = Kirja('Tuntematon Sotilas')
k3 = Kirja('Aakkoset')
k4 = Kirja('Raamattu')

kir1 = Kirjasto('Oodi')
kir1.lisaa(k1)
kir1.lisaa(k2)
kir1.lisaa(k3)

for item in kir1.kirjat:
    print(item.nimi)
    
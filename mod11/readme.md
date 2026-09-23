#class Viesti:
   #lahetetty = 0
   #def __init__(self, sisalto):
      #self.sisältö = sisalto
      #Viesti.lahetetty = Viesti.lahetetty + 1
      #Viesti.lahetetty += 1 tämä käy paremmin
#v2=Viesti('Minne meet?')
#v3=Viesti('Ootko koulussa?')

#print(v2.sisältö)
#print(Viesti.lahetetty)




#class Animal:
    #def __init__(self, paino):
        #self.paino = paino
        #def kavelee(self):
            #print('Minä olen eläin.')

#class Dog:
    #def __init__(self, paino, hanta):
      #  super(). __init__(paino)
       # self.hanta = hanta
    #def kavelee(self):
       # super().kavelee()  
        #print('Itseasiassa olen koira, joten kävelen nätisti')

#d1= Dog(20, 'pitkä')

#d1.kavelee()


class Muoto:
    def __init__(self, vari):
        self.vari = vari
    def mittaa (self):
        print('Nyt lasken piirin')


class Suorakulmio(Muoto):
    def __init__(self, vari, pituus, leveys):
        super().__init__(vari)
        self.pituus = pituus
        self.leveys = leveys
    def mittaa(self):
        super().mittaa()
        piiri=2*(self.leveys + self.pituus)
        print(f'Piiri on {piiri}')

s1 = Suorakulmio('Punainen', 3, 4)
s1.mittaa()


class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus

class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino

class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)

        self.vaihteet = vaihteet

pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)
#s1={2,3,5, 10, 15} 
#d1 = {'a' : 4, 'b' : 6, 'c' : 8}

#print(12 in d1)
#for item in s1:
  #  print(item)
#print(s1[2])
#for item in d1:
    #print(item)


#import snacks
#print(snacks.SNACKS)


#print(snacks.get_random_snacks():)


class Biisi:
    def __init__(self, laulaja, nimi):
        self.laulaja=laulaja
        self.nimi=nimi

b1=Biisi('l1', 'n1')
b2=Biisi('l2', 'n2')
b3=Biisi('13', 'n3')
b4=Biisi('l4', 'n4')
b5=Biisi('l5', 'n5')
b6=Biisi('l6', 'n6')
b7=Biisi('l7', 'n7')

class Playlist:
    def __init__(self):
        self.munlista=[]

    def lisaa(self, uusi):
        self.munlista.append(uusi)

l1=[b1, b2, b3]

for item in l1:
    print(item.laulaja)
pl=Playlist()
pl.lisaa(b2)
print(pl.munlista)



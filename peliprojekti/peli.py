from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

with open ("peliprojekti/intro.txt", "r", encoding="utf-8") as file:
    log_in= file.read()
    print(log_in)

avain = Esine("Avain","Sininen avain jossa on tähti.", '15g')
kirja = Esine("Kirja", "Kirjassa löytyy tietoa ja vihjeitä.", '500g' ) 
kirje = Esine("Kirje", "joka on hukkunut roskaposteihin ja siinä on tärkeää tietoa.", '40g')

def tee_kartta():
    koodilaakso = Huone("Koodilaakso","Olet keskellä Koodilaakso.")
    pixelimaa = Huone("Pixelimaa","Olet oudossa maailmassa, joka on täynnä värejä.")
    muistivuoto = Huone("Muistivuoto","Olet sekavassa paikassa, jossa on paljon muistia.")
    roskapostikuilu = Huone("Roskapostikuilu","Olet paikassa, jossa on maailman roskapostit.")
    
    koodilaakso.lisaa_reitti("1",pixelimaa)
    koodilaakso.lisaa_reitti("2",muistivuoto)
    koodilaakso.lisaa_reitti("3",roskapostikuilu)
    
    pixelimaa.lisaa_reitti("1", koodilaakso)
    muistivuoto.lisaa_reitti("1", koodilaakso)
    roskapostikuilu.lisaa_reitti("1", koodilaakso)
    return koodilaakso, pixelimaa, muistivuoto, roskapostikuilu

print("1. Uusi peli")
print("2. Jatka tallennettua peliä")
valinta = input("Valitse: ")

if valinta == "2":
   nimi, ika, tallennettu_huone, tavarat = lataa_peli()
   print("Tallennettu peli ladattu!")


nimi = input("\nMikä on pelaajamme nimi?: ")
ika = int(input("Entä mikä on ikäsi?: "))
if ika < 12:
    print("Olet liian nuori pelaamaan peliä.")
else:
    print(f'Hauska tavata {nimi}, tervetuloa peliin!')

    pelaaja = Pelaaja(nimi, ika)
    koodilaakso,pixelimaa,muistivuoto, roskapostikuilu = tee_kartta()
    tallahetkella_huone = koodilaakso
    tavarat = ["Kartta"] 
    avain_loydetty = False
    kirja_loydetty = False
    kirje_loydetty = False
    
        
    komento = ""
    while komento != "8":
        print("\nTOIMINNOT")
        print("1. Aloita peli")
        print("2. Lue ohjeet")
        print("3. Tutki ympäristöä")
        print("4. Lisää esine")
        print("5. Näytä inventaario")
        print("6. Liiku")
        print("7. Tallenna peli")
        print("8. Lopeta peli")
        
        def aloita_peli():
            print("Peli alkaa!")
            print("Tehtäväsi on löytää takaisin kotiin.")

        def lue_ohjeet():
         with open ("peliprojekti/ohjeet.txt", "r", encoding="utf-8") as file:
             print(file.read())

        def tutki_esine(esine):
           print("Esine:", esine.nimi)
           print("Kuvaus:", esine.kuvaus)
           print("Paino:", esine.paino)
    
        def tutki_huone(huone):
           print("\n"+ huone.nimi)
           print(huone.kuvaus)
           for esine in huone.esineet:
              print("Huoneessa on:", esine.nimi)

        def tallenna_peli(pelaaja, huone, tavarat):
           file = open ("tallenna.txt", "w")
              
           file.write(pelaaja.nimi + "\n")
           file.write(f'{pelaaja.ika}\n')
           file.write(huone.nimi + "\n")
        
           for tavara in tavarat:
               file.write(tavara + "\n")

        def lataa_peli():
            with open("tallenna.txt", "r") as file:
             tiedot = file.read()

            for rivi in file:
             tiedot.append(rivi)
             nimi = tiedot
             ika = int(tiedot[1])
             huone = tiedot[2]
             tavarat = tiedot[3:]
        
        import json
        def lataa_peli():
            with open("tallenna.txt", "r") as file:
             tiedot = file.read()
             return tiedot["nimi"], tiedot["ika"], tiedot["huone"], tiedot["tavarat"]
        print("Peli on tallennettu!")


        komento=input("Minkä toiminnon valitset?: ")
        if komento == "1":
            aloita_peli()
        
        elif komento == "2":
            lue_ohjeet()
        
        elif komento == "3":
            print(tallahetkella_huone.nimi)
            print(tallahetkella_huone.kuvaus)
            
            for item in tallahetkella_huone.esineet:
              print("Huoneessa on " + item.nimi)
        
        elif komento == "4":
            tavara = input("Minkälaisen esineen haluaisit lisätä tämän kerran?")
            tavarat.append(tavara)
        
        elif komento == "5":
            print("Vau! Olet löytänyt monta esinettä, inventaariosi sisältää: ")
            for t in tavarat:
                print("-" + t)
        
        elif komento == "6":
            print("Minne haluaisit mennä?")
            if tallahetkella_huone == koodilaakso:
             print("1. Pixelimaa")
             print("2. Muistivuoto")
             print("3. Roskapostikuilu")
             print("4. Koodilaakso")
            reitti = input("Valitse reitti: ")

            if reitti == "1":
                tallahetkella_huone = pixelimaa
                print("Olet menossa Pixelimaahan.")
                if avain_loydetty == False:
                 tavarat.append("Avain")
                 avain_loydetty = True
                 print("Löysit Avaimen! Se lisättiin inventaarioon.")
                 print(avain.kuvaus)
                 print("Paino:", avain.paino)

            elif reitti == "2":
                tallahetkella_huone = muistivuoto
                print("Olet menossa Muistivuotoon.")
                if kirja_loydetty == False:
                 tavarat.append("Kirja")
                 kirja_loydetty = True
                 print("Löysit Kirjan! Se lisättiin inventaarioon.")
                 print(kirja.kuvaus)
                 print("Paino:", kirja.paino)
            
            elif reitti == "3":
                tallahetkella_huone = roskapostikuilu
                print("Olet menossa Roskapostikuiluun.")
                if kirje_loydetty == False:
                 tavarat.append("Kirje")
                 kirje_loydetty = True
                 print("Löysit Kirjeen! Se lisättiin inventaarioon.")
                 print(kirje.kuvaus)
                 print("Paino:", kirje.paino)
            
            elif reitti == "4":
                tallahetkella_huone = koodilaakso
                print("Menit takaisin koodilaaksoon.")

                if avain_loydetty == True and kirja_loydetty == True and kirje_loydetty == True:
                 print("Olet löytänyt kaikki tarvittavat esineet jotka olivat: Avain, Kirja ja Kirje!")
                 print("WOW, löysit tien takaisin kotiin!")
                 print("VOITIN PELIN!")

        elif komento == "7":
            tallenna_peli(pelaaja, tallahetkella_huone, tavarat)
        
        elif komento == "8":
         print("Peli lopetetaan.")
        else:
         print("Virheellinen komento")

            
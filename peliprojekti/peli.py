from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

import colorama
from colorama import Fore, Style

with open ("peliprojekti/intro.txt", "r", encoding="utf-8") as file:
    log_in= file.read()
    print(log_in)
   

avain = Esine("Avain","Sininen avain jossa on tähti.", '15g' + Fore.GREEN)
kirja = Esine("Kirja", "Kirjassa löytyy tietoa ja vihjeitä.", '500g' + Fore.GREEN) 
kirje = Esine("Kirje", "joka on hukkunut roskaposteihin ja siinä on tärkeää tietoa.", '40g' + Fore.GREEN)

def tee_kartta():
    koodilaakso = Huone("Koodilaakso","Olet keskellä Koodilaakso."+ Fore.GREEN)
    pixelimaa = Huone("Pixelimaa","Olet oudossa maailmassa, joka on täynnä värejä." + Fore.GREEN)
    muistivuoto = Huone("Muistivuoto","Olet sekavassa paikassa, jossa on paljon muistia." + Fore.GREEN)
    roskapostikuilu = Huone("Roskapostikuilu","Olet paikassa, jossa on maailman roskapostit." + Fore.GREEN)
    
    koodilaakso.lisaa_reitti("1",pixelimaa)
    koodilaakso.lisaa_reitti("2",muistivuoto)
    koodilaakso.lisaa_reitti("3",roskapostikuilu)
    
    pixelimaa.lisaa_reitti("1", koodilaakso)
    muistivuoto.lisaa_reitti("1", koodilaakso)
    roskapostikuilu.lisaa_reitti("1", koodilaakso)
    return koodilaakso, pixelimaa, muistivuoto, roskapostikuilu

def lataa_peli():
   with open("tallenna.txt", "r") as file:
     tiedot = file.read().split("\n")

     nimi= tiedot[0]
     ika= int(tiedot[1])
     huone= tiedot[2]
     tavarat = tiedot[3:]

     return nimi, ika, huone, tavarat

print(Fore.CYAN + "1. Uusi peli")
print("2. Jatka tallennettua peliä")

valinta = input("Valitse: ")

if valinta =="1":
   print('uusi peli')
elif valinta == "2":
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
        print("\nTOIMINNOT" + Fore.MAGENTA)
        print("1. Aloita peli")
        print("2. Lue ohjeet")
        print("3. Tutki ympäristöä")
        print("4. Lisää esine")
        print("5. Näytä inventaario" + Fore.RED)
        print("6. Liiku")
        print("7. Tallenna peli")
        print("8. Lopeta peli")
        
        def aloita_peli():
            print("Peli alkaa!" + Fore.GREEN)
            print("Tehtäväsi on löytää takaisin kotiin." + Fore.GREEN)

        def lue_ohjeet():
         with open ("peliprojekti/ohjeet.txt", "r", encoding="utf-8") as file:
             print(Fore.BLUE + file.read())

        def tutki_esine(esine):
           print("Esine:", esine.nimi + Fore.YELLOW)
           print("Kuvaus:", esine.kuvaus + Fore.YELLOW)
           print("Paino:", esine.paino + Fore.YELLOW)
    
        def tutki_huone(huone):
           print("\n"+ huone.nimi + Fore.YELLOW)
           print(huone.kuvaus + Fore.YELLOW)
           for esine in huone.esineet:
              print("Huoneessa on:", esine.nimi + Fore.YELLOW)

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
            tavara = input("Minkälaisen esineen haluaisit lisätä tämän kerran?" + Fore.GREEN)
            tavarat.append(tavara)
        
        elif komento == "5":
            print("Vau! Olet löytänyt monta esinettä, inventaariosi sisältää: " + Fore.GREEN)
            for t in tavarat:
                print("-" + t)
        
        elif komento == "6":
            print("Minne haluaisit mennä?" + Fore.GREEN)
            if tallahetkella_huone == koodilaakso:
             print("1. Pixelimaa" + Fore.GREEN)
             print("2. Muistivuoto" + Fore.GREEN)
             print("3. Roskapostikuilu" + Fore.GREEN)
             print("4. Koodilaakso" + Fore.GREEN)
            reitti = input("Valitse reitti: " + Fore.GREEN)

            if reitti == "1":
                tallahetkella_huone = pixelimaa
                print("Olet menossa Pixelimaahan." + Fore.GREEN)
                if avain_loydetty == False:
                 tavarat.append("Avain")
                 avain_loydetty = True
                 print("Löysit Avaimen! Se lisättiin inventaarioon." + Fore.GREEN)
                 print(avain.kuvaus)
                 print("Paino:", avain.paino + Fore.GREEN)

            elif reitti == "2":
                tallahetkella_huone = muistivuoto
                print("Olet menossa Muistivuotoon." + Fore.GREEN)
                if kirja_loydetty == False:
                 tavarat.append("Kirja")
                 kirja_loydetty = True
                 print("Löysit Kirjan! Se lisättiin inventaarioon." + Fore.GREEN)
                 print(kirja.kuvaus)
                 print("Paino:", kirja.paino + Fore.GREEN)
            
            elif reitti == "3":
                tallahetkella_huone = roskapostikuilu
                print("Olet menossa Roskapostikuiluun." + Fore.GREEN)
                if kirje_loydetty == False:
                 tavarat.append("Kirje")
                 kirje_loydetty = True
                 print("Löysit Kirjeen! Se lisättiin inventaarioon." + Fore.GREEN)
                 print(kirje.kuvaus)
                 print("Paino:", kirje.paino + Fore.GREEN)
            
            elif reitti == "4":
                tallahetkella_huone = koodilaakso
                print("Menit takaisin koodilaaksoon." + Fore.GREEN)

                if avain_loydetty == True and kirja_loydetty == True and kirje_loydetty == True:
                 print(Fore.WHITE + "Olet löytänyt kaikki tarvittavat esineet jotka olivat: Avain, Kirja ja Kirje!")
                 print("WOW, löysit tien takaisin kotiin!" + Fore.WHITE)
                 print("VOITIN PELIN!" + Fore.WHITE)

        elif komento == "7":
            tallenna_peli(pelaaja, tallahetkella_huone, tavarat)
        
        elif komento == "8":
         print("Peli lopetetaan.")
        else:
         print("Virheellinen komento")

            
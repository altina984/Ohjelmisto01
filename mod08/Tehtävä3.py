lentokentat = {}

while True:
    toiminto = input("Valitse toiminto: uusi, haku tai lopeta:")

    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentokentän nimi: ")
        lentokentat[icao] = nimi
    
    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentokentat:
         print(lentokentat[icao])
    
        else:
         print("lentokenttää ei löytynyt.")
    
    elif toiminto == "lopeta":
    
      print("Ohjelma lopetetaan.")
      break

    else:
     print("Virheellinen valinta")
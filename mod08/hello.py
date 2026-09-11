Vuodenajat = (
    "Talvi",   # Joulukuu 
    "Talvi",   # Tammikuu
    "Talvi",   # Helmikuu
    "Kevät",   # Maaliskuu
    "kevät",   # Huhtikuu
    "Kevät",   # Toukokuu
    "Kesä",    # Kesäkuu
    "Kesä",    # Heinäkuu
    "Kesä",    # Elokuu
    "Syksy",   # Syyskuu
    "Syksy",   # Lokakuu
    "Syksy",   # Marraskuu
)

kuukausi = int(input("Anna kuukauden numero (1-12):"))

print(Vuodenajat[kuukausi % 12])




nimet = set()
while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    print("Syötetyt nimet:")
    for nimi in nimet:
        print(nimi)




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
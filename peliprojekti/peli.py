nimi=input("Mikä on pelaajamme nimi?:")
print(nimi)
ika=int(input("Entä mikä on ikäsi?:"))
print(ika)


if ika < 12:
    print("Olet alaikäinen. Peli loppuu.")
else:
    print("Tervetuloa", nimi)

    komento = ""

    while komento != "lopeta":
        print("\nPÄÄVALIKKO")
        print("tervehdi")
        print("vitsi")
        print("nimi")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "tervehdi":
            print("Hei", nimi)
        elif komento == "vitsi":
            print("Miksi tietokone oli väsynyt? Sillä oli liikaa bittejä.")
        elif komento == "nimi":
            print("Pelaajan nimi on", nimi)
        elif komento == "lopeta":
            print("Peli lopetetaan.")
        else:
            print("Tuntematon komento.")
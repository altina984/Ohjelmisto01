nimi = input("Mikä on pelaajamme nimi?: ")
ika = int(input("Entä mikä on ikäsi: "))

inventaario = []

def tervehdi():
    print("Hei", nimi)

def vitsi():
    print("Miksi tietokone oli väsynyt? Sillä oli liikaa bittejä.")

def näytä_nimi():
    print("Pelaajan nimi on", nimi)

def lisää_esine():
    esine = input("Minkä esineen haluat lisätä: ")
    inventaario.append(esine)
    print(esine, "lisättiin inventaarioon.")

def näytä_inventaario():
    print("Inventaario:")
    for esine in inventaario:
        print(esine)


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
        print("lisää")
        print("inventaario")
        print("lopeta")

        komento = input("Valitse: ")

        if komento == "tervehdi":
            print("Tervetuloa pixeli maailmaan!")
        elif komento == "vitsi":
            print("Miksi pelaaja otti tikkaat mukaan peliin? Koska hän halusi päästä seuraavalle tasolle!")
        elif komento == "nimi":
            näytä_nimi()
        elif komento == "lisää":
            print("Sinua odottaa iso yllätys voittaessa pelin!")
        elif komento == "inventaario":
            print("Sinulla on käytettävissä miekka, avain ja taikajuoma. Minkä valitset?")
        elif komento == "lopeta":
            print("Peli lopetetaan.")
        else:
            print("Tuntematon komento.")

            

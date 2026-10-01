with open ("intro.txt", "r") as file:
    log_in= file.read()
    print(log_in)

with open ("ohjeet.txt", "r") as file:
    ohjeet= file.read()
    print(ohjeet)

def aloita_peli():
    print("Peli alkaa!")
    return


nimi = input("\nMikä on pelaajamme nimi?: ")
ika = int(input("Entä mikä on ikäsi?: "))
if ika < 12:
    print("Olet liian nuori pelaamaan peliä.")
else:
    print(f'Hauska tavata {nimi}, tervetuloa peliin!')
    
    komento = ""
    while komento != "6":
        print("\nTOIMINNOT")
        print("1. Aloita peli")
        print("2. Lue ohjeet")
        print("3. Tutki ympäristöä")
        print("4. Lisää esine")
        print("5. Näytä inventaario")
        print("6. Lopeta peli")

        komento=input("Minkä toiminnon valitset?: ")
        if komento == "1":
            aloita_peli()
        elif komento == "2":
            print(ohjeet)
        elif komento == "3":
            print("Tutkit ympäristöä.")
        elif komento == "4":
            print(lisaa_tavarat)
        elif komento == "5":
             print(inventaario)
        elif komento == "6":
            print("Peli lopetetaan.")
        else:
            print("Virheellinen komento.")

def lisaa_tavara(tavarat):
    tavara = input ("Minkälaisen esineen haluaisit lisätä tämän kerran? ")
    tavarat.append(tavara)
    return
tavarat = ["Kirja", "Kirje"]        
def inventaario(tavarat):
    print("Vau! Olet löytänyt monta esinettä, inventaariosi sisältää:")
    for t in tavarat:
        print("-" + t)
        return

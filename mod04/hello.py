pituus =float(input('Anna kuhan pituus senttimeterinä:'))
if pituus < 37:
    puuttuu= 37 - pituus
    print("Kuha on alamittainen.")
    print("Laske kuha takaisin järveen.")
    print("Alimmasta sallitusta pyyntimitasta puuttuu", puuttuu, "cm.")


hytti=input("Anna hytti:")
if hytti == "LUX":
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hytti == "A":
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hytti == "B":
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hytti == "C":
    print('C on ikkunaton hytti autokannen alapuolella.')
else: 
    print('Virheellinen hyttiluokka.')


sukupuoli = input("Anna biologinen sukupuoli (nainen/mies):")
hb = float(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen": 
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli =="mies":
    if hb < 134:
            print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
            print("Hemoglobiiniarvo on korkea.")
    else:
            print("Hemoglobiiniarvo on korkea.")


vuosi = int(input("Anna vuosiluku: "))
if vuosi % 400 == 0:
    print('Vuosi on karkausvuosi.')
elif vuosi % 100 == 0:
    print('Vuosi ei ole karkausvuosi.')
elif vuosi % 4 == 0:
    print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')
pituus =float(input('Anna kuhan pituus senttimeterinä:'))
if pituus < 37:
    puuttuu= 37 - pituus
    print("Kuha on alamittainen.")
    print("Laske kuha takaisin järveen.")
    print("Alimmasta sallitusta pyyntimitasta puuttuu", puuttuu, "cm.")
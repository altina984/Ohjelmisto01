import random
def nayta_tiedot(nimi):
    for i in range(6):
        sivumaara = random.randint(1, 1000)
        print(f'{nimi}, {sivumaara} sivua')

nayta_tiedot("Mattinen")
nayta_tiedot("Nukkuminen")

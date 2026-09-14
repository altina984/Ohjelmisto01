def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

gallonat = float(input('Anna gallonmäärä: '))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print('Litroins:', litrat)

    gallonat = float(input('Anna gallonmäärä: '))
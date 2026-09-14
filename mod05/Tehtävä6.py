import random
pisteet = int(input("Anna arvottavien pisteiden määrä: "))
i = 0
sisalla = 0

while i < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        sisalla = sisalla + 1

    i = i + 1
pii = 4 * sisalla / pisteet 
print("Piin likiarvo on:", pii)
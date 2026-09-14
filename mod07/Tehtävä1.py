import random
def heitä_noppaa():
    return random.randint(1, 6)

luku = 0

while luku != 6:
    luku=heitä_noppaa()
    print(luku)
print('Terve Altina!')

import math
sade=5
lukupi=3.1415926
print('Ympyrän pinta-ala on:')
print(sade*sade*lukupi)
print('Ympyrän piiri on:')
print(2*lukupi*sade)

luku1=4
luku2=8
luku3=9
keskiarvo = (4+8+9) / 3
print(luku1 + luku2)
print(luku3 *4)
print(keskiarvo)
print(type(luku1))

leiviskat= float(input("Anna leiviskät.\n"))
naulat= float(input("Anna naulat.\n"))
luodit= float(input("Anna luodit.\n"))
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luodit_yhteensa * 13.3
kilogrammat = int(grammat // 1000)
loput_grammat = grammat % 1000
print("Massa nykymittojen mukaan:")
print(f'{kilogrammat} kilogrammaa ja {loput_grammat:.2f} grammaa.')

import random 
numero1 = random.randint (0, 9)
numero2 = random.randint (0, 9)
numero3 = random.randint (0, 9)
print (numero1, numero2, numero3)

numero4 = random.randint (1, 6)
numero5 = random.randint (1, 6)
numero6 = random.randint (1, 6)
numero7 = random.randint (1, 6)
print(numero4, numero5, numero6, numero7)

pienin = None
suurin = None 
syote = input("Anna luku (Enter lopettaa): ")
while syote != "":
   luku = float(syote)

   if pienin is None or luku < pienin:
      pienin = luku

   if suurin is None or luku > suurin:
      suurin = luku 

   syote = input("Anna luku (Enter lopettaa): ")

   print("Pienin luku:", pienin)
   print("Suurin luku:", suurin)
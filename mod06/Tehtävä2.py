luvut = []
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break
    luvut.append(float(syote))
    luvut.sort(reverse=True)
    for luku in luvut[:5]:
        print(luku)
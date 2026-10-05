kevat =(3, 4, 5)
kesa =(6, 7, 8)
syksy =(9, 10, 11)
talvi =(12, 1, 2)

kuukausi = int(input("Anna kuukauden numero: "))

if kuukausi in kevat:
    print("kevät")
elif kuukausi in kesa:
    print("kesä")
elif kuukausi in syksy:
    print("syksy")
elif kuukausi in talvi:
    print("talvi")
else:
    print("Virheellinen kuukauden numero")
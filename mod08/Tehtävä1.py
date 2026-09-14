Vuodenajat = (
    "Talvi",   # Joulukuu 
    "Talvi",   # Tammikuu
    "Talvi",   # Helmikuu
    "Kevät",   # Maaliskuu
    "kevät",   # Huhtikuu
    "Kevät",   # Toukokuu
    "Kesä",    # Kesäkuu
    "Kesä",    # Heinäkuu
    "Kesä",    # Elokuu
    "Syksy",   # Syyskuu
    "Syksy",   # Lokakuu
    "Syksy",   # Marraskuu
)

kuukausi = int(input("Anna kuukauden numero (1-12):"))

print(Vuodenajat[kuukausi % 12])
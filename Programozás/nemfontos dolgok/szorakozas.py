import random

vicces_uzenetek = [
    "Haha, még mindig nincs meg!",
    "Te vagy a legrosszabb matekos a világon!",
    "Próbáld újra, de most jobban!",
    "Még mindig nem találtad el? Komolyan?",
    "Lehet, hogy a matektanulást kéne újrakezdened.",
]

# Választ egy véletlenszerű számot 1 és 100 között
titkos_szam = random.randint(1, 100)

print("Üdvözöllek a Vicces Találd ki a Számot Játékban!")
print("Próbáld meg kitalálni a gondolt számot 1 és 100 között.")

tippek_szama = 0
while True:
    tipp = int(input("Adj meg egy számot: "))
    tippek_szama += 1

    if tipp == titkos_szam:
        print(f"Gratulálok! Kitaláltad a számot {tippek_szama} próbálkozás után!")
        break
    else:
        vicces_uzenet = random.choice(vicces_uzenetek)
        print(vicces_uzenet)

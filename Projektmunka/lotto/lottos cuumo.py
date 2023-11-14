import random

while True:
    jatekos_szamok = []
    for i in range(5):
        szam = int(input(f"kérem add meg a {i+1}. számot (1-90 között):"))
        if szam < 1 or szam > 90 or szam in jatekos_szamok:
            print("Hibás vagy ismétlődő szám. Kérlek adj meg egy újat.")
        else:
            jatekos_szamok.append(szam)

    lotto_szamok = random.sample(range(1, 91), 5)
    print("az ötös lotto szamai", lotto_szamok)

    talalatok = set(jatekos_szamok).intersection(lotto_szamok)
    print("Találatok:", talalatok)

    if len(talalatok) == 5:
        print("Gratulálok, öt találatod van!")
        break

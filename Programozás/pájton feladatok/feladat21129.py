import random

nevdb=100

vnev=("Nagy","Kiss","Horváth","Kovács","Bogdán","Lakatos","Fazekas")
knev=(
    ("Rikárdó","Leonidász","Naruto","Béla","István"),
    ("Rozalinda","Marika","Piroska","Aranka","Britni")
    )

nevlista=[]

nem=random.randrange(2)
tempnev=random.choice(vnev)+" "+random.choice(knev[nem])
if random.randrange(0,3)==0:
    tempnev+=" "+random.choice(knev[nem])

nevlista.append(tempnev)

print(nevlista)






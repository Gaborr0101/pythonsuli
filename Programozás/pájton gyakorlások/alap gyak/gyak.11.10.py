
def menu(lista):
    for i,elem in enumerate(lista):
        print("{}: {}".format(i+1,elem))

    valasztas=0
    while (valasztas<1 or valasztas>len(lista)) and valasztas!=69:
        try:
            valasztas=int(input("Válassz:"))
        except:
            pass
    return valasztas-1


#lista teszt 

lista=["előre","hátra","jobbra","balra"]

#print("/n".join(lista))

#valasz=menu(lista)
#print(valasz,lista[valasz])

#listateszt vege

tortenet=[
        [
            1,#szál ID
            "Reggel felébredtem. Mit tegyek?",#szöveg ami megjelenik
            ["fogmosás","reggeli","öltözés"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            2,#szál ID
            "Elmegyek fogatmosni,sikálom rendesen,ahogy kell!",#szöveg ami megjelenik
            ["fogmosás","reggeli","öltözés"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
                [
            3,#szál ID
            "Kellene valamit enni! Anya csinált valamit? Nézzük meg!",#szöveg ami megjelenik
            ["fogmosás","reggeli","öltözés"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
                [
            4,#szál ID
            "Kissé hűvös van, kellene valami ruha! \nFelveszek egy nadrágot,meg egy pólót",#szöveg ami megjelenik
            ["fogmosás","reggeli","öltözés","66-os parancs"],#választási lehetőségek
            [2,3,4,66] #hova ugorjon
        ],
        [
            66,#szál ID
            "Vége mindennek",#szöveg ami megjelenik
            [],#választási lehetőségek
            [] #hova ugorjon
        ]
    ]

szalid=1

while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #minta, igy is lehet:
    temp=[e[0] for e in tortenet]
    szalindex=temp.index(szalid)

    print(tortenet[szalindex][1])
    if tortenet[szalindex][2]==[]:
        break

    menupont=menu(tortenet[szalindex][2])

    if menupont == 68:
        break
    #print(tortenet[szalindex])

    szalid=tortenet[szalindex][3][menupont]

print("The End")









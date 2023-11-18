#Lista kiíratás függvénye
def menu(lista):
    for i, elem in enumerate(lista):
        print("{} - {}".format(i+1, elem))

    valasztas = 0

    while (valasztas<1 or valasztas>len(lista)) and valasztas != 69:
        try:
            valasztas = int(input("Válassz egy számot a listából:"))
        except:
            pass

    return valasztas-1

#lista = ["Előre", "Hátra", "Jobbra", "Balra"]
#valasz = menu(lista);
#print(valasz, lista[valasz])

d={ "Reggel felébredtem. Mit tegyek?":"Reggel felébredtem. Mit tegyek?",
          "fogmosás":"fogmosás",
          "reggeli":"reggeli",
          "öltözés":"öltözés"
   }
dEng={ "Reggel felébredtem. Mit tegyek?":"woke up, what to do?",
          "fogmosás":"brush teeth",
          "reggeli":"breakfast",
          "öltözés":"get dressed"
     }



#lehetne igy is:

#l={"Reggel felébredtem. Mit tegyek?",
# "fogmosás",
# "reggeli",
# "öltözés"
# }
#lEng={"woke up, what to do?".
# "brush teeth",
# "breakfast",
# "get dressed"
# }

#import szovegHun as t
# nyelvvalasztas
nyelvlista=["Magyar","English","Deutsch","Russky"]
nyelvid={"Magyar":"szovegHun","English":"szovegEng"}

print("Válassz nyelvet:")
while True:
    nyelvvalasztas=menu(nyelvlista)
    #print(nyelvlista[nyelvvalasztas])
    if nyelvlista[nyelvvalasztas] in nyelvid:
        break
    else:
        print("Sajnos ez a fordítás még nem készült el!")

if nyelvid[nyelvlista[nyelvvalasztas]] =="szovegHun":
           import szovegHUN as t

elif nyelvid[nyelvlista[nyelvvalasztas]] =="szovegEng":
            import szovegEng as t


#import nyelvid[nyelvlista[][nyelvvalasztas] as t

tortenet=[
        [
            1,#szál ID
            t.text["Reggel felébredtem. Mit tegyek?"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"],t.text["Elindulok a buszmegállóba"]], #választái lehetőségek
            [2,3,4,5] # hova ugorjon
        ],
        [
            2,#szál ID
            t.text["Elmegyek fogat mosni. Sikálom rendesen, ahogy kell!"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"],t.text["Elindulok a buszmegállóba"]], #választái lehetőségek
            [2,3,4,5] # hova ugorjon
        ],
        [
            3,#szál ID
            t.text[f"Kellene valamit enni! Anya csinált valamit? Nézzük meg!"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"],t.text["Elindulok a buszmegállóba"]], #választái lehetőségek
            [2,3,4,5] # hova ugorjon
        ],
        [
            4,#szál ID
            t.text["Kissé hűvös van, kellene valami ruha. \nFelveszek egy nadrágot, meg egy pólót!"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"],t.text["Elindulok a buszmegállóba"]], #választái lehetőségek
            [2,3,4,5] # hova ugorjon
        ],
        [
            99,#szál ID
            t.text["asd"], #szöveg
            [], #választái lehetőségek
            [] #hova ugorjon
        ],
                [
            5,#szál ID
            t.text["Elindultam a buszmegállóba. \nMelyik buszra szálljak fel?"], #szöveg
            [t.text["6:50"], t.text["7:05"], t.text["7:20"]], #választái lehetőségek
            [6,7,8,] # hova ugorjon
        ],
                [
            6,#szál ID
            t.text["Felszálltam a 6:50-es buszra, nagyon sokan vannak, így álnom kell"], #szöveg
            [t.text["buszról leszállva várjam meg a barátaimat"],t.text["buszról leszállva menjek az iskolába"]], #választái lehetőségek
            [12,13,] # hova ugorjon
        ],
                [
            7,#szál ID
            t.text["Felszálltam a 7:05-ös buszra, sikerült egy helyet szereznem, így letudtam ülni"], #szöveg
            [t.text["buszról leszállva várjam meg a barátaimat"],t.text["buszról leszállva menjek az iskolába"]], #választái lehetőségek
            [12,13,] # hova ugorjon
        ],
          [
            8,#szál ID
            t.text["Felszálltam a 7:20-as buszra, nem voltak a buszon, így leültem.\nTaláltam a földön 500Ft-ot"], #szöveg
            [t.text["Szóljak a sofőrnek és adjam neki"], t.text["Hagyjam ott"], t.text["Vigyem el"]], #választái lehetőségek
            [9,10,11] # hova ugorjon
        ],
          [
            9,#szál ID
            t.text["A sofőr hülyén néz rám, miközben zsebre teszi a pénzt"], #szöveg
            [t.text["buszról leszállva várjam meg a barátaimat"],t.text["buszról leszállva menjek az iskolába"]], #választái lehetőségek
            [12,13,] # hova ugorjon
        ],
          [
            10,#szál ID
            t.text["A földön hagytam a pénzt, én hülye!"], #szöveg
            [t.text["buszról leszállva várjam meg a barátaimat"],t.text["buszról leszállva menjek az iskolába"]], #választái lehetőségek
            [12,13,] # hova ugorjon
        ],
          [
            11,#szál ID
            t.text["A pént boldogan felvettem a földről( :) )."], #szöveg
            [t.text["buszról leszállva várjam meg a barátaimat"], t.text["Suliba menet elajándékozom a pénzt egy hajléktalannak"], t.text["buszról leszállva menjek az iskolába"]], #választái lehetőségek
            [12,100,13] # hova ugorjon
        ],
              [
            100,#szál ID
            t.text["A csöves örült a pénznek, szebbé tettem a napját\nAmiért kedves votam, kaptam tőle egy szuperkártyát"], #szöveg
            [t.text["A suliba beérve menjek a teremhez"], t.text["A suliba beérve menjek a barátaimhoz"]], #választái lehetőségek
            [14,15] # hova ugorjon
        ],
        [
            12,#szál ID
            t.text["megvártam a barátaimat és együtt mentünk iskolába. "], #szöveg
            [t.text["a suliba beérve menjünk együtt a teremhez"], t.text["Suliba beérve menjünk a többiekhez"]], #választái lehetőségek
            [14,14] # hova ugorjon
        ],
                [
            13,#szál ID
            t.text["Egyedül megyek az iskolába, útközben találkoztam a barátaimmal."], #szöveg
            [t.text["a suliba beérve menjünk együtt a teremhez"], t.text["Suliba beérve menjünk a többiekhez"]], #választái lehetőségek
            [14,14] # hova ugorjon
        ],
                [
            14,#szál ID
            t.text["Odaértünk a teremhez. Ott voltak a többiek. \nNagyon kell pipilni"], #szöveg
            [t.text["óráról majd kikéretőzök"], t.text["menjek el WC-re"]], #választái lehetőségek
            [15,15] # hova ugorjon
        ],
                [
            15,#szál ID
            t.text["Pipiltem \nÓ kicsit mellément. Hoppá! ÁÁÁÁÁÁ! \nElestél és beverted a fejedet...\nEgy földalatti szobában ébredtem fel. Mit tegyek?"], #szöveg
            [t.text["Nézzek körül"], t.text["Várjak, hátha csak képzelődöm"],], #választái lehetőségek
            [16,17] # hova ugorjon
        ],
                            [
            16,#szál ID
            t.text["Körülnéztem, csupán egy út vezet kifelé a szobából"], #szöveg
            [t.text["kimenjek rajta"], t.text["Körülnézzek mégegyszer"],], #választái lehetőségek
            [18,19] # hova ugorjon
        ],
                            [
            17,#szál ID
            t.text["Ez nem képzelődés, jobb lenne inkább körülnézni:)"], #szöveg
            [t.text["Körülnézek"],], #választái lehetőségek
            [18,19] # hova ugorjon
        ]




    ]

szalId=1



while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #másként listák ID kígyűjtése
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(szalId)

    print(tortenet[szalIndex][1])

    if tortenet[szalIndex][2]==[]:
        break

    menuPont = menu(tortenet[szalIndex][2])

    if menuPont == 98:
        break

    szalId=tortenet[szalIndex][3][menuPont]


print("The End")

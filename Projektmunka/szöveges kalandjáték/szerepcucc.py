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
            t.text["Kellene valamit enni! Anya csinált valamit? Nézzük meg! \nHamm Hamm! Fincsi!"], #szöveg
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
            [t.text["buszról leszállva várjam meg a barátaimat"], t.text["buszról leszállva menjek az iskolába"]], #választái lehetőségek
            [12,13] # hova ugorjon
        ],
              
        [
            12,#szál ID
            t.text["megvártam a barátaimat és együtt mentünk iskolába. "], #szöveg
            [t.text["a suliba beérve menjünk együtt a teremhez"], t.text["Suliba beérve menjünk a többiekhez"]], #választái lehetőségek
            [14,14] # hova ugorjon
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
            t.text["Elmentem pipilni...\nPipiltem \nÓ kicsit mellément. Hoppá! ÁÁÁÁÁÁ! \nElestél a saját pipidben és beverted a fejedet...\nEgy földalatti szobában ébredtem fel. Mit tegyek?"], #szöveg
            [t.text["Nézzek körül"], t.text["Várjak, hátha csak képzelődöm"]], #választái lehetőségek
            [16,17] # hova ugorjon
        ],
                            [
            16,#szál ID
            t.text["Körülnéztem, csupán egy út vezet kifelé a szobából"], #szöveg
            [t.text["kimenjek rajta"], t.text["Körülnézzek mégegyszer"]], #választái lehetőségek
            [18,19] # hova ugorjon
        ],
                            [
            17,#szál ID
            t.text["Ez nem képzelődés, jobb lenne inkább körülnézni:)"], #szöveg
            [t.text["Körülnézek"],], #választái lehetőségek
            [16] # hova ugorjon
        ],
                            [
            18,#szál ID
            t.text["Kimentem az ajtón, a másik szobában 3 ajtót látok. \nMelyiken menjek be?"], #szöveg
            [t.text["Jobb oldali kopott ajtó"],t.text["Középső fehér ajtó"],t.text["Bal oldali kopott ajtó"]], #választái lehetőségek
            [20,21,22] # hova ugorjon
        ],
                            [
            19,#szál ID
            t.text["Körülnéztél mégyegyszer, és találtál egy titkos ajtót"], #szöveg
            [t.text["Bemegyek rajta"],t.text["Inkább a korábban felfedezett kijáratot választom"]], #választái lehetőségek
            [23,18] # hova ugorjon
        ],
                            [
            20,#szál ID
            t.text["Bementél a jobb oldali ajtón. \nBent eldobált fegyverek és egy 200 centis páncélos harcos áll veled szemben, aki feléd közelít."], #szöveg
            [t.text["Felkapsz egyet a régi fegyverek közül és nekirontasz"],t.text["Kifutsz a szobából, hátha nem követ"]], #választái lehetőségek
            [24,25] # hova ugorjon
        ],
                            [
            21,#szál ID
            t.text["Bementél a középső ajtón. Egy WC-ben találod magad"], #szöveg
            [t.text["Könnyítesz magadon mert ismét kell"],t.text["Mivel más kijáratot nem látsz kimész vissza"]], #választái lehetőségek
            [26,18] # hova ugorjon
        ],
                            [
            22,#szál ID
            t.text["Bementél a bal oldali ajtón. \n Egy sárkány rohan feléd"], #szöveg
            [t.text["Megpróbálsz elfutni"],t.text["Felkapsz egy lándzsát ami a padlón hever és rátámadsz"]], #választái lehetőségek
            [465,465] # hova ugorjon
        ],
                   [
            23,#szál ID
            t.text["Benyitsz a titkos ajtón, ami egy mély aknába nyílik.\n Leesel a mélybe, ahol más hozzád hasonló pisiben elcsúszó kölök tervezi a szabadulást."], #szöveg
            [t.text["Csatlakozol te is a terv megbeszéléséhez"],t.text["Kimaradsz a megbeszélésből"]], #választái lehetőségek
            [50,99] # hova ugorjon
        ],
     [
            50,#szál ID
            t.text["Megbeszéltétek, hogy felmásztok a szakadékba...\n hát nem leestél? (de) \n legalább szépet estél...\nThe End"], #szöveg
            [t.text["Csatlakozol te is a terv megbeszéléséhez"],t.text["Kimaradsz a megbeszélésből"]], #választái lehetőségek
            [50,99] # hova ugorjon
        ],
        [
            99,#szál ID
            t.text["Mivel kimaradtál, nem bírták a képed...\n péppé lettél verve...(R.I.P.)\nThe End"], #szöveg
            [], #választái lehetőségek
            [] # hova ugorjon
        ],
                           [
            24,#szál ID
            t.text["A lovag kiüti a kezedből a kardot és földhözvág. Ez bukta!!\nThe End"], #szöveg
            [], #választái lehetőségek
            [] # hova ugorjon
        ],
                                   [
            25,#szál ID
            t.text["Kifutsz és eltorlaszolod az ajtót a folyosón lévő szekrénnyel. \nMelyik másik ajtót válasszam?"], #szöveg
            [t.text["Középső fehér ajtó"],t.text["Bal oldali kopott ajtó"]], #választái lehetőségek
            [21,22] # hova ugorjon
        ],
                                   [
            26,#szál ID
            t.text["Végre újra pipiltem.\n ÁÁÁÁÁÁÁÁ! \nMár megint elestél és beverted a fejed...\n felébredtél a suli WC-ben\nThe End"], #szöveg
            [], #választái lehetőségek
            [] # hova ugorjon
        ],
                                       [
            465,#szál ID
            t.text["A sárkány tüzet okád rád, majd az égő fájdalom közben rángatózva felébredsz a suli WC-ben :)\nThe End"], #szöveg
            [], #választái lehetőségek
            [] # hova ugorjon
        ],



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
#    if szalId==100:
#        kartya.append("szuperkártya")
    menuPont = menu(tortenet[szalIndex][2])

    if menuPont == 98:
        break
    if menuPont == 464:
        break
    if menuPont == 23:
        break
    if menuPont == 25:
        break
    if menuPont == 49:
        break

   

    szalId=tortenet[szalIndex][3][menuPont]


print("The End")

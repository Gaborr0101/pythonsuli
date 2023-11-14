import random
bekert = ""
while bekert != 0:
    valaszto=["Ötöslottó", "Hatoslottó", "Skandináv","Totó"]
    for i,elem in enumerate(valaszto):
        print(i+1,":", elem)
    print("0 : Kilépés")
    print("*"*60)
    bekert = int(input("Adj meg egy számot 0-4-ig:"))-1;
    if bekert+1 == 0:
        break
    while bekert not in range((len(valaszto))):
        try:
            bekert = int(input("Adj meg egy számot 0-4-ig:"))-1;
            if  bekert not in range(len(valaszto)):
                raise
        except:
            print("A listából válassz")
    print("*"*60)
    bekert+=1
    def kiiratas(lista):
            for i in range(len(lista)):
                print(lista[i]);
    if bekert == 1:
        #hatos
        hatosLista = []

        while len(hatosLista)<= 5:
            randomSzam = random.randint(1,45);
            if randomSzam not in hatosLista:
                hatosLista.append(randomSzam)

        print("A géppel sorsolt Hatoslottó számok:")
        kiiratas(hatosLista)
        print("*"*60)
    elif bekert == 3:
        #skandinav

        skandiLista = []

        while len(skandiLista)<= 6:
            randomSzam = random.randint(1,35);
            if randomSzam not in skandiLista:
                skandiLista.append(randomSzam)
                
        print("A géppel sorsolt Skandináv lottó számok:")
        kiiratas(skandiLista)
        print("*"*60)
    elif bekert == 4:
        #otos
        otosLista = []

        while len(otosLista)<= 4:
            randomSzam = random.randint(1,90);
            if randomSzam not in otosLista:
                otosLista.append(randomSzam)

        print("A gép áltál sorsolt Ötöslottó számok:")
        kiiratas(otosLista)
        print("*"*60)
    elif bekert == 2:
        
        #toto
        toto=["1","2","x"];
        toto2=[];
        while len(toto2)<= 13:
            index = random.randint(0,2);
            toto2.append(toto[index]);
        print("A géppel sorsolt Totó számok:")
        for i,elem in enumerate(toto2[:-1]):
            print(i+1,':',elem)
        print("13+1 :",toto2[-1])
        print("*"*60)
    elif bekert == 0:
        break

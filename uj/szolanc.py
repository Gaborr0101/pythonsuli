szavak=[]

while True:
    szo=input("Adj meg egy szót:")
    if len(szo)!=6:
        print("A karakterek száma téves!")
        break
    elif szo[-1]!=szavak[-1][0]:
        print("Nem illeszkedett!")
    elif len(szo)==6:
        szavak.append(szo)

    


    
 











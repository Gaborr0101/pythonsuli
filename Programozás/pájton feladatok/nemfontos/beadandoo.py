import random
def pszamok(lista):
    
    pszamok=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            pszamok.append(lista[i])
    return pszamok

def prtlnszamok(lista):
    
    prtlnszamok=[]
    osszeg=0
    for i in range(len(lista)):
        if lista[i]%2==1:
            prtlnszamok.append(lista[i])
    for szam in prtlnszamok:
        osszeg+=szam
        
    return osszeg

def paros_szamok_szama(lista):
    parosok = [szam for szam in lista if szam % 2 == 0]
    return len(parosok)






szam=[]
while len(szam)<500:
        i=random.randrange(10000,99999)
        if i not in szam:
            szam.append(i)

def felekosszehasonlitas(lista):
    hossz = len(lista)    
    if hossz % 2 == 0:
        felek = hossz // 2
    else:
        felek = hossz // 2 + 1
    
    elsofel = sum(lista[:felek])
    masodikfel = sum(lista[felek:])
    
    if elsofel > masodikfel:
        return "Az első fele nagyobb."
    elif elsofel < masodikfel:
        return "A második fele nagyobb."
    else:
        return "A két fél egyenlő."
eredmeny = felekosszehasonlitas(szam)


print(pszamok(szam))
print("Ennyi páratlan számok osszege:: "+str(prtlnszamok(szam))+"")
print (eredmeny)


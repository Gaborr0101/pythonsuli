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



szam=[]
while len(szam)<500:
        i=random.randrange(10000,99999)
        if i not in szam:
            szam.append(i)


print(pszamok(szam))
print()
print("A páratlan számok: "+str(prtlnszamok(szam))+"")


element=3
szam.index(element)

print(szam)

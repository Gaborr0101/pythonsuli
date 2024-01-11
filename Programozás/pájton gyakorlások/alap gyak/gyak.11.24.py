import random

def parosdb(lista):
    return len([i for i in lista if i%2==0])
   
szamok=[random.randrange(10000,100000) ]
def prtlnosszeg(lista):
    print("a páratlan számok összege ennyi:()".format([i for i in lista if i%2==1]))

if sum(szamok[:len(szamok)//2]) > sum(szamok[len(szamok)//2:]):
    print("első fele nagyobb")
elif sum(szamok[:len(szamok)//2]) > sum(szamok[len(szamok)//2:]):
    print("masodik fele nagyobb")

else:
    print("Egyenlők.")


db=len([i for i in szamok if i//10000==3])
db=len([i for i in szamok if str(i)[0]=="3"])
db=len([i for i in szamok if str(i).startswith("3")])
print(db)

dblista=[[i for i in szamok if i//10000==k]for k in range(10)]
print(dblista)


szamok=[random.randrange(10000,1000000) for _ in range(500)]
#print(szamok)

szam= math.floor(random.random()*db)*lepes+eltolas
print(szam)





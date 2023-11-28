
import random
import math

def veletlen(mettol, meddig, lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol

    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam


#szamok=[]
#r=veletlen(10,21)
#for _ in range(r):
#    r2=veletlen(10,21)
#    temp=[]
#    for _ in range(r2):
#        temp.append(veletlen(160,201))
#    szamok.append(temp)

#print(szamok)

szamok=[[veletlen(160,201) for _ in range(veletlen(10,21))] for _ in range(veletlen(10,21))]
print(szamok)




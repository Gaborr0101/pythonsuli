#mértékegység átváltó
#Gyarmati Gábor 2023.10.06
#projektfeladat

tipusok=["hosszúság", "Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + Térfogat"]

egysegek=[["mm","cm","dm","m","km"],
           ["mm2","cm2","dm2","m2","km2"],
           ["mm3","cm3","dm3","m3","km3"],
           [],
           [],
           []]
valtok=[[10,10,10,1000,1],
           [100,100,100,1000000,1],
           [1000,1000,1000,1000000000,1],
           [],
           [],
           []]



print("#"*80)
#for elemtípusok
#   print(elem)

for i,elem in enumerate(tipusok):
    print("\t"+str(i+1)+":",elem)
print("\t0: Kilepes")

tipusId="alma"
while tipusId=="alma" or tipusId not in range(len(tipusok)+1):
    try:
        tipusId=int (input("válaszd ki melyiket szeretnéd:"))
        if tipusId not in range(len(tipusok)+1):
            raise 
        
    except:
        print("Válassz a listából!")

print("#"*80)
tipusId-=1
print("tipus:", tipusok[tipusId])
print("mértékegységek:")

print("forrás:")
for i,elem in enumerate(egysegek[tipusId]):
    print("\t"+str(i+1)+":",elem)
print("\t0: Vissza")
    
egysegId="alma"
while egysegId=="alma" or egysegId not in range(len(egysegek[tipusId])+1):
    try:
        egysegId=int (input("válaszd ki melyiket szeretnéd:"))
        if egysegId not in range(len(egysegek[tipusId])+1):
            raise 
        
    except:
        print("Válassz a listából!")

print("cél:")
for i,elem in enumerate(egysegek[tipusId]):
    print("\t"+str(i+1)+":",elem)
print("\t0: Vissza")
    
egysegId2="alma"
while egysegId2=="alma" or egysegId2 not in range(len(egysegek[tipusId])+1):
    try:
        egysegId2=int (input("válaszd ki melyiket szeretnéd:"))
        if egysegId2 not in range(len(egysegek[tipusId])+1):
            raise 
        
    except:
        print("Válassz a listából!")

szam=float(input("Mennyiség: "))

        
egysegId-=1
egysegId2-=1
if egysegId<egysegId2:
    #print(valtok[tipusId][egysegId:egysegId2])
    szorzo=1
    for e in valtok[tipusId][egysegId:egysegId2]:
        szorzo*=e
    eredmeny=szam/szorzo

else:
     #print(valtok[tipusId][egysegId2:egysegId])
    szorzo=1
    for e in valtok[tipusId][egysegId2:egysegId]:
        szorzo*=e
    eredmeny=szam*szorzo
     
print(szam, egysegek[tipusId][egysegId], eredmeny, egysegek[tipusId][egysegId2])





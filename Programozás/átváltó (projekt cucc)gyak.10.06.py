#mértékegység átváltó
#Gyarmati Gábor 2023.10.06
#projektfeladat

tipusok=["hosszúság", "Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + Térfogat"]

print("#"*80)
#for elemtípusok
#   print(elem)


for i,elem in enumerate(tipusok):
    print("\t"+str(i+1)+":",elem)
print("\t0: Kilepes")

tipusId="alma"
while tipusId=="alma":
    try:
        tipusId=int (input("válaszd ki melyiket szeretnéd:"))
    except:
        print("Válassz a listából!")

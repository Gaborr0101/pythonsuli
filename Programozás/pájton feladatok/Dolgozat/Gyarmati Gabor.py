adatok=[]
f=open("helsinki.txt")
for sor in f:
    adatok.append(sor.strip().split(","))


f.close()


print(adatok)


lista=[]

beker="menjébe"

while beker !="":
    beker=input("adj meg valamit: ")
    if beker != "":
        lista.append(beker)

print(lista)
utolso=lista[-3:]
utolso.sort()

lista.sort()

for e in lista:
    print(e)

for e in lista[-3:]:
    print(e)

for e in utolso:
    print(e)



#hf hozzunk létre egy listát, kérj be egy számot, ha lehetséges arra helyre szurj be egy másik adatot     



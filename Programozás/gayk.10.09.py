lista=["a","b","z","h","c","i","o"]

print(lista)

for elem in lista:
    print(elem)

print("#"*30)

for i in range(len(lista)):
    print(lista[i])

print("#"*30)

for elem in lista[:3]:
    print(elem)
    
print("#"*30)
for elem in lista[3:]:
    print(elem)
    
print("#"*30)

for elem in lista[-2:]:
    print(elem)
    
print("#"*30)

for elem in lista[::-1]:
    print(elem)

print("#"*30)

lista2=lista[1:-1]
print(lista2)

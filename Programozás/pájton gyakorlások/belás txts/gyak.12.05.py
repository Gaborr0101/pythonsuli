f=open("bela.txt","w")

#f.write("1")
for i in range(100):
    f.write(str(i)+"\n")
f.close()


#open("bela2.txt","w").write("\n".join(range(100)))

open("bela2.txt","w").write("\n".join([str(i) for i in range(100)]))

f=open("bela.txt","r")
lista=[]
for egysor in f:
    lista.append(egysor.strip())
f.close()
print(lista)

f=open("bela.txt","r")
lista=[egysor.strip() for egysor in f.readlines()]
f.close()
f=open("bela.txt")
lista2=map(lambda x: x.strip(), f.readlines())
print(list(lista2),"qwe")

lista=[]
f=open("bela.txt","r")
lista=f.read().strip().split("\n")
print(lista)
f.close()




def maxKeres(lista):
    legnagyobb=lista[0]
    maxindex=0
    for i in range(len(lista)):
        if lista[i]>legnagyobb:
            legnagyobb=lista[i]
            maxindex=i
    return(legnagyobb,maxindex)



lista=[100,35,69,42,73,55,66,33,22,70,81]


legnagyobb,maxindex=maxKeres(lista)
print(maxindex,legnagyobb)

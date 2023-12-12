import random

#12 fő, 8-12 jegy, jegy:1-5

jegyek=[]

for i in range(12):
    for k in range(random.randrange(8,13)):
        jegy=random.randrange(1,6)
        egydiak.appemd(jegy)
    jegyek.append(egydiak)



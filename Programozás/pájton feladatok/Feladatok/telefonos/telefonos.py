
adatok=[]
f=open("hivas.txt")
for sor in f:
    temp=[]
    tempsor=sor.split(" ")
    #['"6", "51", "8", "54"']
    for e in tempsor:
        temp.append(int(e))
    
    temp.append(temp[3]*60*60+temp[4]*60+temp[5]-temp[0]*60*60+temp[1]*60+temp[2])



    adatok.append(temp)






f.close()

print(adatok)




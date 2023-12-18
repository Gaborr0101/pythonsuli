
import math

a=int(input("a:"))
b=int(input("b:")) 

c = math.sqrt(a**2 + b**2)

print("c: ", c)

if c-c//1==0:
    print("egész")
else:
    print("nem egész")

for a in range(1,100):
    for b in range (a,100):
        c = math.sqrt(a**2 + b**2)
        if c-c//1==0:
            print(a,b,c)

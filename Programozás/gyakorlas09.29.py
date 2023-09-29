
import math

a=int(input("a:"))
b=int(input("b:")) 

c = math.sqrt(a**2 + b**2)

print("c: ", c)

if c-c//1==0:
    print("egész")
else:
    print("nem egész")

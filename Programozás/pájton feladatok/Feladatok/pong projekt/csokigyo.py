#egyszerű pong játék
#Start: 2024.01.31
#End: 
#Boti Lóránt
#tanár: Papp Péter

from tkinter import *
import random

def rajzol ():
    
    #labdaColor, red, green, blue=atmenetColor(red,green,blue)
    #print(labdaColor)
    labdaPos[0]+= labdaSpeed[0]*labdaSize
    labdaPos[1]+= labdaSpeed[1]*labdaSize

    if labdaPos[0] > win.winfo_width() or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        labdaColor = randomcolor()
    if labdaPos[1] > win.winfo_height() or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        labdaColor = randomcolor()

    labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize, fill= "green", outline = ""))

    if len(labdaLista) > labdaListaHossz:
        canvas.delete(labdaLista[0])
        labdaLista.pop(0)

    win.after(jatekSpeed,rajzol)

kajak= []

def kaja ():
    x= random.randint(0,win.winfo_width()-kajaSize)
    y= random.randint(0,win.winfo_height()-kajaSize)
    kajak.append(canvas.create_oval(x,y,x+kajaSize,y+kajaSize, fill= "red", outline = ""))

    win.after(kajaSpeed,kaja)
'''
ütközés 
def collisionDetection():
    sb = playground.bbox(kaja)
    sb = playground.bbox(labda)
    if ab[0] < sb[2] < ab[2] and ab[1] < sb[1] < ab[3]:
        playground.move(labda,50,50)


'''

    

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return ("#"+hex(r)[-2:]+hex(g)[-2:]+hex(b)[-2:]).replace("x","0")

def gombLe(e):
    if e.keysym=="Up":
        #print("fel")
        labdaSpeed[0]=0
        labdaSpeed[1]=-1

    elif e.keysym=="Down":
        #print("le")
        labdaSpeed[0]=0
        labdaSpeed[1]=1

    elif e.keysym=="Left":
        #print("bal")
        labdaSpeed[0]=-1
        labdaSpeed[1]=0
    elif e.keysym=="Right":
        #print("jobb")
        labdaSpeed[0]=1
        labdaSpeed[1]=0
    #print(e)

jatekSpeed = 500
kajaSpeed = 5000
jatekHatter = "lightgray"

def atmenetColor(red,green,blue):
    red+=5
    if red>255:
        red = red-255
        green+=5
    if green>255:
        green = green-255
        blue+=5
    if blue>255:
        blue = blue-255

    return ("#"+hex(red)[-2:]+hex(green)[-2:]+hex(blue)[-2:]).replace("x","0"),red, green, blue
    
print(randomcolor())


win = Tk()
win.geometry("600x600+100+20")
win.title("Pong játék")
canvas = Canvas(win, bg=jatekHatter)
canvas.pack(fill=BOTH, expand= 1)



#labda = canvas.create_oval(0,0,100,100,fill="red")

labdaSpeed = [0,0]
labdaPos = [200,200]
labdaSize = 20
kajaSize = 20
labdaColor = "green"
red, green, blue = 0,0,0
labdaLista = []
labdaListaHossz= 1

win.bind("<KeyPress>", gombLe)
win.after(jatekSpeed,rajzol)
win.after(kajaSpeed,kaja)

win.mainloop()


while True:
    canvas.update()





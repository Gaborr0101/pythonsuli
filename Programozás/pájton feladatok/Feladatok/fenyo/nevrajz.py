import transzformaciok
from tkinter import *


win=Tk()

win.geometry("1000x1000")

canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")

canvas.pack(fill = BOTH, expand = 1)



gbetu = [
    [0,0,100,0,100,10,20,10,20,90,80,90,80,70,40,70,40,60,100,60,100,100,0,100,0,0],
    [0,0,100,0,100,10,20,10,20,90,80,90,80,70,40,70,40,60,100,60,100,100,0,100,0,0]
]

     


              


gbetu2=[]

for e in gbetu:
        e=transzformaciok.nagyit(e,1)
        e=transzformaciok.eltol(e, 100, 100)
        e=transzformaciok.forgat(e, 45)
        gbetu2.append(e)
#print(gbetu2)
gbetu2=transzformaciok.forgat(gbetu2,-45)

for e in gbetu2:
        canvas.create_line(e,width=5,fill="black")

win.mainloop()
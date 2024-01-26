import transzformaciok
from tkinter import *


win=Tk()

win.geometry("1000x1000")

canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")

canvas.pack(fill = BOTH, expand = 1)



gbetu = [
    [0,0,100,0,100,10,20,10,20,90,80,90,80,70,40,70,40,60,100,60,100,100,0,100,0,0],
    [0,0,100,0,100,10,20,10,20,90,80,90,80,70,40,70,40,60,100,60,100,100,0,100,0,0]]
gbetu2=[
    [400, 200, 600, 200, 600, 220, 440, 220, 440, 380, 560, 380, 560, 340, 480, 340, 480, 320, 600, 320, 600, 400, 400, 400, 400, 200], 
 [400, 200, 600, 200, 600, 220, 440, 220, 440, 380, 560, 380, 560, 340, 480, 340, 480, 320, 600, 320, 600, 400, 400, 400, 400, 200]
]

hatter="ffffF"
betuszinek=["red",hatter,"blue"]
     


              


"""gbetu2=[]

for e in gbetu:
        e=transzformaciok.nagyit(e,1)
        e=transzformaciok.eltol(e, 100, 100)
        e=transzformaciok.forgat(e, 45)
        gbetu2.append(e)
"""
gbetu=transzformaciok.eltol(gbetu,50,1)
gbetu=transzformaciok.nagyit(gbetu,2)

#print(gbetu2)
gbetu2=transzformaciok.masol(gbetu)
gbetu2=transzformaciok.forgat(gbetu2,0)
gbetu2=transzformaciok.nagyit(gbetu2,2)
gbetu2=transzformaciok.eltol(gbetu2,50,10)
print(gbetu2)

canvas.create_line(gbetu,width=5,fill="black")

"""for e in gbetu2:
        canvas.create_line(e,width=5,fill="black")
"""        
       
while True:
    canvas.delete("all")
    gbetu2=transzformaciok.forgat(gbetu2,1)
    
    for i,e in enumerate(gbetu2):
       # canvas.create_line(e,width=2,fill="green")
       canvas.create_polygon(e,fill=betuszinek[i],outline='blue')


    win.update_idletasks()
    win.update()
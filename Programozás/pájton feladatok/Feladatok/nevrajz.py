import transzformaciok
from tkinter import *

win=Tk()

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)



gbetu = [0,0,100,0,100,25,35,25,35,90,75,90,75,65
        
        ]
     


              




fenyo2masolat=transzformaciok.eltol(gbetu, 100, 100)
canvas.create_line(gbetu,width=5,fill="green")










win.mainloop()
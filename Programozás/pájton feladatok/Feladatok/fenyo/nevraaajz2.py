import transzformaciok

from tkinter import *


# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x600")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH, expand = 1)

fenyo2=[200,0,
		0,100,
		150,100,
		0,200,
		150,200,
		0,300,
		150,300,
		150,400,
		250,400,
		250,300,
		400,300,
		250,200,
		400,200,
		250,100,
		400,100,
		200,0]
pepa=[[0,0,0,17,3,17,3,6,21,6,21,0],#P
        [3,2,3,4,19,4,19,2],
        #E
        [4,7,4,17,9,17,9,15,6,15,6,13,8,13,8,11,6,11,6,9,9,9,9,7],
        #P
        [10,7,10,17,12,17,12,13,15,13,15,7],
        [12,9,12,11,13,11,13,9],
        #A
        [16,7,16,17,18,17,18,13,19,13,19,17,21,17,21,7],
        [18,9,18,11,19,11,19,9]]

pepa=[
		[0,0,0,17,3,17,3,6,21,6,21,0],#P
        [3,2,3,4,19,4,19,2]
	]
#vonal bezár
pepa2=[x.extend(x[:2]) for x in pepa]


#pepa2=[transzformaciok.nagyit(x,10) for x in pepa]
#pepa2=[transzformaciok.eltol(x,10,10) for x in pepa2]
"""pepa2=[]
for e in pepa:
	pass
	e=transzformaciok.nagyit(e,10)
	e=transzformaciok.eltol(e,100,100)
	e=transzformaciok.forgat(e,90)

	pepa2.append(e)
"""

for e in pepa2:
	e=transzformaciok.nagyit(e,10)
	e=transzformaciok.eltol(e,300,300)
	e=transzformaciok.forgat(e,90)

	#pepa2.append(e)

for e in pepa2:
	canvas.create_line(e,width=2,fill="blue")

pepa2=transzformaciok.forgat(pepa,90)
pepa2=transzformaciok.nagyit(pepa2,10)
pepa2=transzformaciok.eltol(pepa2,100,100)
pepa2=transzformaciok.forgat(pepa,190)

for e in pepa2:
	canvas.create_line(e,width=2,fill="blue")


#fenyo2Masolat=transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(pepa2[0],width=1,fill="green")
#canvas.create_line(pepa2[1],width=1,fill="green")


win.mainloop()
"""
speed=0.01
while True:
	canvas.delete("all")
	pepa2=transzformaciok.forgat(pepa2,speed)

	for e in pepa2:
		canvas.create_polygon(e, fill='red', outline='blue')
		#id=canvas.create_line(e,width=2,fill="blue")
		#canvas.itemconfigure(id, fill='green', width=2)

	win.update_idletasks()
	win.update()
"""
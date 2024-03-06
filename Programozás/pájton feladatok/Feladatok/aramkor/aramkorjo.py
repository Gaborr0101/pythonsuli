#Áramkör
#Start: 2024.02.16
#Gyarmati Gábor
from tkinter import *
import random
import math


class Jel:
	x = 0
	y = 0
	meret = 100
	szin="black"


	def __init__(self,x,y,meret,canvas):
		self.x=x
		self.y=y
		self.meret=meret
		self.r=self.meret*0.06
		#bekotesi pont=bkp by bence
		self.bkp=[[self.x,self.y+self.meret*0.5],[self.x+self.meret,self.y+self.meret*0.5]]
		self.canvas=canvas
		self.selected=False
		self.rajz()


	def kattint(self, event):
		self.selected=not self.selected
		print("katt")
		self.rajz()


	def rajz(self, vonalak=[],korok=[]):
		self.elemek=[]
		if self.selected:
			keret=self.meret*0.1
		else:
			keret=self.meret*0.03
		
		self.elemek.append(self.canvas.create_rectangle(self.x, self.y, self.x+self.meret, self.y+self.meret, fill="grey", width=keret))

		for egyvonal in vonalak:
			self.elemek.append(self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin))
		for egykor in korok:
			self.elemek.append(self.canvas.create_oval(egykor, outline=self.szin, width=self.meret*0.03))
		self.canvas.tag_bind(self.elemek[0], '<Button-1>', self.kattint)


	def vezetek(self,masik, sajatbkp=1, masikbkp=0):
		tavSajat=-self.meret*0.2 + sajatbkp*2*self.meret*0.2 
		tavMasik=-masik.meret*0.2 + masikbkp*2*masik.meret*0.2 
		vastagsag=self.meret*0.03
		#első után a másik, közelebbi pontok
		#	*****
		#	*   *--
		#	***** |
		#         |     *****
		#          -----*   *
		#               *****
		# 1. eset
		if (sajatbkp==1 and masikbkp==0) and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]:
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					(self.bkp[sajatbkp][0]+masik.bkp[masikbkp][0])/2,	self.bkp[sajatbkp][1],
					(self.bkp[sajatbkp][0]+masik.bkp[masikbkp][0])/2,	masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="red"
		#első alatt/felett a másik, közelebbi pontok
		#	*****
		#	*   *--
		#	*****  |
		#      ----
		#     | *****
		#      -*   *
		#       *****
		# 2. eset
#		elif ((sajatbkp==1 and masikbkp==0) and self.x < masik.x < self.x+self.meret)\
#				or ((sajatbkp==1 and masikbkp==0) and self.x > masik.x):
		elif ( masikbkp==0) \
				and (masik.x < self.x+self.meret)\
				and not((self.y<masik.y<self.y+self.meret) or masik.y<self.y<masik.y+masik.meret):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavMasik, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavMasik, masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="green"
		#első alatt/felett a másik, távolabbi pontok
		#	*****
		#	*   *-----
		#	*****     |
		#             |
		#       ***** |
		#       *   *-
		#       *****
		# 3. eset
		elif (((sajatbkp==1 and masikbkp==1) and self.x < masik.x < self.x+self.meret)) \
				or ((sajatbkp==1 and masikbkp==1) \
						and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]\
						and (self.bkp[sajatbkp][1]<masik.y \
		   					or self.bkp[sajatbkp][1]>masik.y+masik.meret)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0]+tavSajat, self.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0]+tavSajat, masik.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="blue"
		#első után a másik, távolabbi pontok
		#	*****
		#	*   *-------------
		#	*****             |
		#               ***** |
		#               *   *-
		#               *****
		# 4. eset
		elif (sajatbkp==1 and masikbkp==1) and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]:
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					(self.bkp[sajatbkp][0]+masik.x)/2,					self.bkp[sajatbkp][1],
					(self.bkp[sajatbkp][0]+masik.x)/2,					masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2,							masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2,							masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="yellow"
		
		# 5. eset
		elif ((sajatbkp==1 and masikbkp==1) \
						and self.bkp[sajatbkp][0] > masik.bkp[masikbkp][0]\
						and (self.bkp[sajatbkp][1]<masik.y \
		   					or self.bkp[sajatbkp][1]>masik.y+masik.meret)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavSajat, masik.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="pink"

		# 6. eset
		elif (((sajatbkp==0 and masikbkp==1) and self.x > masik.x)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]-tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]-tavSajat, masik.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="orange"
		# 7. eset
		elif (((sajatbkp==0 and masikbkp==1) and self.x < masik.x < self.x+self.meret)) \
				or ((sajatbkp==0 and masikbkp==1) \
						and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]\
						and (self.bkp[sajatbkp][1]<masik.y \
		   					or self.bkp[sajatbkp][1]>masik.y+masik.meret)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavMasik, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavMasik,  masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="lightblue"
		# 8. eset
		elif (((sajatbkp==0 and masikbkp==0) and self.x < masik.x < self.x+self.meret)) \
				or ((sajatbkp==0 and masikbkp==0) \
						and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]\
						and (self.bkp[sajatbkp][1]<masik.y \
		   					or self.bkp[sajatbkp][1]>masik.y+masik.meret)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavMasik, (self.y+self.meret+masik.y)/2,
					masik.bkp[masikbkp][0]+tavMasik,  masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="lightgreen"
		# 9. eset
		elif (sajatbkp==0 and masikbkp==1) and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]:
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 					self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 					min(self.y-self.meret*0.2,masik.y-masik.meret*0.2),
					masik.x+masik.meret*1.2,							min(self.y-self.meret*0.2,masik.y-masik.meret*0.2),
					masik.x+masik.meret*1.2,							masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="brown"
		# 10. eset
		elif (sajatbkp==0 and masikbkp==0) and self.bkp[sajatbkp][0] < masik.bkp[masikbkp][0]:
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 					self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 					min(self.y-self.meret*0.2,masik.y-masik.meret*0.2),
					(self.bkp[sajatbkp][0]+masik.x)/2,					min(self.y-self.meret*0.2,masik.y-masik.meret*0.2),
					(self.bkp[sajatbkp][0]+masik.x)/2,					masik.bkp[masikbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="navy"
			#vastagsag=self.meret*0.1
		# 11. eset
		elif ((sajatbkp==1 and masikbkp==1) \
						and self.bkp[sajatbkp][0] > masik.bkp[masikbkp][0]\
						and ((self.y<masik.y<self.y+self.meret) or masik.y<self.y<masik.y+masik.meret)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 	self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 	self.y-self.meret*0.2,
					masik.bkp[masikbkp][0]+tavSajat, 	self.y-self.meret*0.2,
					masik.bkp[masikbkp][0]+tavSajat, 	masik.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="gold"
			#vastagsag=self.meret*0.1
		# 12. eset
		elif (( masikbkp==0) \
						and self.bkp[sajatbkp][0] > masik.bkp[masikbkp][0]\
						and ((self.y<masik.y<self.y+self.meret) or masik.y<self.y<masik.y+masik.meret)):
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 	self.bkp[sajatbkp][1],
					self.bkp[sajatbkp][0]+tavSajat, 	min(self.y-self.meret*0.2,masik.y-masik.meret*0.2),
					masik.bkp[masikbkp][0]+tavMasik, 	min(self.y-self.meret*0.2,masik.y-masik.meret*0.2),
					masik.bkp[masikbkp][0]+tavMasik, 	masik.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="magenta"
			#vastagsag=self.meret*0.1
		#minden más esetben ferde vonallal összekötés
		# utolsó eset
		else:
			vonalak=[
				[
					self.bkp[sajatbkp][0], self.bkp[sajatbkp][1],
					masik.bkp[masikbkp][0], masik.bkp[masikbkp][1],
				],
			]
			self.szin="black"

		for egyVonal in vonalak:
			self.canvas.create_line(egyVonal, width=vastagsag, fill=self.szin)


class Elem(Jel):
	def rajz(self):
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.45, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.45, self.y+self.meret*0.2,
				self.x+self.meret*0.45, self.y+self.meret*0.8,
			],
			[
				self.x+self.meret*0.55, self.y+self.meret*0.4,
				self.x+self.meret*0.55, self.y+self.meret*0.6,
			],
			[
				self.x+self.meret*0.55, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		Jel.rajz(self,vonalak)


class Kapcsolo(Jel):
	def rajz(self):
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.333-self.r, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.333+self.r, self.y+self.meret*0.5,
				self.x+self.meret*0.666-self.r, self.y+self.meret*0.3,
			],
			[
				self.x+self.meret*0.666+self.r, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		korok=[
			[
				self.x+self.meret*0.333-self.r, self.y+self.meret*0.5-self.r,
				self.x+self.meret*0.333+self.r, self.y+self.meret*0.5+self.r
			],
			[
				self.x+self.meret*0.666-self.r, self.y+self.meret*0.5-self.r,
				self.x+self.meret*0.666+self.r, self.y+self.meret*0.5+self.r
			]
		]
		Jel.rajz(self,vonalak,korok)


class Lampa(Jel):
	def rajz(self):
		self.r=self.meret*0.25
		dx=self.r/math.sqrt(2)
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.5-self.r, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.5-dx, self.y+self.meret*0.5-dx,
				self.x+self.meret*0.5+dx, self.y+self.meret*0.5+dx,
			],
			[
				self.x+self.meret*0.5-dx, self.y+self.meret*0.5+dx,
				self.x+self.meret*0.5+dx, self.y+self.meret*0.5-dx,
			],
			[
				self.x+self.meret*0.5+self.r, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		korok=[
			[
				self.x+self.meret*0.5-self.r, self.y+self.meret*0.5-self.r,
				self.x+self.meret*0.5+self.r, self.y+self.meret*0.5+self.r
			],
		]
		Jel.rajz(self,vonalak,korok)


class Ellenallas(Jel):
	def rajz(self):
		
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.25, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.25, self.y+self.meret*0.4,
				self.x+self.meret*0.25, self.y+self.meret*0.6,
				self.x+self.meret*0.75, self.y+self.meret*0.6,
				self.x+self.meret*0.75, self.y+self.meret*0.4,
				self.x+self.meret*0.25, self.y+self.meret*0.4,
			],
			[
				self.x+self.meret*0.75, self.y+self.meret*0.5,
				self.x+self.meret*1.0, self.y+self.meret*0.5,
			],
		]
		
		Jel.rajz(self,vonalak)
#ablak létrehozása
win=Tk()

jatekHatter="lightgray"
jatekSpeed=10

#ablak mérete
win.geometry("1000x600")

win.title("Áramkör")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)


lampa1=Lampa(200,220,100,canvas)

kapcs=[]
kapcs.append(Kapcsolo(450,350,100,canvas))
kapcs.append(Kapcsolo(250,350,100,canvas))
kapcs.append(Kapcsolo(450,50,100,canvas))
kapcs.append(Kapcsolo(250,50,100,canvas))
kapcs.append(Kapcsolo(50,350,100,canvas))
kapcs.append(Kapcsolo(50,50,100,canvas))
kapcs.append(Kapcsolo(650,200,100,canvas))



#ellenallas1=Ellenallas(0,150,100,canvas)
for egyElem in kapcs:
	for masikbkp in [0,1]:
		for sajatbkp in [0,1]:
			#sajatbkp=0
			lampa1.vezetek(egyElem,sajatbkp=sajatbkp,masikbkp=masikbkp)









win.mainloop()
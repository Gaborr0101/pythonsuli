class furdoclass :
    def __init__(self, sor):
        vag=sor.split(" ")
        self.vendeg=int(vag[0])
        self.reszleg=int(vag[1])
        self.belepett=vag[2]==0
        self.ora=int(vag[0])
        self.perc=int(vag[0])
        self.masodperc=int(vag[0])



        def ido(self):
            return ":".join(self.ora, self.perc, self.masodperc)
        

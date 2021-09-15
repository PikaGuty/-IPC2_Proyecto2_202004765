class Obj_Simulacion():
    def __init__(self,nombreS,ListP):
        self.nombreS=nombreS
        self.ListP=ListP
        self.sig = None
    
    #Métodos GET
    def getNombreS(self):
        return self.nombreS

    def getListP(self):
        return self.ListP

    #Métodos SET
    def setNombreS(self,nombreS):
        self.nombreS = nombreS

    def setListP(self,ListP):
        self.ListP = ListP

    def setSig(self,sig):
        self.sig = sig
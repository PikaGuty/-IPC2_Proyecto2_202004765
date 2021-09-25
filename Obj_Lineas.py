class Obj_Linea():
    def __init__(self,NLinea,CComponentes,TEnsamblaje):
        self.NLinea=NLinea
        self.CComponentes=CComponentes
        self.TEnsamblaje=TEnsamblaje
        self.sig = None
    
    #Métodos GET
    def getNLinea(self):
        return self.NLinea

    def getCComponentes(self):
        return self.CComponentes

    def getTEnsamblaje(self):
        return self.TEnsamblaje

    #Métodos SET
    def setNLinea(self,NLinea):
        self.NLinea = NLinea

    def setCComponentes(self,CComponentes):
        self.CComponentes= CComponentes
    
    def setTEnsamblaje(self,TEnsamblaje):
        self.TEnsamblaje= TEnsamblaje

    def setSig(self,sig):
        self.sig = sig

class Lista_Lineas():
    def __init__(self):
        self.primero = None

    def insertar(self, nNode):
        if self.primero:
            uNode = self.primero
            while uNode.sig != None:
                uNode = uNode.sig
            uNode.sig = nNode
        else:
            self.primero = nNode
 
    def mostrar(self):
        tNode = self.primero
        while tNode != None:
            print('No. Linea: '+str(tNode.getNLinea())+', Cantidad de Componentes: '+str(tNode.getCComponentes())+', Tiempo Ensamblaje: '+str(tNode.getTEnsamblaje()), end='<-')
            tNode = tNode.sig

        print('Null')

    def retornar_seleccionado(self, n):
        tNode = self.primero 
        c=1
        while tNode != None:
            if n is c:
                return tNode
            tNode = tNode.sig
            c+=1

    def tiempoE(self, L,t):
        tNode = self.primero 
        c=1
        while tNode != None:
            if L is tNode.getNLinea():
                return tNode.getTEnsamblaje()
            tNode = tNode.sig
            c+=1

    def EliminarP(self):
        tNode = self.primero
        if tNode is None:
            print("Cola vacía")
        else:
            tNode = tNode.sig
            self.primero = None
            self.primero=tNode
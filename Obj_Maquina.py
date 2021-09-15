class Obj_Maquina():
    def __init__(self,NoLineas,ListLineas,ListProductos):
        self.NoLineas=NoLineas
        self.ListLineas=ListLineas
        self.ListProductos=ListProductos
        self.sig = None
    
    #Métodos GET
    def getNoLineas(self):
        return self.NoLineas

    def getListLineas(self):
        return self.ListLineas

    def getListProductos(self):
        return self.ListProductos

    #Métodos SET
    def setNoLineas(self,NoLineas):
        self.NoLineas = NoLineas

    def setListLineas(self,ListLineas):
        self.ListLineas= ListLineas
    
    def setListProductos(self,ListProductos):
        self.ListProductos= ListProductos

    def setSig(self,sig):
        self.sig = sig

class Lista_Maquina():
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

    def retornar_seleccionado(self, n):
        tNode = self.primero 
        c=1
        while tNode != None:
            if n is c:
                return tNode
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
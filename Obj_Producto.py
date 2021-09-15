class OProd():
    def __init__(self,nombre,cola):
        self.nombre=nombre
        self.cola=cola
        self.sig = None
    
    #Métodos GET
    def getNombre(self):
        return self.nombre

    def getCola(self):
        return self.cola

    #Métodos SET
    def setNombre(self,nombre):
        self.nombre = nombre

    def setCola(self,cola):
        self.cola = cola

    def setSig(self,sig):
        self.sig = sig

class Lista_Productos():
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
            print('Nombre: '+str(tNode.getNombre())+', Cola: ('+str(tNode.getCola())+')', end='<-')
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

    def EliminarP(self):
        tNode = self.primero
        if tNode is None:
            print("Cola vacía")
        else:
            tNode = tNode.sig
            self.primero = None
            self.primero=tNode

class nodoProd():
    def __init__(self,linea,componente):
        self.linea = linea
        self.componente = componente
        self.sig = None

    #Métodos GET
    def getLinea(self):
        return self.linea

    def getComponente(self):
        return self.componente

    #Métodos SET
    def setLinea(self,linea):
        self.linea = linea

    def setComponente(self,componente):
        self.componente = componente
    
    def setSig(self,sig):
        self.sig = sig

class ColaProd():
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
            print('('+str(tNode.getLinea())+','+str(tNode.getComponente())+')', end='<-')
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

    def EliminarP(self):
        tNode = self.primero
        if tNode is None:
            pass
        else:
            tNode = tNode.sig
            self.primero = None
            self.primero=tNode


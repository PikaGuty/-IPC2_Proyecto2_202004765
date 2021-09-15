class Obj_ProductoS():
    def __init__(self,nombre):
        self.nombre=nombre
        self.sig = None
    
    #Métodos GET
    def getNombre(self):
        return self.nombre

    #Métodos SET
    def setNombre(self,nombre):
        self.nombre = nombre

    def setSig(self,sig):
        self.sig = sig

class Lista_ProductosS():
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
            print(str(tNode.getNombre()), end='<-')
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
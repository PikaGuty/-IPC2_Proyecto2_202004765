import tkinter as tk
class nodoE():
    def __init__(self,linea,estado):
        self.linea = linea
        self.estado = estado
        self.sig = None

    #Métodos GET
    def getLinea(self):
        return self.linea

    def getEstado(self):
        return self.estado

    #Métodos SET
    def setLinea(self,linea):
        self.linea = linea

    def setEstado(self,estado):
        self.estado = estado
    
    def setSig(self,sig):
        self.sig = sig

class ColaE():
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
            pass
        else:
            tNode = tNode.sig
            self.primero = None
            self.primero=tNode

    def mostrar(self,listEnsam):
        tNode = self.primero
        while tNode != None:
            print("Linea "+str(tNode.getLinea())+" "+str(tNode.getEstado()))
            listEnsam.insert(tk.END, "Linea "+str(tNode.getLinea())+" "+str(tNode.getEstado()))
            tNode = tNode.sig

      

    def Modificar(self, L, E):
        tNode = self.primero 
        x=1
        while tNode != None:
            if L is tNode.getLinea():
                tNode.setEstado(E)
                #print('('+str(tNode.getLinea())+','+str(tNode.getComponente())+')')
                return tNode
            tNode = tNode.sig
            x+=1

    def ObEstado(self, L, E):
        tNode = self.primero 
        x=1
        while tNode != None:
            if L is tNode.getLinea():
                return tNode.getEstado()
            tNode = tNode.sig
            x+=1
class nodoS():
    def __init__(self,linea,componente,posicion,estado):
        self.linea = linea
        self.componente = componente
        self.posicion = posicion
        self.estado=estado
        self.sig = None

    #Métodos GET
    def getLinea(self):
        return self.linea

    def getComponente(self):
        return self.componente

    def getPosicion(self):
        return self.posicion

    def getEstado(self):
        return self.estado

    #Métodos SET
    def setLinea(self,linea):
        self.linea = linea

    def setComponente(self,componente):
        self.componente = componente

    def setPosicion(self,posicion):
        self.posicion = posicion

    def setEstado(self,estado):
        self.estado = estado
    
    def setSig(self,sig):
        self.sig = sig

class ColaS():
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
            print('('+str(tNode.getLinea())+','+str(tNode.getComponente())+','+str(tNode.getPosicion())+','+str(tNode.getEstado())+')', end='<-')
            tNode = tNode.sig

        print('Null')

    def imp(self, anterior,n):
        tNode = self.primero
        

        for cc in range(int(n)+1):
            if cc!=0:
                L=anterior.retornar_seleccionado(cc).getLinea()
                C=anterior.retornar_seleccionado(cc).getComponente()
                P=anterior.retornar_seleccionado(cc).getPosicion()
                if L==tNode.getLinea():
                    if P==tNode.getPosicion():
                        print('Linea '+str(tNode.getLinea())+' ensamblando componente '+str(tNode.getPosicion())+'')
                    else:
                        print('Linea de ensamblaje '+str(tNode.getLinea())+' mover brazo '+str(tNode.getPosicion())+'')
                    tNode = tNode.sig
        

        

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

    def Modificar(self, L, C, P, E):
        tNode = self.primero 
        x=1
        while tNode != None:
            ttNode=tNode
            if L is tNode.getLinea():
                tNode.setComponente(C)
                tNode.setPosicion(P)
                tNode.setEstado(E)
                #print('('+str(tNode.getLinea())+','+str(tNode.getComponente())+')')
                return tNode
            tNode = tNode.sig
            x+=1

    def ModificarE(self, L, E):
        tNode = self.primero 
        x=1
        while tNode != None:
            ttNode=tNode
            if L is tNode.getLinea():
                tNode.setEstado(E)
                #print('('+str(tNode.getLinea())+','+str(tNode.getComponente())+')')
                return tNode
            tNode = tNode.sig
            x+=1
'''
cola=ColaS()
cola.insertar(nodoS(1,2,0))
cola.insertar(nodoS(2,1,0))
cola.insertar(nodoS(3,1,0))
cola.mostrar()
cola.Modificar(1,4,4)
cola.mostrar()
cola.Modificar(1,3,7)
cola.mostrar()
cola.Modificar(2,3,9)
cola.mostrar()
cola.Modificar(1,4,1)
cola.mostrar()
cola.Modificar(1,4,'esperando')
cola.mostrar()
cola.Modificar(1,4,5)
cola.mostrar()
colaa=cola
cola=ColaS()
cola.mostrar()
colaa.mostrar()
colaa.EliminarP()
colaa.mostrar()
print(cola.retornar_seleccionado(1))'''

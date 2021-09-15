import xml.etree.ElementTree as ET
from Obj_Producto import nodoProd, ColaProd, Lista_Productos, OProd
from Obj_Lineas import Obj_Linea, Lista_Lineas
from Obj_Maquina import Obj_Maquina, Lista_Maquina

listaP=Lista_Productos()
listaL=Lista_Lineas()
listaLineas=Lista_Maquina()

class AMaquina:
    def AnalizarArchivoM(ruta):
        
        archivo=ET.parse(ruta)
        raiz = archivo.getroot()
        
        for CLProd in raiz.findall('CantidadLineasProduccion'):
            CantLProd=CLProd.text
            #print('Cantidad de lineas de produccion '+CantLProd)
            
        for LLProd in raiz.findall('ListadoLineasProduccion'):
            for LProd in LLProd.findall('LineaProduccion'):

                num=LProd.find('Numero').text
                cantC=LProd.find('CantidadComponentes').text
                TEnsam=LProd.find('TiempoEnsamblaje').text
                listaL.insertar(Obj_Linea(num,cantC,TEnsam))

                

        for LProd in raiz.findall('ListadoProductos'):
            for Prod in LProd.findall('Producto'):
                cola=ColaProd()
                nom=Prod.find('nombre').text
                LElab=Prod.find('elaboracion').text

                #print('Nombre'+nom)
                #print('Listado Elaboracion'+LElab)
                Analiz=Analizador()
                coola=Analiz.analizar(LElab+'#',cola)
                
                listaP.insertar(OProd(nom,coola))
                #listaP.mostrar()
                #for x in range(1000):
                    #cola.EliminarP()

        listaLineas.insertar(Obj_Maquina(CantLProd,listaL,listaP))         
        return listaLineas           
                

class Analizador():
    def estado0(self,caracter,cola):
        self.buffer=''
        #Comparacion de caracteres
        if caracter=='L':
            self.estado = 1          
        else:
            pass     

    def estado1(self,caracter,cola):
        
        if caracter.isdigit():
            self.buffer+=caracter
        elif caracter=='C':
            self.linea=self.buffer
            self.buffer=''
            
        elif caracter==' ':
            self.componente=self.buffer
            self.buffer=''
            cola.insertar(nodoProd(self.linea,self.componente))
            self.estado = 0
        else:
            self.componente=self.buffer
            self.buffer=''
            cola.insertar(nodoProd(self.linea,self.componente))
            

    def analizar(self, cadena,cola):
        self.i = 0
        self.continuar=True
        self.estado=0
        self.linea=''
        self.componente=''
        while self.i < len(cadena):
            if self.continuar:
                if self.estado == 0:
                    self.estado0(cadena[self.i],cola)
                elif self.estado == 1:
                    self.estado1(cadena[self.i],cola)
                self.i += 1
        return cola
            




#listaL.mostrar()



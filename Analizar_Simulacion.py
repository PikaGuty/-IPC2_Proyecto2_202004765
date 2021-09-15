import xml.etree.ElementTree as ET
from Obj_ProductoS import Lista_ProductosS, Obj_ProductoS
from Obj_Simulacion import Obj_Simulacion

ListP=Lista_ProductosS()


class ASimulacion:
    def AnalizarArchivoS(ruta):
        
        archivo=ET.parse(ruta)
        raiz = archivo.getroot()
        
        for nom in raiz.findall('Nombre'):
            NombreS=nom.text

        for Prod in raiz.findall('ListadoProductos'):
            for p in Prod.findall('Producto'):
                NombreP=p.text
                ListP.insertar(Obj_ProductoS(NombreP))
                #ListP.insertar(Obj_ProductoS(NombreP))

        Simulacion=(Obj_Simulacion(NombreS,ListP))
        return Simulacion

            

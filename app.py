from Obj_Producto import OProd as OProd
from Obj_Producto import nodoProd
from Obj_Producto import ColaProd

cola=ColaProd()

class op1:
    def IOrden():
        print("\n\n")
        print("******************* Ingresar Orden *******************")
        Fila=input("Ingrese Fila\n")
        Componente=input("Ingrese Componente\n")
        
        cola.insertar(nodoProd(Fila,Componente))
        print("Ingresada Fila: "+Fila+" Componente "+Componente)

        cola.mostrar()

op1.IOrden()
        
    
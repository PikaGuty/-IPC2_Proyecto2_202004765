from tkinter import *
from tkinter import ttk

root = Tk()
##
root.title("Bitxelart")
root.iconbitmap("favicon.ico")
root.resizable(False,False)
root.geometry("1000x600")

tabControl = ttk.Notebook(root)

tab1 = Frame(tabControl)
tab1.config(bg="#B0B0B0", width=1000, height=600)
tabControl.add(tab1, text = 'Cargar Archivo')

tab2 = Frame(tabControl)
tab2.config(bg="#B0B0B0", width=1000, height=600)
tabControl.add(tab2, text = 'Analizar Archivo')

tab3 = Frame(tabControl)
tab3.config(bg="#B0B0B0", width=1000, height=600)
tabControl.add(tab3, text = 'Ver Reportes')

tab4 = Frame(tabControl)
tab4.config(bg="#B0B0B0", width=1000, height=600)
tabControl.add(tab4, text = 'Seleccionar Imagen')

tab5 = Frame(tabControl)
tab5.config(bg="#B0B0B0", width=1000, height=600)
tabControl.add(tab5, text = 'Ver Imagen')

tabControl.pack()

root.mainloop()
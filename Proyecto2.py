from tkinter import *
from tkinter import ttk
from typing import Sized
from PIL import ImageTk, Image

class app():
    def __init__(self):
        self.root = Tk()
        
        #Configurando ventana
        self.root.title("DIGITAL INTELLIGENCE S.A.")
        self.root.iconbitmap("icono.ico")
        self.root.resizable(False,False)
        self.root.geometry("675x650")
        self.root.configure(bg="#1D1E1B")

        #Agregando menú
        self.menu()

        #Titulo
        Label(self.root,text="DIGITAL INTELLIGENCE S.A.",fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 30, "bold"),borderwidth = 2,width = 30,relief="ridge").place(x=20,y=20)

        self.tabControl = ttk.Notebook(self.root)

        img=PhotoImage(file='min.png')
        self.Proceso(img)
        self.Reportes(img)
        
        self.tabControl.place(x=20,y=75)
        self.root.mainloop()

    def menu(self):
        menubar = Menu(self.root)

        #Menú Cargar
        Cmenu = Menu(menubar)
        Cmenu.add_command(label="Archivo de configuración")
        Cmenu.add_command(label="Archivo de simulación")
        Cmenu.add_command(label="Salir")
        menubar.add_cascade(label="Cargar", menu=Cmenu)

        #Menú Ayuda
        Amenu = Menu(menubar)
        Amenu.add_command(label="Información del estudiante", command=self.InfoE)
        Amenu.add_command(label="Información de la aplicación", command=self.InfoA)

        menubar.add_cascade(label="Ayuda", menu=Amenu)

        self.root.config(menu=menubar)

    def Reportes(self,img):
        self.root.option_add('*TCombobox*Listbox*Background', '#1D1E1B')
        self.root.option_add('*TCombobox*Foreground', '#D90808')
        self.root.option_add('*TCombobox*Font', ("Fixedsys", 14, "bold"))
        

        tab1 = Frame(self.tabControl)
        tab1.config(bg="#1D1E1B", width=635, height=525)
        
        Label(tab1, text="Reporte HTML: ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=10)
        #componentes
        componentes = Frame(tab1)
        scrollbarY = ttk.Scrollbar(componentes,orient=VERTICAL)
        scrollbarX = ttk.Scrollbar(componentes,orient=HORIZONTAL)
        self.listbox = Listbox(componentes, width=32, height=9, xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set, bg="#1D1E1B", fg="#D90808",font=("Fixedsys", 14, "bold"))
        for i in range(20):
            self.listbox.insert(END, "Elementoooooooooooooooooooooooooooooooo {}".format(i))
        scrollbarY.config(command=self.listbox.yview)
        scrollbarY.pack(side=RIGHT, fill=Y)
        scrollbarX.config(command=self.listbox.xview)
        scrollbarX.pack(side=BOTTOM, fill=X)
        self.listbox.pack()
        componentes.place(x=10,y=40)


        Label(tab1, text="Reporte de cola de secuencia: ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=275)
        #componentes
        componentes = Frame(tab1)
        scrollbarY = ttk.Scrollbar(componentes,orient=VERTICAL)
        scrollbarX = ttk.Scrollbar(componentes,orient=HORIZONTAL)
        self.listbox = Listbox(componentes, width=32, height=9, xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set, bg="#1D1E1B", fg="#D90808",font=("Fixedsys", 14, "bold"))
        for i in range(20):
            self.listbox.insert(END, "Elementoooooooooooooooooooooooooooooooo {}".format(i))
        scrollbarY.config(command=self.listbox.yview)
        scrollbarY.pack(side=RIGHT, fill=Y)
        scrollbarX.config(command=self.listbox.xview)
        scrollbarX.pack(side=BOTTOM, fill=X)
        self.listbox.pack()
        componentes.place(x=10,y=305)

        
        Button(tab1,text='Generar',fg="#FFFFFF", bg="#D90808", font=("Fixedsys", 14, "bold")).place(x=450,y=130)
        Button(tab1,text='Generar',fg="#FFFFFF", bg="#D90808", font=("Fixedsys", 14, "bold")).place(x=450,y=400)
        self.tabControl.add(tab1, text = 'Reportes')

    def Proceso(self,img):
        self.root.option_add('*TCombobox*Listbox*Background', '#1D1E1B')
        self.root.option_add('*TCombobox*Foreground', '#D90808')
        self.root.option_add('*TCombobox*Font', ("Fixedsys", 14, "bold"))
        

        tab1 = Frame(self.tabControl)
        tab1.config(bg="#1D1E1B", width=635, height=525)
        
        Label(tab1, text="Archivo de configuración: ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=10)
        Ruta1=Label(tab1, text="...", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=30)

        Label(tab1, text="Archivo de simulación: ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=60)
        Ruta2=Label(tab1, text="...", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=80)

        Label(tab1, text="Selecciona el producto a trabajar: ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=110)
        comboExample = ttk.Combobox(tab1, values=["op1","op2","op3","op4"]).place(x=10,y=140)

        Label(tab1, text="Componentes necesarios: ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=10,y=180)
        #componentes
        componentes = Frame(tab1)
        scrollbar = ttk.Scrollbar(componentes,orient=VERTICAL)
        self.listbox = Listbox(componentes, width=19, height=5, yscrollcommand=scrollbar.set, bg="#1D1E1B", fg="#D90808",font=("Fixedsys", 14, "bold"))
        for i in range(20):
            self.listbox.insert(END, "Elemento {}".format(i))
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack()
        componentes.place(x=10,y=210)


        #componentes
        componentes = Frame(tab1)
        scrollbarY = ttk.Scrollbar(componentes,orient=VERTICAL)
        scrollbarX = ttk.Scrollbar(componentes,orient=HORIZONTAL)
        self.listbox = Listbox(componentes, width=32, height=13, xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set, bg="#1D1E1B", fg="#D90808",font=("Fixedsys", 14, "bold"))
        for i in range(20):
            self.listbox.insert(END, "Elementoooooooooooooooooooooooooooooooo {}".format(i))
        scrollbarY.config(command=self.listbox.yview)
        scrollbarY.pack(side=RIGHT, fill=Y)
        scrollbarX.config(command=self.listbox.xview)
        scrollbarX.pack(side=BOTTOM, fill=X)
        self.listbox.pack()
        componentes.place(x=250,y=210)

        pb = ttk.Progressbar(tab1,orient='horizontal',mode='determinate',length=230).place(x=10,y=350)

        tabimg = Canvas(tab1,width=100,height=100, bg="black")
        tabimg.create_image(0,0,image=img,anchor="nw")
        tabimg.place(x=10,y=400)

        tiempo=Label(tab1, text="tiempo ", wraplength=890,fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 14, "bold")).place(x=120,y=440)

        Button(tab1,text='Iniciar',fg="#FFFFFF", bg="#D90808", font=("Fixedsys", 14, "bold")).place(x=530,y=160)

        self.tabControl.add(tab1, text = 'Proceso')

    def InfoE(self):
        win = Toplevel()
        win.wm_title("Window")
        win.resizable(False,False)
        win.config(height=200,width=530,bg="#1D1E1B")
        win.title("Información del estudiante")
        win.iconbitmap("icono.ico")

        Label(win, text="Javier Alejandro Gutierrez de León",fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 15, "bold")).place(x=10,y=10)
        Label(win, text="202004765",fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 15, "bold")).place(x=10,y=40)
        Label(win, text="Introducción a la Programación y Computación 2 sección A",fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 15, "bold")).place(x=10,y=70)
        Label(win, text="Ingeniería en Ciencias y Sistemas",fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 15, "bold")).place(x=10,y=100)
        Label(win, text="4to Semestre",fg="#D90808", bg="#1D1E1B", font=("Fixedsys", 15, "bold")).place(x=10,y=130)

        Button(win,text='Aceptar',fg="#FFFFFF", bg="#D90808", font=("Fixedsys", 14, "bold"),command=win.destroy).place(x=210,y=155)

    def InfoA(self):
        win = Toplevel()
        win.wm_title("Window")
        win.resizable(False,False)
        win.config(height=230,width=530,bg="#1D1E1B")
        win.title("Información de la aplicación")
        win.iconbitmap("icono.ico")

        Label(win, text="En esta aplicación se pueden crear simulaciones del tiempo que toma ensamblar un producto que se solicite, según la configuración establecida por el usuario. \n\n Programado en Python 3.9.6 \n Reportes generados con Graphviz y HTML5",fg="#D90808", wraplength=510,bg="#1D1E1B", font=("Fixedsys", 15, "bold")).place(x=10,y=10)
        

        Button(win,text='Aceptar',fg="#FFFFFF", bg="#D90808", font=("Fixedsys", 14, "bold"),command=win.destroy).place(x=210,y=180)


app()
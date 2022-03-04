from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import io
from io import *
class interfaz:
    root = object()
    bCargar = object()
    e2 = object()
    def __init__(self):
        global root 
        global bCargar
        global e2
        root = Tk()
        root.geometry('600x500')
        root.config(bg = 'thistle4')
        root.title('Formulario Dinámicos ')
        bCargar = Button(text="Cargar Archvo",command=  self.CargarArchivo)
        # relx = y = relheigth="Altura " width = altura 
        bCargar.place(x=10 , y=20 , height=50 ,width=150)
        bCargar.config(bg="thistle2")
        bCargar.config()
        
        e2 = Text(root, show=None, font=('Arial', 14))  # Mostrar como texto sin formato
        e2.place(x=10, y=75 ,height=200, width=500)
        
        #Reportes
        comboReportes =  ttk.Combobox(state="readonly")
        comboReportes.place(x=300,y=20,height=45,width=200)
        
        comboReportes['values'] = ('Repoorte  de Tokens',
                                    'Repoorte  de Errores',
                                    'Repoorte  de Usuario',
                                    'Repoorte  de Tecnico',
                                    'Reportes')
        comboReportes.current('4')
        
        bAnalizar = Button(text="Analizar Archvo", command= self.AnalizarArchivo)
        # relx = y = relheigth="Altura " width = altura 
        bAnalizar.place(x=10 , y=300 , height=50 ,width=150)
        bAnalizar.config(bg="thistle2")
        bAnalizar.config()




        root.mainloop()

    
    Instrucciones='' 
    def CargarArchivo(self):
        print("Boton Cargar Archivo")

        
        #Abre Ventana para Buscar el archivo .lfp 
        archivo =  filedialog.askopenfilename(initialdir = "/") 
            #Abre el achivo 
        archivo_texto = open(archivo ,'r',encoding="utf8")
            #Contenido del archivo leido 
        texto = archivo_texto.read()
        archivo_texto.close()
            #Analiza el contenido del Archivo 
        
        global Instrucciones
        Instrucciones = texto
        
        print("Archivo de Instrucciones .flp")
        print(Instrucciones)
        print("----------------------------")
        global e2
        e2.get("1.0", "end-1c")
        e2.insert( INSERT,Instrucciones)



    def AnalizarArchivo(self):
        print("Analizar Archivo")
    
   
    



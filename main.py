
#librerias 
import os
import tkinter 
from tkinter import *
from tkinter import filedialog
import io
from io import *
from automatadatos import *
from mes import* 
from automata_instrucciones import *
entradaInstrucciones = automata_instrucciones()
entradaData = automatadatos()
Data =[]
Entrada = ''
Mes=[]
def menu1():
    """
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
    #os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    
    print ("Selecciona una opción")
    print ("\t1 -  Cargar Data  ")
    print ("\t2 - Cargar Instrucciones ")
    print ("\t3 - Analizar")
    print ("\t4 - Reportes")
    print ("\t5  - salir")
        #Menu Principal del Programaa

def MenuPrincipal(): 
    while True:
        # Mostramos el menu
        menu1()
    
        # solicituamos una opción al usuario
        opcionMenu = input("Seleccione una opcion >> ")
    
        if opcionMenu=="1":
           print("---->Carga de Datos")
           CargarData()

        elif opcionMenu=="2":
            print("---->Cargar Instrucciones")
            CargarInstrucciones()
            global Instrucciones
            
            print("entrada analizador ")
            entradaInstrucciones.automataInstrucciones(Instrucciones)     
        elif opcionMenu=="3":
            print("Analizar")
            global Entrada
            print(Entrada)
            entradaData.analizador(Entrada)
            
            
        elif opcionMenu =="4":
            print("Datos ")
            entradaData.imprimir()
            print("<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>")
                    
                   
                    

           
                

        elif opcionMenu=="5":
                    break
        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n pulsa una tecla para continuar")


#Carga del Archivo .data
def CargarData():
    
    
    root = Tk()
        #Abre Ventana para Buscar el archivo .data 
    archivo =   filedialog.askopenfilename(initialdir = "/") 
        #Abre el achivo 
    archivo_texto = open(archivo ,'r',encoding="utf8")
        #Contenido del archivo leido 
    texto = archivo_texto.read()
    archivo_texto.close()
        #Analiza el contenido del Archivo 
    
    global Entrada
    Entrada = texto
    root.destroy()
    print("Archivo del Mes .Data ")
    print(Entrada)
    print("--------------------------------------")
    
    #Carga Instrucciones  .flp
Instrucciones = ''
    
def CargarInstrucciones():
    
    
    root=Tk()
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
    root.destroy()
    print("Archivo de Instrucciones .flp")
    print(Instrucciones)
    print("----------------------------")


if __name__ == "__main__":
   MenuPrincipal()
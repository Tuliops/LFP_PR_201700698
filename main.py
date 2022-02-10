
#librerias 
import os
import tkinter 
from tkinter import *
from tkinter import filedialog
import io
from io import *
from automatadatos import *

entradaData = automatadatos()
Data =[]
Entrada = ''

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
                
                    
        elif opcionMenu=="3":
            print("Analizar")
            global Entrada
            print(Entrada)
            entradaData.analizador(Entrada)
        elif opcionMenu =="4":
            print("Reportes")
            for x in entradaData.listaProductos:
                    print(x.getNombre() ," ", x.getPrecio())
        elif opcionMenu=="5":
                    break
        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n pulsa una tecla para continuar")


#Carga del Archivo .data
def CargarData():
    
    

        #Abre Ventana para Buscar el archivo .data 
    archivo =  filedialog.askopenfilename(initialdir = "/") 
        #Abre el achivo 
    archivo_texto = open(archivo ,'r',encoding="utf8")
        #Contenido del archivo leido 
    texto = archivo_texto.read()
    archivo_texto.close()
        #Analiza el contenido del Archivo 
    print(texto)
    global Entrada
    Entrada = texto
    print(Entrada)
    

    #Carga Instrucciones  .flp
def CargarInstrucciones():
    
    

        #Abre Ventana para Buscar el archivo .lfp 
    archivo =  filedialog.askopenfilename(initialdir = "/") 
        #Abre el achivo 
    archivo_texto = open(archivo ,'r',encoding="utf8")
        #Contenido del archivo leido 
    texto = archivo_texto.read()
        #Analiza el contenido del Archivo 
    print(texto)

if __name__ == "__main__":
   MenuPrincipal()
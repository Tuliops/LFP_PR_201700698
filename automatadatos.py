import re
from mes import *
from producto import *


nuevoMes=mes("nombre", "año","producots" )

class automatadatos:
    def __init__(self):
        self.signos={'=':"igual",':':"dosPuntos",'(':"abreParentesis",
                    ')':"cierraParentesis",'"':"comillas",'[':"abreCorchete",
                    ']':"cierraCorchete",',':"coma"}
        self.listaTokens =[]
        self.error = []

    #Variables Golbales para productos
    NameProduct = ''
    PriceProduct=''
    cantidadProduct = ''

    def analizador(self, entrada):
        lex = ""
        estado = 1
        indice = 0

        while indice< len(entrada):
            #Estado 1: Verifiacion de Caracteres 
            #Estado 1: verificacion de Nombre
            #Estado 2: Verificacion de Año
            #Estado 3: verificacion de productos 
                #Estado 4 : Nombre del producto
                #Estado 5 : Precio del Producto
                #Estado 6 : Cantidad del producto
                #Estado 0 : Nada Salir 
                #con  )<-- termina un mes 
            
            if estado == 1:
                #Verifica si el caracter es una letra 
                
                if re.search(r"[a-zA-Z]", entrada[indice]):
                    lex += entrada[indice]
                    indice += 1
                    
                    estado = 1
                    #Verifica si termino el nombre 
                    #Dos puntos y comienza el año 
                elif re.search(r"[:]" , entrada[indice]):
                    nombreMes = lex
                    print("Nombre del Mes :",nombreMes)
                    #envia a estaod 2 para verificar año 
                    estado = 2
                    lex=''
                elif re.search(r"[(]", entrada[indice]):
                    estado = 3
                    indice += 1
                    
                else:
                    lex+=entrada[indice]
                    estado = 1 
                    indice+=1
            #Verificador Año 
            if estado == 2:
                #Verifica si el caracter y separa el año 
                if re.search(r"[0-9]", entrada[indice]):
                    lex += entrada[indice]
                    indice +=1
                    estado = 2
                    #Si es = termina el año y comienzan los productos 
                elif re.search(r"[=]", entrada[indice]):
                    anioMes=lex
                    print("Año del Mes: ",anioMes)
                    
                    indice += 1
                    lex =''
                    #Envia a estado de los productos
                    estado = 1
                else:
                    #Si no se Encuentra el caracter aumetna indice y sigue en estado 2 de verificacion
                    lex += entrada[indice]
                    indice += 1
                    estado = 2 
                    #Reportar error si el caracter no esta en los parametros 
            # Estado de Verificacion de productos
            # Se verificaran Nuevos producos   
             
            if estado == 3:

                if re.search(r"[\[]", entrada[indice]):
                    indice += 1
                    estado = 4
                #Verificacion de entrada y salida de productos 
                
                elif re.search(r"[ ]", entrada[indice]):
                    estado=3
                    indice += 1

                elif re.search(r"[;]", entrada[indice]):
                    #Fin de Un Producto
                    indice += 1
                    estado = 3
                    lex = ''
                    #Fin de productos
                elif re.search(r"[\n]", entrada[indice]):
                    indice += 1
                    estado = 3


                elif re.search(r"[)]", entrada[indice]):

                    indice+=1
                    estado = 1

                else :
                       #Si no se Encuentra el caracter aumetna indice y sigue en estado 3 de verificacion
                    lex += entrada[indice]
                    indice += 1
                    estado = 3
            #Verificar Nombre del Producto
            if estado == 4 :
                

                if re.search(r"[a-zA-Z]", entrada[indice]):
                    lex += entrada[indice]
                    indice += 1
                    estado = 4
                elif re.search(r"[0-9]", entrada[indice]):
                    lex += entrada[indice]
                    indice += 1
                    estado = 4
                elif re.search(r"[ ]", entrada[indice]):
                    lex += entrada[indice]
                    indice += 1
                    estado = 4
                    #la , es el separado del precio
                    #envia a estado 5 que verifica el precio 
                elif re.search(r"[,]", entrada[indice]):
                    print("----------Nuevo Producto-------------")
                    global NameProduct
                    NameProduct = lex
                    print("producto : ",NameProduct)
                    indice += 1
                    estado = 5
                    
                    lex = ''
                
                
                elif re.search(r"[\“]", entrada[indice]):
                    indice += 1
                    estado = 4
                elif re.search(r"[\”]", entrada[indice]):
                    indice += 1
                    estado = 4
                else : 
                    
                    
                    indice +=1
                    estado = 3
            #Verificar el precio del producto 
            if estado == 5:
                if re.search(r"[0-9]", entrada[indice]):
                    lex += entrada[indice]
                    estado = 5
                    indice +=1
                elif re.search(r"[\.]", entrada[indice]):
                    lex += entrada[indice]
                    estado = 5
                    indice +=1
                elif re.search(r"[ ]", entrada[indice]):
                    indice +=1
                    estado = 5
                    #Separador de Cantidad envia a estado 6
                elif re.search(r"[,]", entrada[indice]):
                    indice +=1
                    estado = 6
                    global PriceProduct
                    PriceProduct = lex
                    print("Precio ", PriceProduct)
                    lex = ''
                    
               
    

                else :
                    estado = 4
                    indice +=1

            #Verificar la cantidad del producto 
            if estado ==6:
                    if re.search(r"[0-9]", entrada[indice]):
                        lex += entrada[indice]
                        estado = 6
                        indice +=1
                        #Fin de un producto regresa a estado 5 
                    elif re.search(r"[]]", entrada[indice]):
                        indice += 1
                        global cantidadProduct
                        cantidadProduct = lex
                        print("Cantidad : ", cantidadProduct)
                        estado= 5
                        lex = ''
                        self.CreacionProducto()
                        
                        
                    elif re.search(r"[ ]", entrada[indice]):
                        indice += 1
                        estado = 6

                    
                    else :
                        print ("regresa por ", entrada[indice])
                        estado = 5
                        indice +=1
        
            if estado == 0:
                break
    listaProductos = []
    
    #Metodo Creacion de Objetos Producto 
    def CreacionProducto(self):
        global PriceProduct
        global cantidadProduct
        global NameProduct
       
        PriceProduct = float(PriceProduct)
        if cantidadProduct == '':
            cantidadProduct = 0
        newProduct = producto(NameProduct, PriceProduct, cantidadProduct)
        self.listaProductos.append(newProduct)      
        
    
import re
class automata_instrucciones:
    def __init__(self):
        pass
    def automataInstrucciones(self,Instrucciones):
        lexema = ''
        estado = 1
        indice = 0
        NOMBRE = ''
        GRAFICA = ''
        TITULO = ''
        TITULOX = ''
        TITULOY = ''
        
        
        while indice  < len(Instrucciones):
            if estado == 1:
                if re.search(r"[<]", Instrucciones[indice]):
                    estado = 2
                    indice += 1
                    
                else:
                    estado = 1
                    indice += 1

            if estado == 2:
               
                if re.search(r"[¿]", Instrucciones[indice]):
                    estado = 3 
                    indice += 1
                elif re.search(r"[?]", Instrucciones[indice]):
                    estado = 1
                    indice += 1
                
            if estado == 3 :
                
                if re.search(r"[\n]", Instrucciones[indice]):
                    estado = 3
                    indice += 1
                elif re.search(r"[a-zA-Z]", Instrucciones[indice]):
                    lexema += Instrucciones[indice]
                    
                    estado = 3
                    indice += 1
                
                elif re.search(r"[\:]", Instrucciones[indice]):
                    
                    lexema = lexema.upper()
                    
                    estado = 5
                    indice += 1
                elif re.search(r"[\,]", Instrucciones[indice]):
                    
                    lexema =''
                    
                    estado = 3
                    indice += 1

                else :
                   
                    estado = 3
                    indice += 1
            #Verificacion de obligatorias 
            if estado == 4:
                if lexema == 'NOMBRE' :
                    
                    indice += 1
                    e = 0
                    lexema=''
                    while e == 0:
                        

                        if re.search(r"[\"]", Instrucciones[indice]):
                            indice += 1
                            
                        elif re.search(r"[a-zA-z]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[0-9]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[\,]", Instrucciones[indice]):
                            NOMBRE = lexema.upper()
                            print("Grafica : ", NOMBRE)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\?]", Instrucciones[indice]):
                            NOMBRE = lexema.upper()
                            print("NOMBRE : ", NOMBRE)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\n]", Instrucciones[indice]):
                            indice+=1
                            
                        elif re.search(r"[ ]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                    lexema=''
                    estado = 3
                elif lexema == 'GRAFICA':
                
                    indice += 1
                    e = 0
                    lexema=''
                    while e == 0:
                        

                        if re.search(r"[\"]", Instrucciones[indice]):
                            indice += 1
                            
                        elif re.search(r"[a-zA-z]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[0-9]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[\,]", Instrucciones[indice]):
                            GRAFICA = lexema.upper()
                            print("GRAFICA : ", GRAFICA)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\?]", Instrucciones[indice]):
                            GRAFICA = lexema.upper()
                            print("GRAFICA : ", GRAFICA)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\n]", Instrucciones[indice]):
                            indice+=1
                            
                        elif re.search(r"[ ]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                           
                    lexema=''
                    estado = 3
                   
                else :
                    print("Archivo no Contiene Datos Obligatorios y Necesarios")
                    estado = 3
            #Verificar  de Opcionales 
            if estado == 5:
                #Verificar se se encontro el un TiTULO
                if lexema == 'TITULO':
                   
                    
                    indice += 1
                    e = 0
                    lexema=''
                    while e == 0:
                        

                        if re.search(r"[\"]", Instrucciones[indice]):
                            indice += 1
                            
                        elif re.search(r"[a-zA-z]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[0-9]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[\,]", Instrucciones[indice]):
                            TITULO = lexema.upper()
                            print("TITULO : ", TITULO)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\?]", Instrucciones[indice]):
                            TITULO = lexema.upper()
                            print("TITULO : ", TITULO)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\n]", Instrucciones[indice]):
                            indice+=1
                            
                        elif re.search(r"[ ]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                            
                    lexema=''
                    estado = 3
                elif lexema == 'TITULOX':
                    
                    indice += 1
                    e = 0
                    lexema=''
                    while e == 0:
                        

                        if re.search(r"[\"]", Instrucciones[indice]):
                            indice += 1
                            
                        elif re.search(r"[a-zA-z]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[0-9]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[\,]", Instrucciones[indice]):
                            TITULOX = lexema.upper()
                            print("TITULOX : ", TITULOX)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\?]", Instrucciones[indice]):
                            TITULOX = lexema.upper()
                            print("TITULOX : ", TITULOX)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\n]", Instrucciones[indice]):
                            indice+=1
                            
                        elif re.search(r"[ ]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                    lexema=''
                    estado = 3
                elif lexema =='TITULOY':
                    
                    indice += 1
                    e = 0
                    lexema=''
                    while e == 0:
                        

                        if re.search(r"[\"]", Instrucciones[indice]):
                            indice += 1
                        
                            
                        elif re.search(r"[a-zA-z]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                            
                        elif re.search(r"[0-9]", Instrucciones[indice]):
                            lexema += Instrucciones[indice]
                            indice += 1
                        
                            
                        elif re.search(r"[\,]", Instrucciones[indice]):
                            TITULOY = lexema.upper()
                            print("Nombre : ", TITULOY)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\?]", Instrucciones[indice]):
                            TITULOY = lexema.upper()
                            print("Nombre : ", TITULOY)
                            indice += 1
                            
                            e = 1
                        elif re.search(r"[\n]", Instrucciones[indice]):
                            indice+=1
                        elif re.search(r"[ ]", Instrucciones[indice]):
                            indice += 1
                            lexema += Instrucciones[indice]
                    lexema=''
                    estado = 3

                else :
                    estado = 4
          
            

            if estado == 0:
                indice = len(Instrucciones)+1
                break

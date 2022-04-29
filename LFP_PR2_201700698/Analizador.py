import re
from Token import Token
from Token import Error
from ReporteToken import reportehtml
from ReporteErrores import reportehtmlERR
class Analizdor:

    def __init__(self):
        self.listTokens = []
        self.LIstaError = []
    
    #Lismpiar Listas
    def LimpiarLogTokens(self):
       self.listTokens = [] 
    def LimpiarErrores(self):
      self.LIstaError = []  
        
    def analizador(self, datos):
        #Lismpiar Listas
        self.c =[]
        linea = 1
        columna = 1
        lexema = ""
        estado = 0
        buffer = ''
        centinela = '$'
        datos += centinela
        index = 0
        equipo1 =''
        equipo2 = ''
        Temporada = ''
        nJornada = ''
        nombreArchvo = ''
        nComillas = 0
        GolesCondicion = ''
        equipoGoles =''
        nJornadaI = ''
        nJornadaF = ''
        equipo  = ''
        n = '5'
        while index < len(datos):
            c = datos[index]
            if estado == 0:
                if buffer == 'RESULTADO':
                    token = Token('RESULTADO', buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 1 
                elif buffer == "JORNADA":
                    token = Token('JORNADA', buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 3
                elif buffer == "TEMPORADA":
                    token = Token("TEMPORADA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 2
                elif buffer == "TABLA":
                    token = Token("TABLA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 0
                elif buffer == "GOLES":
                    token = Token("GOLES", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 6
                elif buffer == "PARTIDOS":
                    token = Token("PARTIDOS", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 7
                elif buffer == '-f':
                    token = Token("BANDERA NOMBRE ARCHIVO", buffer, linea, columna)
                    self.listTokens.append(token)
                    estado = 4
                    buffer = ''
                elif buffer == '-ji':
                    token = Token('JORNADA INICIAL', buffer, linea, columna)
                    self.listTokens.append(token)
                    estado = 8
                    buffer = ''
                elif buffer == '-jf':
                    token = Token('JORNADA FINAL', buffer, linea, columna)
                    self.listTokens.append(token)
                    estado = 9
                    buffer = ''
                elif buffer == '-n':
                    token = Token("TOP", buffer, linea, columna)
                    self.listTokens.append(token)
                    estado = 11
                    buffer = ''
                elif buffer == 'TOP':
                    token = Token("TOP", buffer, linea, columna)
                    self.listTokens.append(token)
                    estado = 10
                    buffer = ''
                elif buffer == 'ADIOS':
                    token = Token("ADIOS", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                elif re.search(r"[f]", c) or re.search(r"[-]", c) or re.search(r"[j]", c):
                    buffer += c
                    columna += 1 
                elif re.search(r"[j]", c) or re.search(r"[-]", c ) or re.search(r"[i]", c) :
                    buffer += c
                    columna += 1
                elif re.search(r"[n]", c):

                    buffer += c
                    columna += 1
                elif re.search(r"[\ ]", c):
                    columna+=1
                
                elif re.search(r"[A-Z]", c) :
                    buffer += c
                    columna += 1
                elif c == '$':
                    token = Token('EOF', c, linea, columna)
                    self.listTokens.append(token)
                else :
                    buffer += c
                    estado  = 5
            #Resultados 
            elif estado == 1 : 
                if  c == '“'or c == '”' or c =='"':
                    nComillas += 1
                    columna+=1
                    token = Token('COMILLA DOBLE','"' , linea, columna)
                    self.listTokens.append(token)
                    if nComillas == 2:
                        
                        equipo1 = buffer
                        token = Token("EQUIPO", buffer, linea, columna)
                        self.listTokens.append(token)
                        buffer==''
                    elif nComillas == 4:
                        
                        equipo2 = buffer
                        token = Token("EQUIPO", buffer, linea, columna)
                        self.listTokens.append(token)
                        buffer ==''
                        estado = 2
                    buffer = ''
                elif re.search(r"[A-Za-z]", c) or re.search(r"[\ ]", c) or c == 'ñ':
                    buffer += c
                    columna += 1 
                if buffer == ' VS' or buffer == 'VS':
                    columna += 1
                    token = Token("VS", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
            #Estado 2 : TEMPORADAS
            elif estado == 2 :
                if re.search(r"[0-9]", c):
                    buffer += c 
                    columna += 1
                elif re.search(r"[-]", c):
                    buffer += c
                    columna += 1
                    token = Token("GUION", c, linea, columna)
                    self.listTokens.append(token)
                elif re.search(r"[<]", c):
                    
                    columna += 1
                    token = Token("ABRE", c, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                elif re.search(r"[>]", c):
                    Temporada = buffer
                    token = Token("N.TEMPORADA", Temporada, linea, columna)
                    self.listTokens.append(token)
                    columna += 1
                    token = Token("CIERRA", c, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 0
            #Estado 3 : Numerojornada 
            elif estado == 3: 
                if re.search(r"[0-9]", c):
                    buffer += c
                    columna+=1
                elif re.search(r"[A-Z]", c):
                    
                    nJornada = buffer
                    token = Token('NUMERO DE JORNADA', buffer, linea, columna) 
                    self.listTokens.append(token)
                    buffer = ''
                    columna += 1
                    buffer += c
                    estado = 0
            #Estado 4 :  nombre Archovo
            elif estado == 4:
                if re.search(r"[a-zA-Z]", c) or re.search(r"[0-9]", c) or re.search(r"[_]", c):
                    buffer += c
                    columna += 1
                else:
                    nombreArchvo = buffer
                    buffer =''
                    token = Token("NOMBRE ARCHIVO", nombreArchvo, linea, columna)
                    self.listTokens.append(token)
                    estado = 0
            #Estado 6 ; Goles
            elif estado == 6 :
                if re.search(r"[A-Z]", c) :
                    buffer += c 
                    columna+=1
                elif buffer == 'LOCAL':
                    token = Token('CONDICION', buffer, linea, columna)
                    self.listTokens.append(token)
                    columna += 1
                    GolesCondicion =  buffer
                    buffer = ''
                    
                elif buffer == 'VISITANTE':
                    token = Token('CONDICION', buffer, linea, columna)
                    self.listTokens.append(token)
                    columna += 1
                    GolesCondicion =  buffer
                    buffer = ''
                    
                elif buffer == 'TOTAL':
                    token = Token('CONDICION', buffer, linea, columna)
                    self.listTokens.append(token)
                    columna += 1
                    GolesCondicion =  buffer
                    buffer = ''
                elif re.search(r"[a-z]", c) or c == " ":
                    buffer += c 
                    columna+=1
                elif   c == '“'or c == '”' or c =='"':
                    nComillas += 1
                    columna+=1
                    token = Token("COMILLA DOBLE",'"' , linea, columna)
                    self.listTokens.append(token)
                    if nComillas == 2:
                        
                        equipoGoles = buffer
                        token = Token("EQUIPO", buffer, linea, columna)
                        self.listTokens.append(token)
                        buffer  = ''
                        estado = 0


            # Estado 7 : Equipo
            elif estado == 7 : 
                
                if c == '“'or c == '”' or c =='"':
                    nComillas += 1
                    columna+=1
                    token = Token("COMILLA DOBLE",'"' , linea, columna)
                    self.listTokens.append(token)
                    if nComillas == 2:
                        equipo = buffer
                        token = Token("EQUIPO", buffer, linea, columna)
                        self.listTokens.append(token)
                        buffer  = ''
                        estado = 0
                elif re.search(r"[a-zA-Z]", c) or re.search(r"[\ ]", c) or re.search(r"[\ñ]", c) or c ==" ":
                    buffer += c 
                    columna+=1
                elif c =='ñ' :
                    buffer += c 
                    columna+=1
            
            #JORNADA INICIAL 
            elif estado == 8 :
                if re.search(r"[0-9]", c) or re.search(r"[\ ]", c):
                    buffer += c
                    columna+=1
                else :
                    nJornadaI = buffer
                    token = Token("NUMERO DE JORNADA", buffer, linea, columna) 
                    self.listTokens.append(token)
                    buffer = ''
                    columna += 1
                    buffer += c
                    estado = 0
            #JORNADA FINAL 
            elif estado == 9:
                if re.search(r"[0-9]", c) or re.search(r"[\ ]", c):
                    buffer += c
                    columna+=1
                else :
                    
                    nJornadaF = buffer
                    token = Token("NUMERO JORNADA", buffer, linea, columna) 
                    self.listTokens.append(token)
                    buffer = ''
                    columna += 1
                    buffer += c
                    estado = 0
            #estaod 10 : CONDICIONES
            elif estado == 10 :
                if re.search(r"[A-Z]", c):
                    columna += 1
                    buffer += c
                elif buffer == 'SUPERIOR':
                    token = Token("CONDICION", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 0
                elif buffer == 'INFERIOR':
                    token = Token("CONDICION", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ''
                    estado = 0
            #Estado  11 ; n 
            elif estado == 11:
                if re.search(r"[0-9]", c) or re.search(r"[\ ]", c):
                    buffer += c
                    columna+=1
                else :
                    
                    n = buffer
                    token = Token("NUMERO EQUIPOS", buffer, linea, columna) 
                    self.listTokens.append(token)
                    buffer = ''
                    columna += 1
                    buffer += c
                    estado = 0
            
                
            #Errores
            elif estado == 5 :
                error = Error("Error Lexico", buffer, linea, columna)
                self.LIstaError.append(error)
                print(buffer)
                buffer = ''
                estado = 0
                columna += 1
                index-=1
            index += 1 
        
        print("Lexico Exitoso ")
        return datos
        
                    
                


     #self.listTokens.append([linea, columna, "decimal", lexema])
    #Verfificar CAracter Alfabetico
    def imprimir(self):
        print("\n\n\n")
        print("listaTokens ")
        for token  in self.listTokens:
            
            token.mostrarToken()
        
    def imprimirErrores(self):
        print("\n\n\n")
        print("listaErrores  ")
        i = 0
        for error  in self.LIstaError:
            print(i+1)
            error.mostrarError()
            i += 1
    def RerporteErrores(self):
        reportehtmlERR("ErroresLexicos",self.LIstaError)
        
    def RerporteTokens(self):
        reportehtml(self.listTokens)
    
    def pag (self):
        Pagina(self.c, self.v)
    



    def Alfabetico(self, lex):
        if lex == 'a' or lex =='A':
            return lex
        elif lex ==  'b' or lex == 'C ':
            return lex
        elif lex == 'c ' or lex == 'C':
            return lex
        elif lex == 'd ' or lex == 'D':
            return lex
        elif lex == 'E ' or lex == 'e':
            return lex
        elif lex == 'f ' or lex == 'F':
            return lex
        elif lex == 'G' or lex == 'G':
            return lex
        elif lex == 'h ' or lex == 'H':
            return lex
        elif lex == 'i ' or lex == 'I':
            return lex
        elif lex == 'j ' or lex == 'J':
            return lex
        elif lex == 'k ' or lex == 'K':
            return lex
        elif lex == 'l ' or lex == 'L':
            return lex
        elif lex == 'm ' or lex == 'M':
            return lex
        elif lex == 'n ' or lex == 'N':
            return lex
        elif lex == 'ñ ' or lex == 'Ñ':
            return lex
        elif lex == 'o ' or lex == 'O':
            return lex
        elif lex == 'p ' or lex == 'P':
            return lex
        elif lex == 'q ' or lex == 'Q':
            return lex
        elif lex == 'r ' or lex == 'R':
            return lex
        elif lex == 's ' or lex == 'S':
            return lex
        elif lex == 't ' or lex == 'T':
            return lex
        elif lex == 'v ' or lex == 'V':
            return lex
        elif lex == 'w' or lex == 'W"':
            return lex
        elif lex == 'x ' or lex == 'Y':
            return lex
        elif lex == 'y ' or lex == 'Y':
            return lex
        elif lex == 'z ' or lex == 'Z':
            return lex
        else :
            return 'error'
    #Analizar Numeros 
    def Numeros(lex):
        if lex == '0':
            return lex
        elif lex == '1':
            return lex 
        elif lex == '2':
            return lex 
        elif lex == '3':
            return lex 
        elif lex == '4':
            return lex 
        elif lex == '5':
            return lex 
        elif lex == '6':
            return lex 
        elif lex == '7':
            return lex 
        elif lex == '8':
            return lex 
        elif lex == '9':
            return lex 
        else :
            return 'error'
    # Verificador Caracteres error 
    def signosError(self, lex):
        if lex  == '/':
            return lex
        elif lex == '\'':
            return lex
        elif lex == ';':
            return lex
        elif lex == '@':
            return lex
        elif lex == '.':
            return '@'
        else :
            return ''
    def espaciosYsaltos(self,lex):
        if lex == '\n':
            return 'salto'
        elif lex =='\t':
            return ''
        elif lex == ' ':
            return '' 
    def signos(self , lex):
        if lex == '<':
            return lex 
        elif lex =='>':
            return lex 
        elif lex == '[':
            return lex 
        elif lex == ']':
            return lex  
        elif lex == ',':
            return lex 
        elif lex == '[':
            return lex  
        elif lex == '~':
            return lex      
        elif lex == '"':
            return lex  
        elif lex == ':':
            return lex  
        elif lex == '':
            return lex  
    def verificaLexema(self, lexxe):
        if lexxe.lower() == "formulario~>>":
            return "reservada"
        else:
            return "identificador"
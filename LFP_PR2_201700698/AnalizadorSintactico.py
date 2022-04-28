from Token import Token
from Token import Error

class AnalizadorSintactico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = []
        self.Seasons = []
        self.i = 0

    def inicio(self):
        token = self.ListaTokens[self.i]
        print(token.tipo)
        #Analisis de las Funciones 
      

        if token.tipo == 'RESULTADO':
            return self.ResultadoPartido()
            self.i = 0
        elif token.tipo == 'JORNADA':
            r = self.ResultadoJornada()
            return r
            self.i = 0
        elif token.tipo == 'GOLES':
            return self.TotalGolesTemporada()
            self.i = 0
        elif token.tipo =='TABLA':
            return self.TablaGeneralTemporada()
            self.i = 0
        elif token.tipo == 'PARTIDOS':
            return self.TemporadaEquipo()
            self.i = 0
        elif token.tipo == 'TOP':
            return self.TopEquipos()
            self.i = 0

        
    #Token(tipo, lexema, linea, columna)
    def ResultadoPartido(self):
        equipo1= ''
        equipo2=''
        Temporada = ''

        self.i += 1
        token = self.ListaTokens[self.i]
        
        if token.tipo == 'COMILLA DOBLE':
            self.i += 1
            token = self.ListaTokens[self.i]
            if token.tipo == 'COMILLA DOBLE':
                self.i += 1
                token = self.ListaTokens[self.i]
                if token.tipo == 'EQUIPO':
                    equipo1 = token.lexema
                    self.i += 1
                    token = self.ListaTokens[self.i]
                    if token.tipo == 'VS':
                        self.i += 1 
                        token = self.ListaTokens[self.i]
                        if token.tipo == 'COMILLA DOBLE':
                            self.i += 1
                            token = self.ListaTokens[self.i]
                            if token.tipo == 'COMILLA DOBLE':
                                self.i += 1
                                token = self.ListaTokens[self.i]
                                if token.tipo == 'EQUIPO':
                                    print(token.lexema)
                                    equipo2 = token.lexema
                                    self.i += 1
                                    token = self.ListaTokens[self.i]
                                    if token.tipo == 'ABRE':
                                        self.i += 1
                                        token = self.ListaTokens[self.i]
                                        if token.tipo == 'GUION':
                                            self.i += 1
                                            token = self.ListaTokens[self.i]
                                            if token.tipo == 'N.TEMPORADA':
                                                Temporada = token.lexema
                                                self.i += 1
                                                token = self.ListaTokens[self.i]
                                                if token.tipo == 'CIERRA':
                                                    self.i += 1
                                                    token = self.ListaTokens[self.i]
                                                    if token.tipo == '$':
                                                        self += 1
                                                        token = self.ListaTokens[self.i]
                                                    else :
                                                        # $ >
                                                        pass
                                                else:
                                                    error = Error("Lexico", token.tipo, token.linea, token.columna)
                                                    self.ListaErrores.append(error)
                                            else :
                                                error = Error("Lexico", token.tipo, token.linea, token.columna)
                                                self.ListaErrores.append(error)
                                        else :
                                            error = Error("Lexico", token.tipo, token.linea, token.columna)
                                            self.ListaErrores.append(error)
                                    else : 
                                        error = Error("Lexico", token.tipo, token.linea, token.columna)
                                        self.ListaErrores.append(error)
                                else:
                                    error = Error("Lexico", token.tipo, token.linea, token.columna)
                                    self.ListaErrores.append(error)

                            else:
                                error = Error("Lexico", token.tipo, token.linea, token.columna)
                                self.ListaErrores.append(error)

                        else:
                            error = Error("Lexico", token.tipo, token.linea, token.columna)
                            self.ListaErrores.append(error)

                    else :
                        pass
                        error = Error("Lexico", token.tipo, token.linea, token.columna)
                        self.ListaErrores.append(error)
                       
                else :
                    error = Error("Lexico", token.tipo, token.linea, token.columna)
                    self.ListaErrores.append(error)
                    #Se Esperaba Equipo 

            else :
                error = Error("Lexico", token.tipo, token.linea, token.columna)
                self.ListaErrores.append(error)
                #se Esperaba "


            
        else:
            error = Error("Lexico", token.tipo, token.linea, token.columna)
            self.ListaErrores.append(error)
        print("----------")
        print(equipo1)
        print(equipo2)
        result =''
        for temporada in self.Seasons:
            if temporada.getSeasonYear()==Temporada:
                result = temporada.ResultadoUnPartido(equipo1,equipo2)

        return result

    def ResultadoJornada(self):
        self.i += 1
        token = self.ListaTokens[self.i]
        jornada = ''
        temporada = ''
        nombre = 'jornada'
        print("sasdf", token.tipo)

        if token.tipo == 'NUMERO DE JORNADA': 
            jornada = token.lexema
            self.i += 1
            token = self.ListaTokens[self.i]
            if token.tipo == 'TEMPORADA':
               
                self.i += 1 
                token = self.ListaTokens[self.i]
                if token.tipo == 'ABRE':
                    self.i += 1
                    token =  self.ListaTokens[self.i]
                    if token.tipo ==  'GUION':
                        self.i += 1 
                        token = self.ListaTokens[self.i]
                        if token.tipo == 'N.TEMPORADA':
                            temporada = token.lexema
                            self.i +=  1 
                            token =  self.ListaTokens[self.i]
                            if token.tipo =='CIERRA':
                                self.i += 1 
                                token = self.ListaTokens[self.i]
                                if token.tipo == 'BANDERA NOMBRE ARCHIVO':
                                    self.i += 1 
                                    token = self.ListaTokens[self.i]
                                    if token.tipo == 'NOMBRE ARCHIVO':
                                        nombre = token.lexema
                                    else:
                                        print("SE esperaba el Nombre del Archivo")
                                    
                                else:
                                    pass
                            else:
                                print("SE Espera Llave Cierre ")
                                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                self.ListaErrores.append(error)

                        else:
                            print("No ESta Bien la Temporada ")
                            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                            self.ListaErrores.append(error)
                            
                    else:
                        print("Se Espera un Guion")
                        error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                        self.ListaErrores.append(error)
                else:
                    print("Se Espera Signo de que Abre <")
                    error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                    self.ListaErrores.append(error)
                    
            else:
                print("Se espera IDENTIFICADOR TEMPORADA")
                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                self.ListaErrores.append(error)
        else:

            print("VA Numer de Jornada ")
            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
            self.ListaErrores.append(error)
            
        print("jornada: ", jornada)
        print("Temporada: ",temporada)
        respuesta = ''
        for t in self.Seasons:
            print(t.getSeasonYear())
            if t.getSeasonYear() == temporada:
                print("")
                respuesta = t.ResultadosDeJornada(jornada,nombre)

        return respuesta



    def TotalGolesTemporada(self):
        self.i += 1 
        token = self.ListaTokens[self.i]
        condicion = ''
        equipo = ''
        temporada = ''
        if token.tipo == 'CONDICION':
            condicion = token.lexema
            self.i += 1 
            token = self.ListaTokens[self.i]
            if token.tipo == 'COMILLA DOBLE':
                self.i += 1 
                token = self.ListaTokens[self.i]
                if token.tipo == 'COMILLA DOBLE':
                    self.i += 1 
                    token = self.ListaTokens[self.i]
                    if token.tipo == 'EQUIPO':
                        equipo = token.lexema
                        self.i += 1 
                        token = self.ListaTokens[self.i]
                        if token.tipo == 'TEMPORADA':
                            self.i += 1 
                            token = self.ListaTokens[self.i]
                            if token.tipo == 'ABRE':
                                self.i += 1 
                                token = self.ListaTokens[self.i] 
                                if token.tipo =='GUION':
                                    self.i += 1 
                                    token = self.ListaTokens[self.i]
                                    if token.tipo =='N.TEMPORADA':
                                        temporada = token.lexema
                                        self.i += 1 
                                        token = self.ListaTokens[self.i]
                                        if token.tipo == 'CIERRA':
                                            self.i += 1 
                                            token = self.ListaTokens[self.i]
                                        else :
                                            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                            self.ListaErrores.append(error)
                                            print("Cierra  ")
                                                
                                    else:
                                        error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                        self.ListaErrores.append(error)
                                        print("N Temporada ")
                                else:
                                    error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                    self.ListaErrores.append(error)
                                    print("Guion")
                                    
                            else :
                                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                self.ListaErrores.append(error)
                                print("Abre")  

                        else:
                            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                            self.ListaErrores.append(error)
                            print("Temporada ")
                    else:
                        error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                        self.ListaErrores.append(error)
                        print("Equipo ")
                        
                else:
                    error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                    self.ListaErrores.append(error)
                    print("Comillas dobles ")
            else:
                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                self.ListaErrores.append(error)
                print("Comillas dobles ")
            
        else:
            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
            self.ListaErrores.append(error)
            print("se esperaba condicion")
        
        for t in self.Seasons:
            if t.getSeasonYear() == temporada:
                print("")
                respuesta = t.GolesCondicion(equipo,condicion)
                return respuesta





    def TablaGeneralTemporada(self):
        self.i += 1
        token = self.ListaTokens[self.i]
        temporada = ''
        nombre = 'temporada'
        print(token.tipo,">>>>>>>><")
        if token.tipo == 'TEMPORADA':
            self.i += 1
            token = self.ListaTokens[self.i]
            if token.tipo =='ABRE':
                self.i += 1
                token = self.ListaTokens[self.i]
                if token.tipo == 'GUION':
                    self.i += 1
                    token = self.ListaTokens[self.i]
                    if token.tipo == 'N.TEMPORADA':
                        temporada =token.lexema
                        self.i += 1
                        token = self.ListaTokens[self.i]
                        if token.tipo == 'CIERRA':
                            self.i += 1
                            token = self.ListaTokens[self.i]
                            if token.tipo == 'BANDERA NOMBRE ARCHIVO':
                                        self.i += 1 
                                        token = self.ListaTokens[self.i]
                                        if token.tipo == 'NOMBRE ARCHIVO':
                                            nombre = token.lexema
                                        else:
                                            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                            self.ListaErrores.append(error)
                                            print("SE esperaba el Nombre del Archivo")
                                        
                            else:
                                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                self.ListaErrores.append(error)
                                pass
                        else: 
                            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                            self.ListaErrores.append(error)
                            print("Cierra ")
                    else:
                        error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                        self.ListaErrores.append(error)
                        print("Temporada ")


                else:
                    error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                    self.ListaErrores.append(error)
                    print("Guion")
            else:
                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                self.ListaErrores.append(error)
                print("abres")

        else:
            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
            self.ListaErrores.append(error)
            print("Temporada")
            

        for t in self.Seasons:
            if t.getSeasonYear() == temporada:
                print("")
                respuesta = t.TablaTemporada(nombre)
                return respuesta




    def TemporadaEquipo(self):
        self.i += 1
        token =self.ListaTokens[self.i]
        temporada = ''
        Jinicial = ''
        JFinal = ''
        nombre = 'partidos'
        equipo = ''
        if token.tipo == 'COMILLA DOBLE':
            self.i += 1 
            token = self.ListaTokens[self.i]
            if token.tipo == 'COMILLA DOBLE':
                self.i += 1 
                token = self.ListaTokens[self.i]
                if token.tipo == 'EQUIPO':
                    equipo = token.lexema
                    self.i += 1 
                    token = self.ListaTokens[self.i]
                    if token.tipo == 'TEMPORADA':
                        self.i += 1 
                        token = self.ListaTokens[self.i]
                        if token.tipo == 'ABRE':
                            self.i += 1 
                            token = self.ListaTokens[self.i]
                            if token.tipo == 'GUION':
                                self.i += 1 
                                token = self.ListaTokens[self.i]
                                if token.tipo == 'N.TEMPORADA':
                                    temporada = token.lexema
                                    self.i += 1 
                                    token = self.ListaTokens[self.i]
                                    if token.tipo == 'CIERRA':
                                        self.i += 1 
                                        token = self.ListaTokens[self.i]
                                        if token.tipo == 'JORNADA INICIAL':
                                            self.i += 1 
                                            token = self.ListaTokens[self.i]
                                            if token.tipo == 'NUMERO DE JORNADA':
                                                Jinicial = token.lexema
                                                try:
                                                    self.i += 1 
                                                    token = self.ListaTokens[self.i]
                                                except:
                                                    pass
                                            else: 
                                                print("Numero Jornada Inicial")
                                        if token.tipo == 'JORNADA FINAL':
                                            self.i += 1 
                                            token = self.ListaTokens[self.i]
                                            if token.tipo =='NUMERO JORNADA':
                                                JFinal = token.lexema
                                                try:
                                                    self.i += 1 
                                                    token = self.ListaTokens[self.i]
                                                except:
                                                    pass
                                            else:
                                                print("N Jornada Final")

                                        if token.tipo =='BANDERA NOMBRE ARCHIVO':
                                            self.i += 1 
                                            token = self.ListaTokens[self.i]
                                            if token.tipo =='NOMBRE ARCHIVO':
                                                nombre = token.lexema
                                                try:
                                                    self.i += 1 
                                                    token = self.ListaTokens[self.i]
                                                except:
                                                    pass
                                            else:
                                                print("Nombre Archivo")
                                                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                                self.ListaErrores.append(error)
                                    else:
                                        print("CIERRA")
                                        error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                        self.ListaErrores.append(error)

                                else:
                                    print("N Temporada")
                                    error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                    self.ListaErrores.append(error)
                            else: 
                                print("GUION")
                                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                                self.ListaErrores.append(error)  
                        else:
                            print("ABRE")
                            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                            self.ListaErrores.append(error)

                    else:
                        print("Temporada ")
                        error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                        self.ListaErrores.append(error)

                else:
                    print("Equipo")
                    error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                    self.ListaErrores.append(error)
            else:
                print("comilla doble ")
                error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
                self.ListaErrores.append(error)
        else:
            print("comilla doble ")
            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
            self.ListaErrores.append(error)
        print("-------------------")
        print(temporada)
        print(Jinicial)
        print(JFinal)
        print(nombre)
        print(equipo)
        if Jinicial =='' and JFinal=='':
            for t in self.Seasons:
                if t.getSeasonYear() == temporada:
                    respuesta = t.TemporadaCompletaDeEquipo(nombre,equipo)
                    return respuesta
        elif Jinicial == '' and JFinal != '':

            for t in self.Seasons:
                if t.getSeasonYear() == temporada:
                    respuesta = t.TemporadaConJFinal(JFinal,equipo,nombre)
                    return respuesta
            
        elif Jinicial != '' and JFinal == '':
            for t in self.Seasons:
                if t.getSeasonYear() == temporada:
                    respuesta = t.TemporadaConInicio(Jinicial,equipo,nombre)
                    return respuesta
        elif Jinicial != '' and JFinal != '':
            
            for t in self.Seasons:
                if t.getSeasonYear() == temporada:
                    respuesta = t.TemporadaIncioFin(Jinicial,JFinal,equipo,nombre)
                    return respuesta
            

    def TopEquipos (self):
        n = 5 
        temporada = ''
        condicion = ''
        self.i += 1
        token = self.ListaTokens[self.i]
        if token.tipo == 'CONDICION':
            condicion = token.lexema
            self.i += 1 
            token = self.ListaTokens[self.i]
            if token.tipo == 'TEMPORADA':
                self.i += 1 
                token = self.ListaTokens[self.i]
                if token.tipo =='ABRE':
                    self.i += 1 
                    token = self.ListaTokens[self.i]
                    if token.tipo == 'GUION':
                        self.i += 1 
                        token = self.ListaTokens[self.i]
                        if token.tipo == 'N.TEMPORADA':
                            temporada = token.lexema
                            self.i += 1 
                            token = self.ListaTokens[self.i]
                            if token.tipo == 'CIERRA':
                                try:
                                    self.i += 1 
                                    token = self.ListaTokens[self.i]
                                except:
                                    pass
                                if token.tipo =='TOP':
                                    self.i += 1 
                                    token = self.ListaTokens[self.i]
                                    if token.tipo == 'NUMERO EQUIPOS':
                                        n = token.lexema
                                else:
                                    pass

                            else:
                                print("Cierra")
                                    
                        else:
                            print("N Temporada ")

                    else:
                        print("Guion ")
                else:
                    print("Guion")
            else:
                print("TEmporada")
                

        else : 
            print("condicion")
            error = Error("SINTACTICO", token.lexema, token.linea, token.columna)
            self.ListaErrores.append(error)
        pass
    def Salida(self):
        pass

    
    def Analizar(self, listaTokens , listaErrores,Temporadas):
        self.ListaTokens  = listaTokens
        self.ListaErrores = listaErrores
        self.Seasons = Temporadas
        r = self.inicio()
        return r

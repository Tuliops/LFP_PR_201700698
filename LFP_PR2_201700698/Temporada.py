from Partido import Partido
import webbrowser
class Temporada:
    matches=[]
    def __init__(self, seasonYears, matches=[]):
        self.seasonYears = seasonYears
        self.matches = []

    def getSeasonYear(self):
        return self.seasonYears
        
    def InsertMatch(self,match):
        self.matches.append(match)
    def ShowMatches(self):

        
        for match in self.matches:
           print(match.getJornada())
    def equiposdeTemporada(self,temporada):
        pass

    #RESULTADO DE UN PARTIDO        
    def ResultadoUnPartido(self,equipo1,equipo2):
        
        for partido in self.matches:
            if partido.getLocal()== equipo1:
                if partido.getVisitante()==equipo2:
                    print("El resultado de este partido fue:"
                        ,equipo1," ", partido.getGolLocal," - ",
                        equipo2, " ", partido.golVisitante)
                    resultado = "El resultado de este partido fue: "+equipo1+" "+ partido.getGolLocal()+" - "+equipo2+ " "+ partido.golVisitante
                    print(resultado)
                    return resultado
        #El resultado de este partido fue: Real Madrid 2 - Villarreal 1

    def TemporadaCompletaDeEquipo(self,nombre,equipo):
        contenido = ''
   
        htmFile = open( nombre+ ".html", "w")

        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>REPORTE </title>
            <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
        <h2>\t : Resultados    </h2>
        <h2> Temporada : """+self.getSeasonYear()+"""</h2>
            
        <table class="table">
            <thead>
            <tr>
            
                <th>Jornada</th>
                <th>Local</th>
                <th>Goles Local </th>
                <th>Visitante</th>
                <th>Goles Visitante 
                
            </tr>
            </thead>

            """)
            #Resivira la los datos o la tabla con los Datos 
        for partido in self.matches:
            
            if partido.getLocal() == equipo or partido.getVisitante() == equipo:
                print(":",partido.getLocal()," ", partido.getGolLocal()," - ",
                        partido.getVisitante(), " ", partido.getGolVisitante())
                contenido += '<tr>'
                contenido += "<td>"+partido.getJornada() + "</td>\n"
                contenido += "<td>"+partido.getLocal()+"</td>\n"
                contenido += "<td>"+partido.getGolLocal()+ "</td>\n"
                contenido += "<td>"+partido.getVisitante()+"</td>\n"
                contenido += "<td>"+partido.getGolVisitante()+ "</td>\n"
                contenido += '</tr>'
        contenido  +=  "</tr>"
        htmFile.write(contenido)
        htmFile.write("""
            </table>
            </div>
                </body>
                </html>""")
        webbrowser.open(nombre+".html")
        htmFile.close
        return "Generando archivo de resultados de temporada"+ self.getSeasonYear() +" del "+equipo 

    def TemporadaConJFinal(self,Jfnal,equipo,nombre):
        contenido = ''
   
        htmFile = open( nombre+ ".html", "w")

        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>REPORTE </title>
            <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
        <h2>\t : Resultados    </h2>
        <h2> Temporada : """+self.getSeasonYear()+"""</h2>
            
        <table class="table">
            <thead>
            <tr>
            
                <th>Jornada</th>
                <th>Local</th>
                <th>Goles Local </th>
                <th>Visitante</th>
                <th>Goles Visitante 
                
            </tr>
            </thead>

            """)
            #Resivira la los datos o la tabla con los Datos
        for partido in self.matches:
            if int(partido.getJornada()) <= int(Jfnal) :
                if partido.getLocal() == equipo or partido.getVisitante() == equipo:
                    print(":",partido.getLocal()," ", partido.getGolLocal()," - ",
                            partido.getVisitante(), " ", partido.getGolVisitante())
                    contenido += '<tr>'
                    contenido += "<td>"+partido.getJornada() + "</td>\n"
                    contenido += "<td>"+partido.getLocal()+"</td>\n"
                    contenido += "<td>"+partido.getGolLocal()+ "</td>\n"
                    contenido += "<td>"+partido.getVisitante()+"</td>\n"
                    contenido += "<td>"+partido.getGolVisitante()+ "</td>\n"
                    contenido += '</tr>'

        contenido  +=  "</tr>"
        htmFile.write(contenido)
        htmFile.write("""
            </table>
            </div>
                </body>
                </html>""")
        webbrowser.open(nombre+".html")
        htmFile.close
        return "Generando archivo de resultados de temporada"+ self.getSeasonYear() +" del "+equipo


    def TemporadaConInicio(self,jInicio,equipo,nombre):
        contenido = ''
   
        htmFile = open( nombre+ ".html", "w")

        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>REPORTE </title>
            <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
        <h2>\t : Resultados    </h2>
        <h2> Temporada : """+self.getSeasonYear()+"""</h2>
            
        <table class="table">
            <thead>
            <tr>
            
                <th>Jornada</th>
                <th>Local</th>
                <th>Goles Local </th>
                <th>Visitante</th>
                <th>Goles Visitante 
                
            </tr>
            </thead>

            """)
            #Resivira la los datos o la tabla con los Datos 

        for partido in self.matches:
            if int(partido.getJornada()) >= int(jInicio) :
                if partido.getLocal() == equipo or partido.getVisitante() == equipo:
                    print(":",partido.getLocal()," ", partido.getGolLocal()," - ",
                            partido.getVisitante(), " ", partido.getGolVisitante())
                    contenido += '<tr>'
                    contenido += "<td>"+partido.getJornada() + "</td>\n"
                    contenido += "<td>"+partido.getLocal()+"</td>\n"
                    contenido += "<td>"+partido.getGolLocal()+ "</td>\n"
                    contenido += "<td>"+partido.getVisitante()+"</td>\n"
                    contenido += "<td>"+partido.getGolVisitante()+ "</td>\n"
                    contenido += '</tr>'
        contenido  +=  "</tr>"
        htmFile.write(contenido)
        htmFile.write("""
            </table>
            </div>
                </body>
                </html>""")
        webbrowser.open(nombre+".html")
        htmFile.close
        return "Generando archivo de resultados de temporada"+ self.getSeasonYear() +" del "+equipo 
        
    def TemporadaIncioFin(self,jInicio,JFinal,equipo,nombre):
        contenido = ''
   
        htmFile = open( nombre+ ".html", "w")

        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>REPORTE </title>
            <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
        <h2>\t : Resultados    </h2>
        <h2> Temporada : """+self.getSeasonYear()+"""</h2>
            
        <table class="table">
            <thead>
            <tr>
            
                <th>Jornada</th>
                <th>Local</th>
                <th>Goles Local </th>
                <th>Visitante</th>
                <th>Goles Visitante 
                
            </tr>
            </thead>

            """)
            #Resivira la los datos o la tabla con los Datos 

        for partido in self.matches:
            if int(partido.getJornada()) >= int(jInicio) and int(partido.getJornada()) <= int(JFinal) :
                if partido.getLocal() == equipo or partido.getVisitante() == equipo:
                    print(":",partido.getLocal()," ", partido.getGolLocal()," - ",
                            partido.getVisitante(), " ", partido.getGolVisitante())
                    contenido += '<tr>'
                    contenido += "<td>"+partido.getJornada() + "</td>\n"
                    contenido += "<td>"+partido.getLocal()+"</td>\n"
                    contenido += "<td>"+partido.getGolLocal()+ "</td>\n"
                    contenido += "<td>"+partido.getVisitante()+"</td>\n"
                    contenido += "<td>"+partido.getGolVisitante()+ "</td>\n"
                    contenido += '</tr>'
        contenido  +=  "</tr>"
        htmFile.write(contenido)
        htmFile.write("""
            </table>
            </div>
                </body>
                </html>""")
        webbrowser.open(nombre+".html")
        htmFile.close
        return "Generando archivo de resultados de temporada"+ self.getSeasonYear() +" del "+equipo


    def ResultadosDeJornada(self,nJornada,nombre):

        #Generando archivo de resultados jornada 12 temporada 2019-2020
        contenido = ''
   
        htmFile = open(nombre+".html", "w")

        htmFile.write("""<!DOCTYPE HTML PUBLIC"

        <html>

        <head>
            <title>REPORTE </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
        
        <h2> Temporada :"""+self.getSeasonYear()+""" </h2>
        <h2>  Jornada """+nJornada+""" </h2> 
        <table class="table">
            <thead>
            <tr>
        
            <th>Local</th>
            <th>Goles Local</th>
            <th>Visitante</th>
            <th>Goles Visita </th>
        </tr>
        </thead>

        """)
        for partido in self.matches:
            if partido.getJornada() == nJornada:
                
                contenido += '<tr>'
                contenido += "<td>"+partido.getLocal() + "</td>\n"
                contenido += "<td>"+partido.getGolLocal()+"</td>\n"
                contenido += "<td>"+partido.getVisitante()+"</td>\n"
                contenido += "<td>"+partido.getGolVisitante()+"</td>\n"
                contenido += '</tr>'
        contenido  +=  "</tr>"
        htmFile.write(contenido)
        htmFile.write("""
        </table>
        </div>
            </body>
            </html>""")
        webbrowser.open(nombre+".html")
        htmFile.close
        return "Generando archivo de resultados jornada "+nJornada+" temporada"+self.getSeasonYear()


    def GolesCondicion(self, equipo,condicion):
        nGoles = 0 
        if condicion =='LOCAL' :
            for partido in self.matches:
                if partido.getLocal()== equipo:
                    nGoles += int(partido.getGolLocal()) 
            
        elif condicion == 'VISITANTE'  :
            for partido in self.matches:
                if partido.getVisitante()== equipo:
                    nGoles +=  int(partido.getGolVisitante())  
        elif condicion == 'TOTAL':
            for partido in self.matches:
                if partido.getLocal()== equipo:
                    nGoles += int(partido.getGolLocal())
            for partido in self.matches:
                if partido.getVisitante()== equipo:
                    nGoles +=  int(partido.getGolVisitante())


        print("Goles : " ,nGoles)
        return "Los goles anotados por el "+  equipo+  " en " + condicion + " \n \t en la temporada " +self.getSeasonYear() +" fueron  "  +str(nGoles)
        

    def TablaTemporada(self,nombre):
        equipos = []

        for partido in self.matches:
                if  partido.getLocal() not in equipos:
                    equipos.append(partido.getLocal())
        n= 0
        Tabla = []
        for e in equipos:
            pts = 0
            for partido in self.matches:
                if partido.getLocal() == e:
                    if partido.getGolLocal()<partido.getGolVisitante():
                        pts += 0
                    elif partido.getGolLocal()>partido.getGolVisitante():
                        pts += 3
                    elif partido.getGolLocal()== partido.getGolVisitante():
                        pts += 1
            for partido in self.matches:
                if partido.getVisitante() == e:
                    if partido.getGolLocal()<partido.getGolVisitante():
                        pts += 3
                    elif partido.getGolLocal()>partido.getGolVisitante():
                        pts += 0
                    elif partido.getGolLocal()== partido.getGolVisitante():
                        pts += 1
            equipo={
                'Equipo' :  e,
                'Puntos' :  pts ,
            }
            
            Tabla.append(equipo)
        ordenPUntos = []
        for e in Tabla:
             ordenPUntos.append(e['Puntos'])
        
        Ordenado = self.bubbleSort(ordenPUntos)
        print(Ordenado)
        TablaOrdenada = []
        e= object()
        for puntos in reversed(Ordenado):
            for equipo in Tabla:
                if equipo['Puntos'] == puntos :
                    
                    e = {
                        'Equipo': equipo['Equipo'],
                        'Puntos': puntos
                    }
                    if e not in TablaOrdenada:
                        TablaOrdenada.append(e)
                    
        self.ReporteTabla(TablaOrdenada, nombre)
        return "Generando archivo de clasificación de temporada "+self.getSeasonYear()

    # Bubble sort in Python

    def bubbleSort(self,array):
        
        # loop to access each array element
        for i in range(len(array)):

            # loop to compare array elements
            for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
                if array[j] > array[j + 1]:

                    # swapping elements if elements
                    # are not in the intended order
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                
        return array
    
    def ReporteTabla(self,lista,nombre):
        contenido = ''
   
        htmFile = open( nombre+ ".html", "w")

        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>REPORTE </title>
            <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
        <h2>\t : Tabla de Posiciones  </h2>
        <h2> Temporada : """+self.getSeasonYear()+"""</h2>
            
        <table class="table">
            <thead>
            <tr>
            
                <th>Equipo</th>
                <th>Puntos</th>
                
            </tr>
            </thead>

            """)
            #Resivira la los datos o la tabla con los Datos 
        
        for t in lista:
                contenido += '<tr>'
                contenido += "<td>"+t['Equipo'] + "</td>\n"
                contenido += "<td>"+str(t['Puntos'])+"</td>\n"
                contenido += '</tr>'
            
            

                
            
        contenido  +=  "</tr>"
        htmFile.write(contenido)
        htmFile.write("""
            </table>
            </div>
                </body>
                </html>""")
        webbrowser.open(nombre+".html")
        htmFile.close
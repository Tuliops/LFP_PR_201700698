import webbrowser
def Pagina():

    contenido = ''
    
    htmFile = open( "Pagina"+ ".html", "w")

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
    <body style="background-color:#ECEFF1;">
    <div class="container" bgcolor ="skyblue">
  <h2>Nombre : TULIO JAFETH PIRIR SCHUMAN </h2>
  <h2> Carne : 20170068</h2>
      
    

    """)
  
    contenido += etiqueta("nombre")
    contenido += texto("nombre", "Ingrese su Nombre")
    v = ['Masculino','Femenido']
    contenido += grupo_radio("Sexo",v)

    vo = ['Guatemala','Mexico','Argentina']
    contenido += grupo_option("Pais", vo)

    htmFile.write(contenido)
    webbrowser.open("Pagina.html")
    htmFile.close

def etiqueta(nombre):
    contenido = ""
    contenido += "<p><h3>"+nombre+"</h3></p>"
    return contenido
def texto(nombre, fondo):
    contenido = ""
    contenido +=   '''<h3><input type="text" name="'''+nombre+'''
    " size="40" placeholder="'''+fondo+'''"></h3>'''
    return contenido
def grupo_radio(nombre,valores=[]):
    contenido =''
    contenido+='''<p><h3>'''+nombre+ '''  :  '''
    for v in valores:
        contenido += '''<input type ="radio"
         name="boton" value='''+v+''' required> '''+v+'''  '''
        
  
    contenido += '''</h3></p>''' 
   
    return contenido
def grupo_option(nombre, valores=[]):
    continido = '<p><h3>'''+nombre+''''''
    
    continido +=''' <select name="menu">
  <option selected>...</option>'''
    for v in valores:
        continido += '''<option value='''+v+'''>'''+v+'''</option>'''
    continido += '''</select></h3></p>'''
    
    return continido
  

from tkinter import ttk
from tkinter import filedialog
from tkinter import* 
from io import *
from Temporada import Temporada
from Partido import Partido
from Analizador import Analizdor
from AnalizadorSintactico import AnalizadorSintactico
import webbrowser
analizar = Analizdor()
sinta = AnalizadorSintactico()

class Interfaz:
    root = object()
    chat = object()
    btnCargar = object()
    txtChat = object()
    txtEnviar = object()
    btnEnviar = object()
    btnReporteTokens = object()
    btnLimpiarTokens = object()
    btnReporteErrores = object()
    btnLimpiarErrores = object()
    bntManuales =object()
    DicParidos = object()
    Temporadas = []
    def __init__(self):
        
        #ventana 
        global root 
        root = Tk()
        root.geometry('1000x1000')
        root.config(bg='gray45')
        root.title('La Liga Bot') 
        #Encabezado 
        head_label = Label(  text="Welcome", pady=10,bg="#17202A",fg="white")
        head_label.place(relwidth=1) 
        #botones 
        global btnCargar 
        btnCargar  = Button(text="Cargar CSV", command=self.CargaSCV)  
        btnCargar.place(x=845 , y=50 , height=50 ,width=150)
        
        btnCargar.config()
        #Boton Reporte Tokens 
        global  btnReporteTokens
        btnReporteTokens  = Button(text="Reporte Tokens ", command=self.ReporteTokens)  
        btnReporteTokens.place(x=845 , y=110 , height=50 ,width=150)
        
        btnReporteTokens.config()
        # Boton Limpiar Tokens 
        global  btnLimpiarTokens
        btnLimpiarTokens  = Button(text=" Limpiar Log  Tokens ", command=self.LimpiarLogTokens)  
        btnLimpiarTokens.place(x=845 , y=170 , height=50 ,width=150)
        
        btnLimpiarTokens.config()
        #Errores
        global btnReporteErrores
        btnReporteErrores  = Button(text=" Reporte Eroores  ", command=self.Errores)  
        btnReporteErrores.place(x=845 , y=230 , height=50 ,width=150)
        
        btnReporteErrores.config()
        global btnLimpiarErrores
        btnLimpiarErrores  = Button(text=" Limpiar Log Eroores  ", command=self.LogErrores)  
        btnLimpiarErrores.place(x=845 , y=290 , height=50 ,width=150)
        
        btnLimpiarErrores.config()
        #Manuales
        global bntManuales
        bntManuales  = Button(text=" MANUALES  ", command=self.Manuales)  
        bntManuales.place(x=845 , y=350 , height=50 ,width=150)
        
        bntManuales.config()
        

        global txtChat
        #Texto Chat 
        txtChat = Text(root, show=None, font=('Helvetica 14 ', 14))  # Mostrar como texto sin formato
        txtChat.config(bg="#17202A", fg="white")
        txtChat.place(x=10, y=75 ,height=400, width=800)
        # scroll bar
        scrollbar = Scrollbar(txtChat)
        scrollbar.place(relheight=1, relx=0.974)
        # bottom label
        bottom_label = Label(root, bg="#ABB2B9", height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        global txtEnviar
        # message entry box
        txtEnviar= Entry(bottom_label, bg="#2C3E50", fg="#EAECEE", font="Helvetica 14")
        txtEnviar.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        global btnEnviar
        # send button
        btnenviar = Button(bottom_label, text="Send", font="Helvetica 13 bold", width=20, bg="#ABB2B9",
                    command= self.Env)
        btnenviar.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        root.mainloop()
    def Errores(self):
        print("Errores")
        analizar.RerporteErrores()
    def LogErrores(self):
        print("Log Errores")
        analizar.LimpiarErrores()

    def Manuales(self):
        webbrowser.open('ManualUsuario.pdf')
        webbrowser.open('ManualTecnico.pdf')

    def Env(self):

        global txtEnviar
        Mensaje = txtEnviar.get()
        lex = analizar.analizador(Mensaje)
        r = sinta.Analizar(analizar.listTokens, analizar.LIstaError,self.Temporadas)
        global txtChat

        msj  = "(._.)-->"+Mensaje
       
        txtChat.insert( INSERT,msj+"\n\n ")

        Mensaje = txtChat.get("1.0","end-1c")
        bot = ">>{•̃_•̃}<<"
        #carabot <<{•̃_•̃}
       
        txtChat.insert( INSERT,bot+str(r)+"\n\n")
        
        Mensaje = txtChat.get("1.0","end-1c")
        
        Mensaje=""
        bot = ""
    
    def ReporteTokens(self):
        sinta.ReportarErrresSintactico()
    def LimpiarLogTokens(slef):
        analizar.LimpiarLogTokens()
        sinta.LimpiarErrores()

    def CargaSCV(self):
        print("Carga ")

        archivo =  filedialog.askopenfilename(initialdir = "/") 
            #Abre el achivo 
        archivo_texto = open(archivo ,'r',encoding="utf8")
            #Contenido del archivo leido 
        texto = archivo_texto.read()
        archivo_texto.close()

        #por Partidos 
        partidos = texto.split('\n')        

        DicParidos = []

        for partido in partidos:
            dato = partido.split(',')
            
            p={
                'Fecha' :  dato[0],
                'Temporada' :  dato[1],
                'Jornada' :  dato[2],
                'Local' :  dato[3],
                'Visitante' :  dato[4],
                'GolesLocal' :  dato[5],
                'GolesVisitante' :  dato[6]
            }
            DicParidos.append(p)
        DicParidos.pop(0)
        newSeason = object()
        lasTemporadas=[]
        for t in DicParidos:
            if t['Temporada'] not in lasTemporadas:
                lasTemporadas.append(t['Temporada'])
                newSeason = Temporada(t['Temporada'])
                self.Temporadas.append(newSeason)
        for tem in self.Temporadas:
            print(tem.getSeasonYear())
            for partido in DicParidos:
                if partido['Temporada'] == tem.getSeasonYear():
                    newMatch = Partido(partido['Fecha'],
                                         partido['Local'],
                                         partido['Visitante'],
                                          partido['GolesLocal'],
                                           partido['GolesVisitante'],
                                           partido['Jornada'])
                    tem.InsertMatch(newMatch)
        global txtChat

        msj  = "--CARGA EXITOSA---  "
       
        txtChat.insert( INSERT,msj+"\n\n ")
             

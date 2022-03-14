
from pagina import Pagina
from interfaz import interfaz
from Token import Token
from Analizador import Analizdor
def leer(ruta):
    file = open(ruta ,  'r')
    contenido = file.read()
    return contenido
if __name__ == "__main__":
    entrada = leer('ejemploP1.form')
    lex = Analizdor()
    lex.analizador(entrada)
    lex.imprimir()
    lex.imprimirErrores()
class Partido:
    def __init__(self,date,local,visitante,golLocal,golVisitante,jornada):
        self.date = date
        self.local = local
        self.visitante = visitante
        self.golLocal = golLocal
        self.golVisitante = golVisitante
        self.jornada = jornada
    
    def getDate(self):
        return self.date
    def getLocal(self):
        return self.local
    def getVisitante(self):
        return self.visitante
    def getGolLocal(self):
        return self.golLocal
    def getGolVisitante(self):
        return self.golVisitante
    def getJornada(self):
        return self.jornada
        
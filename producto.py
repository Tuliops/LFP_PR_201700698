class producto :
    
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    #METODOS SET
    
    def setNombre(self,nombre):
        self.nombre = nombre
    def setPrecio(self,precio):
        self.precio = precio
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    #METODOS GET    

    def getNombre(self):
        return self.nombre
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cantidad
        
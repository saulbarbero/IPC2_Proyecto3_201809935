from edd.lista import lista

class Empresa:
    def __init__(self, nombre = ""):
        self.nombre = nombre.lower()
        self.bueno = 0
        self.malo = 0
        self.neutral = 0
        
        self.servicios = lista()

    def __str__(self):
        self.servicios.printLista()
        return self.nombre




class Servicio:
    def __init__(self, nombre):
        self.nombre = nombre.lower()
        self.alias = lista()
        self.bueno = 0
        self.malo = 0
        self.neutral = 0

    def __str__(self):
        # salida  = self.nombre
        # salida  += "\n"
        self.alias.printLista()
        return self.nombre

class Mensaje:
    def __init__(self, fecha, contenido):
        self.fecha = fecha
        self.content = contenido


    def __str__(self) -> str:
        return self.fecha  + "\n" + self.content 
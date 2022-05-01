from edd.lista import lista



class Mensaje:
    def __init__(self, fecha, contenido):
        self.fecha = fecha
        self.content = contenido
        self.lWords = lista()
        self.contentToList()



    def contentToList(self):
        aux = ""
        for i in range(len(self.content)):
            if ord(self.content[i]) >= 0 and ord(self.content[i]) <= 46:
                if ord(self.content[i]) == 32 and aux != "":
                    self.lWords.insertar(aux)
                    aux = ""
                continue
            else:
                aux += self.content[i]

        self.lWords.insertar(aux)

    def __str__(self) -> str:
        return self.fecha  + "\n" + self.content 
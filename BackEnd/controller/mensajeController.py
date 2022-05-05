from regex import P
from edd.lista import Nodo
from model.empresa import Empresa
from edd.lista import lista
from controller.Recurso import Recurso

positivos = lista()
negativos = lista()
mensajes = lista()
empresas = lista()


class MensajeController:
    def __init__(self, text) -> None:
        self.test = ''
        self.nodoEmpresa = None
        self.nodoServicio = None
        self.positivos = 0
        self.negativos = 0
        self.input = text

        self.setData(self.input)



    def setData(self, text):
        recurso = Recurso(positivos, negativos, mensajes, empresas)
        recurso.obtenerDataText(text)

    def analizarEntrada(self)->str:
        

        pivote = mensajes.primero
        flagError = False
        while pivote:
            self.positivos = 0
            self.negativos = 0
            mensaje = pivote.dato.content

            self.encontrarPalabras(mensaje, 0)
            self.encontrarPalabras(mensaje, 1)
            self.encontrarPalabras(mensaje, 2)


            if self.nodoServicio == None and self.nodoEmpresa == None:
                print(' error inesperado ')
                flagError = True
                break
            

            if self.nodoServicio == None:
                #el mensaje habla sobre la empresa directamente
                empresa = self.nodoEmpresa.dato
                empresa.bueno += self.positivos
                empresa.malo += self.negativos

                self.nodoEmpresa.dato = empresa
            else:
                # el mensaje habla sobre el servicio
                servicio = self.nodoServicio.dato
                servicio.bueno += self.positivos
                servicio.malo += self.negativos
                self.nodoServicio.dato = servicio

            
            pivote = pivote.siguiente



        if flagError:
            return "Error"
        else:
            printTo = self.resultToJson()

            print(printTo)
            return printTo



    def resultToJson(self)->str:
        buffer = "[\n"

        pivoteEmpresa = empresas.primero

        while pivoteEmpresa: 

            buffer += "{\n"
            buffer += f'"nombre": "{pivoteEmpresa.dato.nombre}",\n'
            buffer += f'"positivos": {pivoteEmpresa.dato.bueno},\n'
            buffer += f'"negativos": {pivoteEmpresa.dato.malo},\n'
            buffer += f'"servicios": [\n'

            pivoteServicio = pivoteEmpresa.dato.servicios.primero
            while pivoteServicio:
                buffer += "{\n"
                buffer += f'"nombre": "{pivoteServicio.dato.nombre}",\n'
                buffer += f'"positivos": {pivoteServicio.dato.bueno},\n'
                buffer += f'"negativos": {pivoteServicio.dato.malo}\n'

                buffer += "\n}" #coma

                if pivoteServicio.siguiente != None:
                    buffer += ",\n"

                pivoteServicio = pivoteServicio.siguiente

            buffer += "\n]"

            buffer += "\n}" #coma
            if pivoteEmpresa.siguiente != None:
                buffer += ",\n"


            pivoteEmpresa = pivoteEmpresa.siguiente


        buffer += "]"

        return buffer


    def encontrarPalabras(self, input:str, type:int)->None:
        state = 0
        lexema = ""
        input = input.lower()
        for c in input:

            if state == 0:
                lexema = ""
                if self.isLetter(c):
                    state = 1
                    lexema += c
                else:
                    continue

            elif state == 1:
                if self.isLetter(c):
                    state = 1
                    lexema += c
                else:
                    state = 0
                    self.reconocerPalabra(lexema, type)

                    #validar aqui la palabra reconocida.

            
            



    def reconocerPalabra(self, palabra:str, type:int)->None:

        if type == 0:
            temp = self.encontrarEmpresa(palabra)
            if temp != None:
                self.nodoEmpresa = temp
        elif type == 1:
            temp = self.encontrarServicio(palabra, self.nodoEmpresa.dato)
            if temp != None:
                self.nodoServicio = temp
        else:
            print('') # bueno o malo se pueden capturar juntos

            if self.encontrarSentimiento(palabra, positivos):
                self.positivos += 1

            elif self.encontrarSentimiento(palabra, negativos):
                self.negativos += 1






    def isLetter(self, input)->bool:
        ascii = ord(input)
        if (ascii >= 64 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            return True

        return False


    def encontrarServicio(self, name:str, empresa:Empresa)->None:
        
        if empresa == None:
            return

        pivote = empresa.servicios.primero

        while pivote:

            servicio = pivote.dato
            if servicio.nombre == name:
                return pivote


            alias = servicio.alias.primero

            while alias:
                
                if alias.dato == name:
                    return pivote

                alias = alias.siguiente

            pivote = pivote.siguiente

        return None


    def encontrarEmpresa(self, name:str)->Nodo:
        
        pivote = empresas.primero 
        while pivote:
            
            empresa:Empresa = pivote.dato
            if empresa.nombre.lower() == name:
                return pivote

            pivote = pivote.siguiente

        return None


    def encontrarSentimiento(self, palabra:str, list:lista):
        pivote = list.primero


        while pivote:

            if pivote.dato == palabra:
                return True

            pivote = pivote.siguiente

        return False
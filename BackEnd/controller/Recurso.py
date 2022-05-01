from edd.lista import lista
from model.mensaje import Mensaje
from model.empresa import Empresa, Servicio


import xml.etree.ElementTree as ET


class Recurso:
    def __init__(self, positivos:lista, negativos:lista, mensajes:lista, empresas:lista):
        self.lpositivos = positivos
        self.lnegativos = negativos
        self.lmensajes = mensajes
        self.lempresa = empresas

    def obtenerDataFile(self, file)->None:
        tree = ET.parse(file)
        root = tree.getroot()

        self.__obtenerData(root)

    def obtenerDataText(self, text)->None:
        root = ET.fromstring(text)

        self.__obtenerData(root)


    def __obtenerData(self, root):
        # tree = ET.fromstring(text)

        for element in root:
            if element.tag == 'diccionario':
                for c in element:
                    if c.tag == 'sentimientos_positivos':
                        self.capturarSentimientosPositivos(c)
                    elif c.tag == 'sentimientos_negativos':
                        self.capturarSentimientosNegativos(c)
                    else:
                        self.capturarEmpresa(c)

            else:
                for r in element:
                    # mensajes
                    self.capturarMensaje(r)
                    print('')
                    


    
    def capturarSentimientosPositivos(self, root):
        for palabra in root:
            temporal = palabra.text
            temporal = temporal.strip()
            self.lpositivos.insertar(temporal)
    
    def capturarSentimientosNegativos(self, root):
        for palabra in root:
            temporal = palabra.text
            temporal = temporal.strip()
            self.lnegativos.insertar(temporal)

    def capturarEmpresa(self, root):
        empresa = Empresa()
        for e in root:
            for c in e:
                if c.tag == "nombre":
                    temp = str(c.text.replace(' ', ""))
                    temp = self.removerAcentos(temp)
                    empresa.nombre = temp.lower()
                elif c.tag == "servicio":
                    temp = str(c.attrib["nombre"].replace(" ", ""))
                    temp = self.removerAcentos(temp)

                    servicio = Servicio(temp.lower())
                    for alias in c:
                        temp = str(alias.text.replace(" ", ""))
                        temp = self.removerAcentos(temp)
                        
                        servicio.alias.insertar(temp.lower())

                    empresa.servicios.insertar(servicio)

            #guardarla en una lista
            self.lempresa.insertar(empresa)
                
        

        print('')


    def capturarMensaje(self, root):
        temp = root.text.split('\n')


        for element in temp:
            if element == "":
                temp.remove(element)


        lugarFecha = temp[0].split(':', 1)
        fecha = lugarFecha[1].split(',')[1] # datetime
        msg = temp[3]
        msg = self.removerAcentos(msg)
        self.lmensajes.insertar(Mensaje(fecha, msg))



    def removerAcentos(self, texto):
        salida = ""
        for c in texto:
            salida += self.sinAcento(c)

        return salida



    def sinAcento(self, letra):
        if letra == "á":
            return "a"
        elif letra == "é":
            return "e"
        elif letra == "í":
            return "i"
        elif letra == "ó":
            return "o"
        elif letra == "ú":
            return "u"
        else:
            return letra



from lista import lista
from mensaje import Mensaje
from empresa import Empresa, Servicio


import xml.etree.ElementTree as ET


class Recurso:
    def __init__(self, positivos:lista, negativos:lista, mensajes:lista, empresas:lista):
        self.lpositivos = positivos
        self.lnegativos = negativos
        self.lmensajes = mensajes
        self.lempresa = empresas


    def obtenerData(self, text):
        # tree = ET.fromstring(text)
        tree = ET.parse(text)
        root = tree.getroot()

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
            self.lpositivos.insertar(palabra.text)
    
    def capturarSentimientosNegativos(self, root):
        for palabra in root:
            self.lnegativos.insertar(palabra.text)

    def capturarEmpresa(self, root):
        empresa = Empresa()
        for e in root:
            for c in e:
                if c.tag == "nombre":
                    empresa.nombre = c.text.replace(' ', "")
                elif c.tag == "servicio":
                    servicio = Servicio(c.attrib["nombre"].replace(" ", ""))
                    for alias in c:
                        servicio.alias.insertar(alias.text.replace(" ", ""))

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
        self.lmensajes.insertar(Mensaje(fecha, msg))




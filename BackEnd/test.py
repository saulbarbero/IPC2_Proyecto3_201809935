from Recurso import Recurso
from lista import lista


positivos = lista()
negativos = lista()
mensajes = lista()
empresas = lista()

def llenarData():
    recurso = Recurso(positivos, negativos, mensajes, empresas)
    recurso.obtenerData('entrada.xml')
    positivos.printLista()
    negativos.printLista()
    mensajes.printLista()
    empresas.printLista()
    print('')


if __name__ == "__main__":
    llenarData()
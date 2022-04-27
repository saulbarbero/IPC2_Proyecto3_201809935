from Recurso import Recurso
from lista import lista


positivos = lista()
negativos = lista()
mensajes = lista()
empresas = lista()

def llenarData():
    recurso = Recurso(positivos, negativos, mensajes, empresas)
    recurso.obtenerData('entrada.xml')

    testMensaje = mensajes.primero.dato
    testMensaje.contentToList()

    print('')


if __name__ == "__main__":
    llenarData()
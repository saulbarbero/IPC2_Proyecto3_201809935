from lista import lista
from Recurso import Recurso



positivos = lista()
negativos = lista()

def setData(text):

    recurso = Recurso(positivos, negativos, None, None)
    recurso.obtenerData(text)
    print('')

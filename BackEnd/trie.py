from lista import lista
from Recurso import Recurso



positivos = lista()
negativos = lista()
mensajes = lista()
empresas = lista()

out = lista()
fail = lista()


max_states = 0
max_characters = 27
miTrie = lista()

class AhoCorasick:
    def __init__(self, txt, diccionario:lista):
        self.mensaje = txt
        self.diccionario = diccionario

        self.max_characters = 27
        self.max_states = self.calculateStates(self.diccionario)
        self.out = self.initList(self.max_states + 1, 0)
        self.fail = self.initList(self.max_states + 1, -1)

        self.goto = lista()


        self.generateTrie(self.max_states + 1, self.max_characters)
        self.diccionarioToLower()





    def __build_matching_machine(self):
        k = self.diccionario.tam

        states = 1


        pivote = self.diccionario.primero
        i = 0
        while pivote:

            word = str(pivote.dato)
            current_state = 0

            for character in word:
                if ord(character) == 32:
                    continue
                ch = ord(character) - 97

                
                if self.buscarTrie(current_state, ch) == -1:
                    self.setTrieDato(current_state, ch, states)
                    states += 1

                current_state = self.buscarTrie(current_state, ch)

            
            pOut = self.buscarPorPosicion(current_state, self.out)
            pOut.dato |= (1 << i)

            i += 1
            pivote = pivote.siguiente


        for ch in range(self.max_characters):
            if self.buscarTrie(0, ch) == -1:
                self.setTrieDato(0, ch, 0)

        
        cola = lista()

        for ch in range(self.max_states):
            if self.buscarTrie(0, ch) != 0:
                self.setByPosicion(self.fail, 0, int(self.buscarTrie(0, ch)))
                cola.insertar(self.buscarTrie(0, ch))


        pivoteQueue = cola.primero
        while pivoteQueue:

            state = cola.dequeue()

            for ch in range(self.max_characters):
                if self.buscarTrie(state, ch) != -1:
                    temp = self.buscarPorPosicion(state, self.fail)
                    failure = int(temp.dato)


                    while self.buscarTrie(failure, ch) == -1:
                        temp = self.buscarPorPosicion(failure, self.fail)
                        failure = int(temp.dato)

                    failure = self.buscarTrie(failure, ch)
                    self.setByPosicion(self.fail, failure, self.buscarTrie(state, ch))

                    temp1 = self.buscarPorPosicion(failure, self.out)
                    temp2 = self.buscarPorPosicion(self.buscarTrie(state, ch), self.out)

                    temp2.dato |= int(temp1.dato)

                    self.setByPosicion(self.out, temp2.dato, self.buscarTrie(state, ch))
                    cola.insertar(self.buscarTrie(state, ch))

            pivoteQueue = pivoteQueue.siguiente

        return states
            

    def __find_next_state(self, current_state, next_input):
        print('no sirve jeje')


    def setByPosicion(self, list:lista, dato, count):
        pivote = list.primero

        while pivote and count > 0:
            count -= 1
            pivote = pivote.siguiente

        pivote.dato = dato

    def diccionarioToLower(self):
        pivote = self.diccionario.primero

        while pivote:
            
            dato = str(pivote.dato)
            pivote.dato = dato.lower()


            pivote = pivote.siguiente


    def calculateStates(self, list:lista):
        pivote = list.primero
        max_states = 0
        while pivote != None:
            max_states += int(pivote.dato)
            pivote = pivote.siguiente

        return max_states

    def initList(self, max, value):
        list = lista()
        for i in range(max):
            list.insertar(value)

        return list


    def generateTrie(self, filas, columnas):
        for i in range(filas):
            t = trie(-1)
            for j in range(columnas):
                t.interno.insertar(-1)

            
            self.goto.insetar(t)



    def buscarTrie(self, xCount, yCount):
        pivote = self.goto.primero

        while(pivote and xCount > 0):
            xCount -= 1
            pivote = pivote.siguiente

        # pivote esta en la posicion de xCount
        pinterno = pivote.dato.interno.primero
        while(pinterno and yCount > 0):
            yCount -= 1
            pinterno = pinterno.siguiente


        return int(pinterno.dato)

    def setTrieDato(self, xCount, yCount, dato):
        pivote = self.goto.primero

        while(pivote and xCount > 0):
            xCount -= 1
            pivote = pivote.siguiente

        # pivote esta en la posicion de xCount
        pinterno = pivote.dato.interno.primero
        while(pinterno and yCount > 0):
            yCount -= 1
            pinterno = pinterno.siguiente


        pinterno.dato = int(dato) # probar

    def buscarPorPosicion(self, posicion, l:lista):
        pivote = l.primero

        while(pivote and posicion > 0):
            posicion -= 1
            pivote = pivote.siguiente

        return pivote


class trie:
    def __init__(self, dato = 0):
        self.dato = dato
        self.interno = lista()





    
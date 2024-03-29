class Nodo:
    __dato = None
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
class listaEncadenada:
    __cabeza = None
    __cantidad: int
    
    def __init__ (self):
        self.__cabeza 
        self.__cantidad = 0
    
    def vacio(self):
        return self.__cabeza == None

    def anterior(self, dato):
        pos = self.buscar(dato)
        if pos == -1 or pos == self.__cabeza:
            print('No existe el dato o es el primer elemento')
        else:
            return pos.getDato()
        
    def siguiente(self, dato):
        pos = self.buscar(dato)
        if pos == -1 or pos == self.__cantidad:
            print('No existe el dato o es el ultimo elemento')
        else:
            return pos.getSiguiente().getDato() #type: ignore
    
    def buscar(self, dato):
        aux = self.__cabeza
        
        while aux != None and aux.getDato() != dato:
            aux = aux.getSiguiente()
        
        if aux == None:
            return -1
        else:
            return aux

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.vacio() or dato < self.__cabeza.getDato(): #type: ignore
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            anterior = None
            
            while aux is not None and dato > aux.getDato():
                anterior = aux
                aux = aux.getSiguiente()

            nuevo.setSiguiente(aux)
            anterior.setSiguiente(nuevo) #type: ignore
    
    def eliminar(self, dato):
        aux = self.__cabeza
        anterior = None

        while aux != None and aux.getDato() != dato:
            anterior = aux
            aux = aux.getSiguiente()
        
        if aux == None:
            print("El dato no existe")
        elif anterior == None:
            self.__cabeza = aux.getSiguiente() #
        else:
            anterior.setSiguiente(aux.getSiguiente())

    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

if __name__ == '__main__':
    lista = listaEncadenada()
    lista.insertar(3)
    lista.insertar(2)
    lista.insertar(1)

    lista.mostrar()
    print("------------------------------------------------------------------\n\n")
    print("El Anterior al elemento [{}] es: {}".format(2, lista.anterior(2)))
    print("El Siguiente al elemento [{}] es: {}".format(2, lista.siguiente(2)))
    print("------------------------------------------------------------------\n\n")
    lista.eliminar(2)
    lista.mostrar()
   
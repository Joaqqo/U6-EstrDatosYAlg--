from Nodo import Nodo
class Cola:
    __cant= 0
    __pri= None
    __ult= None


    def __init__(self, xcant=0):
        self.__pri= None
        self.__ult= None
        self.__cant= xcant

    def Vacia(self):
        return self.__cant == 0

    def Insertar(self, dato):
        nodo = Nodo(dato)
        if self.__ult == None:
            self.__pri= nodo
        else:
            self.__ult.setSiguiente(nodo)
        self.__ult= nodo
        self.__cant += 1


    def Suprimir(self):
        dato= None
        if not self.Vacia():
            aux= self.__pri
            dato= self.__pri.getDato()
            self.__pri= self.__pri.getSiguiente()
            self.__cant -= 1
            if self.__pri == None:
                self.__ult= None
            del aux
        return dato

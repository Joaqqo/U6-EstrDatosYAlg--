import numpy as np
from Cola import Cola
from ListaE import ListaE

class GrafoEnlazado:
    def __init__(self, cantn, pond=False):
        self.__cantn=cantn
        self.__ponderado=pond
        self.__adyacencias= np.full(self.__cantn, None)
        self.__nodos= np.full(self.__cantn, None)
        for i in range(self.__cantn):

            self.__adyacencias[i]= ListaE()

    def CargarNodo(self, nodo):
        if self.Indice(nodo):
            self.__nodos[nodo]=nodo
        else:
            print("Error con el nodo ingresado.")

    def Aristas(self, nodoa, nodo, peso=1):
        if self.Indice(nodoa,nodo):
            relacion= {"nodos":nodo,"peso":peso} #Le doy un "nombre" a cada cosa, así es más fácil después para sacarlos de la lista
            posicion= self.__adyacencias[nodoa].Longitud()
            self.__adyacencias[nodoa].Insertar(relacion, posicion)

            relacion= {"nodos":nodoa,"peso":peso} #Le doy un "nombre" a cada cosa, así es más fácil después para sacarlos de la lista
            posicion= self.__adyacencias[nodo].Longitud()
            self.__adyacencias[nodo].Insertar(relacion, posicion)
        else:
            print("Error con el nodo ingresado.")



    def Adyacente(self, nodo):
        adyacentes=[]
        if self.Indice(nodo):
            for i in range(self.__adyacencias[nodo].Longitud()):
                adyacentes.append(self.__adyacencias[nodo].Recuperar(i)["nodos"])
        else:
            print("Error con el Nodo ingresado.")
        return adyacentes

    def Indice(self, i, j=0):
        valid=True
        if i<0 or j<0 or i >= self.__cantn or j >= self.__cantn:
            valid= False
        return valid




    def Grado(self, nodo):
        adya= self.Adyacente(nodo)
        grado=len(adya)
        return grado

    def Camino(self, nodoi, nodod):
        camino=[]
        if self.Indice(nodoi, nodod):
            datos= self.BuscarREA(nodoi)
            camino= self.auxCamino(nodod, datos[1])
        else:
            print("Error con los nodos ingresados")
        return camino

    def auxCamino(self, nodod, anteriores):
        camino=[]
        while nodod != None: #Como se hizo un np.array lleno de Nones, se usa este
            camino.append(nodod)
            nodod= anteriores[nodod]

        camino.reverse() #Para que se vea desde nodo inicial al destino
        return camino

    def Conexo(self):
        i=0
        conexo=True
        while i < self.__cantn and conexo:
            dato= self.BuscarREA(i)
            if False in dato[0]:
                conexo=False
            i+=1
        return conexo

    def Aciclico(self):
        i=0
        aciclico=True
        while i < self.__cantn and aciclico:
            dato= self.BuscarREA(i)
            if dato[3]:
                aciclico=False
            i+=1
        return aciclico


    def BuscarREA(self, nodoi):
        vistos=np.full(self.__cantn, False)
        anteriores=np.full(self.__cantn, None)
        recorrido=[]
        cola=Cola()

        ciclo=False
        vistos[nodoi]=True
        cola.Insertar(nodoi)

        while not cola.Vacia():
            nv= cola.Suprimir()
            recorrido.append(nv)
            nu= self.Adyacente(nv)
            for u in nu:
                adyAu=self.Adyacente(u)
                if nv in adyAu and not ciclo:
                    ciclo=True
                if vistos[u] == False:
                    vistos[u]= True
                    anteriores[u]= nv
                    cola.Insertar(u)
        return vistos, anteriores, recorrido, ciclo


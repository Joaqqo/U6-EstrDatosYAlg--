import numpy as np
from Cola import Cola
class GrafoSecuencial:
    __cantn=0 #Cantidad nodos
    __ponderado=None #Si es ponderado o no
    __componentes=0 #Cantidad de componentes
    __relaciones=None
    __nodos=None


    def __init__(self, cant, pond=False):
        self.__cantn=cant
        self.__ponderado=pond
        #Unidimensional
        self.__componentes= int(self.__cantn*(self.__cantn+1)/2) #n(n+1)/2
        self.__relaciones= np.full(self.__componentes, 0)
        self.__nodos= np.full(self.__cantn, None)



    def CargarNodo(self, nodo):
        if self.Indice(nodo):
            self.__nodos[nodo]= nodo
        else:
            print("Error con el Nodo ingresado.")

    def Aristas(self, i,j,peso=1): #Si es ponderado, en peso viene un valor y si no es ponderado se carga 1 para las relaciones
        if self.Indice(i,j):
            posicion=self.Posicion(i,j) #Obtenemos la posición
            self.__relaciones[posicion]= peso
        else:
            print("Error con el Nodo ingresado.")



    def Indice(self, i, j=0):
        valid=True
        if i<0 or j<0 or i >= self.__cantn or j >= self.__cantn:
            valid= False
        return valid

    def Posicion(self,i,j): #Posición del arreglo
        i+= 1
        j+= 1
        if i<=j:
            aux=j
            j=i
            i=aux
        pos= int(i *(i-1)/2 + j)
        pos=pos-1
        return pos

    def Adyacente(self, nodo):
        adyacentes=[]
        if self.Indice(nodo):
            for i in range(self.__cantn):
                posicion= self.Posicion(nodo, i)#Traemos una posición
                if self.__relaciones[posicion] > 0: #Si es mayor que 0 entonces es que hay una relación
                    adyacentes.append(i)#Osea que en el caso de que haya relación lo agregamos a la lista
        else:
            print("Error con el Nodo ingresado.")
        return adyacentes

    def Grado(self, nodo):
        adya= self.Adyacente(nodo)
        grado=len(adya)
        return grado

    def Camino(self, nodoi, nodod):
        camino=[]
        if self.Indice(nodoi, nodod):
            datos= self.BuscarREA(nodoi)
            #anteriores=datos[1]
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


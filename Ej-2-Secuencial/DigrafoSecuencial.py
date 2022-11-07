import numpy as np
from Cola import Cola

class DigrafoSecuencial:
    cantn=0
    ponderado=False #Probar poniendole FALSE
    matriz=None
    nodos=None


    def __init__(self, cantn, pond):
        self.__cantn=cantn
        self.__ponderado=pond
        self.__relaciones= np.full((self.__cantn, self.__cantn),0)
        self.__nodos= np.full(self.__cantn, None)



    def CargarNodo(self, nodo):
        if self.Indice(nodo):
            self.__nodos[nodo]= nodo
        else:
            print("Error con el Nodo ingresado.")

    def Aristas(self, nodoa, nodob,peso=1): #Si es ponderado, en peso viene un valor y si no es ponderado se carga 1 para las relaciones
        if self.Indice(nodoa,nodob):
            self.__relaciones[nodoa][nodob]= peso
        else:
            print("Error con el Nodo ingresado.")

    def Adyacente(self, nodo):
        adyacentes=[]
        if self.Indice(nodo):
            for i in range(self.__cantn):
                if self.__relaciones[nodo][i] > 0: #Si es mayor que 0 entonces es que hay una relación
                    adyacentes.append(i)#Osea que en el caso de que haya relación lo agregamos a la lista
        else:
            print("Error con el Nodo ingresado.")
        return adyacentes

    def Camino(self, nodoi, nodod):
        camino=[]
        if self.Indice(nodoi, nodod):
            datos= self.BuscarREA(nodoi)
            #anteriores=datos[1]
            camino= self.auxCamino(nodod, datos[1])
        else:
            print("Error con los nodos ingresados")
        return camino

    def Grado(self, nodo):
        cont=0
        adya= self.Adyacente(nodo)
        salida=len(adya)
        for i in range(self.__cantn):
            if i != nodo:
                adyai= self.Adyacente(i)
                if nodo in adyai:
                    cont+=1
        return cont, salida


    def BuscarREA(self, nodoi):
        vistos=np.full(self.__cantn, False)
        anteriores=np.full(self.__cantn, None)
        recorrido=[]
        cola=Cola()


        vistos[nodoi]=True
        cola.Insertar(nodoi)

        while not cola.Vacia():
            nv= cola.Suprimir()
            recorrido.append(nv)
            nu= self.Adyacente(nv)
            for u in nu:
                if vistos[u] == False:
                    vistos[u]= True
                    anteriores[u]= nv
                    cola.Insertar(u)
        return vistos, anteriores, recorrido


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



    def Indice(self, i, j=0):
        valid=True
        if i<0 or j<0 or i >= self.__cantn or j >= self.__cantn:
            valid= False
        return valid

    def Aciclico(self):
        i=0
        aciclico=True
        warshall=self.Warshall(self.__relaciones)
        while i < self.__cantn and aciclico:
            if warshall[i][i] >= 1:
                aciclico=False
            i+=1
        return aciclico

    def Warshall(self, P): #Llega la matriz
        for k in range(self.__cantn):
            for i in range(self.__cantn):
                for j in range(self.__cantn):
                    P[i][j]= P[i][j] or (P[i][k] and P[k][j])
        return P

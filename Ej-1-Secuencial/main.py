from GrafoSecuencial import GrafoSecuencial

import os
import json

def manejadorArchivo(ponderado):
    archivo= open("grafos.json", "r")
    contenido= archivo.read()
    jsonDecodificado= json.loads(contenido)
    if not ponderado:
        grafo= jsonDecodificado[0]
    else:
        grafo= jsonDecodificado[1]
    nodos= grafo['nodos']
    relaciones= grafo['relaciones']
    return nodos, relaciones

def tipoGrafo():
    print('\n----------------------MENU DE OPCIONES---------------------')
    print("1-Grafo ponderado")
    print("2-Grafo no ponderado")
    eleccion=int(input("Ingrese una OPCION:  "))
    while eleccion != 1 and eleccion != 2:
        print("Elija entre 1 o 2")
        eleccion=int(input("Ingrese una OPCION: "))
    if eleccion == 1:
        ponderado=True
        nodos, relaciones= manejadorArchivo(ponderado)
    elif eleccion == 2:
        ponderado=False
        nodos, relaciones= manejadorArchivo(ponderado)
    return nodos, relaciones, ponderado

def configuracionGrafo(grafo, nodos, relaciones, ponderado):
    for nodo in nodos:
        grafo.CargarNodo(nodo)
    for relacion in relaciones:
        relacuno=relacion[0]
        relacdos= relacion[1]
        peso=1
        if ponderado:
            peso=relacion[2]
        grafo.Aristas(relacuno,relacdos,peso)
    return grafo


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1- Adyacentes de nodo ingresado')
        print('\n 2- Grado de nodo ingresado')
        print('\n 3- Camino de nodo a otro')
        print('\n 4- Grafo conexo')
        print('\n 5- Grafo acíclico')
        print('\n 6- Salir')
        print('\n 7- ---')
        opcion = int(input('\n Ingrese una OPCION: '))
#-----------------------------------------------------------------------------------
        if(opcion == 1):
            nodo=int(input("Ingrese el nodo que desea ver sus adyacentes:  "))
            adya=grafo.Adyacente(nodo)
            print("Los nodos adyacentes del ingresado son: {}".format(adya))
#-----------------------------------------------------------------------------------
        if(opcion == 2):
            nodo=int(input("Ingrese el nodo que desea ver su grado:  "))
            grado=grafo.Grado(nodo)
            print("El grado del nodo ingresado es: {}" .format(grado))
#-----------------------------------------------------------------------------------
        if(opcion == 3):
            nodoi=int(input("Ingrese nodo inicio:  "))
            nodod=int(input("Ingrese nodo destino: "))
            camino=grafo.Camino(nodoi,nodod)
            print("El camino es: {}".format(camino))
#-----------------------------------------------------------------------------------
        if(opcion == 4):
            bandera=grafo.Conexo()
            if bandera:
                print("El grafo es conexo.")
            else:
                print("El grafo no es conexo.")
#-----------------------------------------------------------------------------------
        if(opcion == 5):
            bandera=grafo.Aciclico()
            if bandera:
                print("El grafo es aciclico.")
            else:
                print("El grafo no es aciclico.")
#-----------------------------------------------------------------------------------
        if(opcion == 6):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')
        if(opcion == 7):
            grafo.prueba()



if __name__ == '__main__':
    nodos, relaciones, ponderado= tipoGrafo()
    grafo= GrafoSecuencial(len(nodos), ponderado)
    grafo= configuracionGrafo(grafo, nodos, relaciones, ponderado)
    menu()

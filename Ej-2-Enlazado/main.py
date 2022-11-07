from DigrafoEnlazado import DigrafoEnlazado
import os
import json

def manejadorArchivo(ponderado):
    archivo= open("digrafos.json", "r")
    contenido= archivo.read()
    jsonDecodificado= json.loads(contenido)
    if not ponderado:
        digrafo= jsonDecodificado[0]
    else:
        digrafo= jsonDecodificado[1]
    nodos= digrafo['nodos']
    relaciones= digrafo['relaciones']
    return nodos, relaciones

def tipoDigrafo():
    print('\n----------------------MENU DE OPCIONES---------------------')
    print("1-Digrafo ponderado")
    print("2-Digrafo no ponderado")
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

def configuracionDigrafo(digrafo, nodos, relaciones, ponderado):
    for nodo in nodos:
        digrafo.CargarNodo(nodo)
    for relacion in relaciones:
        relacuno=relacion[0]
        relacdos= relacion[1]
        peso=1
        if ponderado:
            peso=relacion[2]
        digrafo.Aristas(relacuno,relacdos,peso)
    return digrafo


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1- Adyacentes de nodo ingresado')
        print('\n 2- Grado de nodo ingresado')
        print('\n 3- Camino de nodo a otro')
        print('\n 4- Digrafo conexo')
        print('\n 5- Digrafo acíclico')
        print('\n 6- Salir')
        print('\n 7- ---')
        opcion = int(input('\n Ingrese una OPCION: '))
#-----------------------------------------------------------------------------------
        if(opcion == 1):
            nodo=int(input("Ingrese el nodo que desea ver sus adyacentes:  "))
            adya=digrafo.Adyacente(nodo)
            print("Los nodos adyacentes del ingresado son: {}".format(adya))
#-----------------------------------------------------------------------------------
        if(opcion == 2):
            nodo=int(input("Ingrese el nodo que desea ver su grado:  "))
            grado=digrafo.Grado(nodo)
            print("El grado de entrada del nodo ingresado es: {}" .format(grado[0]))
            print("El grado de salida del nodo ingresado es: {}" .format(grado[1]))
#-----------------------------------------------------------------------------------
        if(opcion == 3):
            nodoi=int(input("Ingrese nodo inicio:  "))
            nodod=int(input("Ingrese nodo destino: "))
            camino=digrafo.Camino(nodoi,nodod)
            print("El camino es: {}".format(camino))
#-----------------------------------------------------------------------------------
        if(opcion == 4):
            bandera=digrafo.Conexo()
            if bandera:
                print("El Digrafo es conexo.")
            else:
                print("El Digrafo no es conexo.")
#-----------------------------------------------------------------------------------
        if(opcion == 5):
            bandera=digrafo.Aciclico()
            if bandera:
                print("El Digrafo es aciclico.")
            else:
                print("El Digrafo no es aciclico.")
#-----------------------------------------------------------------------------------
        if(opcion == 6):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')
        if(opcion == 7):
            digrafo.prueba()



if __name__ == '__main__':
    nodos, relaciones, ponderado= tipoDigrafo()
    digrafo= DigrafoEnlazado (len(nodos), ponderado)
    digrafo= configuracionDigrafo(digrafo, nodos, relaciones, ponderado)
    menu()

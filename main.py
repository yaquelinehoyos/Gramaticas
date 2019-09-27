import os
import platform

from archivo import Archivo
from gramatica import Gramatica
from validador import Validador
from validador import ValidadorError
from adaptador import Adaptador
from reconocer import Reconocer

gramatica = Gramatica()
archivo = None


def get_clear_command_by_os():
    switcher = {'Linux': "clear", 'Windows': "cls", 'Darwin': "clear"}
    return switcher[platform.system()]


def display_tittle_bar():
    os.system(get_clear_command_by_os())

    print("\t********************************************************************************")
    print("\t***  Laboratorio teoría de Lenguajes 201901 - Practica 2: Gramáticas         ***")
    print("\t********************************************************************************")


def get_user_choice():

    print("Selecciona una opción")

    print("\t1 - Cargar desde archivo")
    print("\t2 - Determinar clase de gramatica")
    print("\t3 - Mostrar conjunto de selección")
    print("\tq - Salir")

    return input("inserta un numero valor >> ")


choice = ''
display_tittle_bar()

while choice != 'q':

    display_tittle_bar()

    choice = get_user_choice()

    if choice == "1":

        #print("")

        nombre_archivo = input("\nIngrese el nombre del archivo\n>>")
        
        try:
            
            archivo = Archivo()
            archivo.cargar_archivo("./gramaticas/" + nombre_archivo, "r")
            lista_gramatica = archivo.obtener_lista_desde_archivo()

            validador = Validador()
            validador.validar_todo(lista_gramatica)

            adaptador = Adaptador()
            gramatica = adaptador.pasar_lista_a_gramatica(lista_gramatica)
            
            __primeros_no_terminales = ['a','d']
            __primeros_produccion = {}
            __primeros = []
            __siguientes_no_terminales =[]
            __anulables_produccion = []
            __anulables = []

            __producciones = gramatica.obtener_producciones()
            __terminales = gramatica.obtener_terminales()
            __no_terminales = gramatica.obtener_no_terminales()

            reconocer = Reconocer()
            tipo = reconocer.tipo_gramatica(gramatica)
            if tipo[0] == 1:
                print("Es gramatica especial")
            if tipo[1] == 1:
                print("Es gramatica lineal")
            if tipo[2] == 1:
                print("Es gramatica ll")
            if tipo[3] == 1:
                print("Es gramatica s")
            if tipo[4] == 1:
                print("Es gramatica q")
            
            # def primeros_no_terminales(self, __producciones, __terminales, __no_terminales, __anulables):
            # for _seguir in range(0,len(__no_terminales))
            #         for _recorrer in range(0,len(__producciones)):
            #             _produccion = __producciones[_recorrer]
            #                 if produccion[0] == __no_terminales[_seguir]
            #                     if produccion[1] in __terminales:
            #                         __primeros_no_terminales = {__no_terminales[_seguir]: produccion[1]} 
            #                     else: 
            #                         if produccion[1] in __no_terminales:
            #                             if produccion[1] in __anulables
            #                                 _anulable_local
            #                                 _iteracion = 1
            #                                 while produccion[_iteracion] and iteracion <= len(produccion):
            #                                     if produccion[_iteracion] != produccion[0]
            #                                         _anulable_local = produccion[_iteracion]
            #                                     _iteracion =+
            #                                 primeros_no_terminales( __producciones, __terminales, _anulable_local, __anulables)                               
            #                         else
            #                         __primeros_producciones = {__no_terminales[_seguir]: primeros[produccion[1]]}#si algo .index

            # def primeros_producciones(self, __producciones, __terminales, __no_terminales, __anulables):
            #     for _recorrer in range(0,len(__producciones)):
            #             _produccion = __producciones[_recorrer]
            #             if _produccion[1] in __terminales:
            #                 __primeros_produccion[_recorrer] = _produccion[1]
            #             else: 
            #                 #falta verificar
            #                 if _produccion[1] in __no_terminales:
            #                     print(_produccion[1])
            #                     if _produccion[1] in __anulables:
            #                         _anulable_local
            #                         _iteracion = 1
            #                         while _produccion[_iteracion] and iteracion <= len(_produccion) and _produccion[_iteracion] in __anulables:
            #                             _anulable_local = _produccion[_iteracion]
            #                             _iteracion = _iteracion + 1
            #                         for _verificar in range(0,len(_anulable_local)):
            #                             __primeros_produccion = {_recorrer: __primeros_no_terminales[_anulable_local[_verificar]]}
            #                         if _produccion[_iteracion] in __terminales:
            #                             __primeros_producciones = {_recorrer: _produccion[_iteracion]}
            #                         else:   
            #                             __primeros_producciones = {_recorrer: __primeros_no_terminales[_produccion[_iteracion]]}
            #                     else:
            #                         __primeros_producciones = {_recorrer: __primeros_no_terminales[_produccion[1]]}#si algo .index o verificar
            #                     if _produccion[1] == '@':
            #                         __primeros_produccion[_recorrer] = _produccion[1]   
            #             print(__primeros_produccion) 
            
        except FileNotFoundError:
            print("El archivo no existe en la carpeta gramaticas")
        except ValidadorError as Error:
            print(Error)
        
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")

    elif choice == "2":

        print("")

        if gramatica is None:

            print("Do something")

        else:

            print("Do something")

        input("Has pulsado la opción 2...\npulsa una tecla para continuar")

    elif choice == "3":

        print("")

        if gramatica is None:

            print("Cargue el automata a validar (Opción 1)")

            # else:

            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        else:

            print("Do something")

        input("Has pulsado la opción 3...\npulsa una tecla para continuar")

    elif choice == "q":

        print("...Hasta luego")

    else:

        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

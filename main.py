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
    print("\t***  Laboratorio teoria de Lenguajes 201901 - Practica 2: Gramaticas         ***")
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

        nombre_archivo = input("\nIngrese el nombre del archivo\n>>")

        try:

            archivo = Archivo()
            archivo.cargar_archivo("./gramaticas/" + nombre_archivo, "r")
            lista_gramatica = archivo.obtener_lista_desde_archivo()

            validador = Validador()
            validador.validar_todo(lista_gramatica)

            adaptador = Adaptador()
            gramatica = adaptador.pasar_lista_a_gramatica(lista_gramatica)

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
            reconocer = Reconocer()
            es_produccion_anulable = reconocer.es_produccion_anulable(['<B>','<C>','<D>'], gramatica)
            """tipo = reconocer.tipo_gramatica(gramatica)
            print(tipo)
            if tipo == 0:
                print("No es ningun tipo solicitado en la practica")
            if tipo == 1:
                print("Es gramatica especial")
            if tipo == 2:
                print("Es gramatica lineal")
            if tipo == 3:
                print("Es gramatica ll")
            if tipo == 4:
                print("Es gramatica s")
            if tipo == 5:
                print("Es gramatica q") 
            """
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")

    elif choice == "3":

        print("")

        if gramatica is None:

            print("Cargue el automata a validar (Opción 1)")

            # else:

            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        # else:

            # reconocer = Reconocer()
            # _select= reconocer.mostrar_seleccion(gramatica)
            # print(_select)

        input("Has pulsado la opción 3...\npulsa una tecla para continuar")

    elif choice == "q":

        print("...Hasta luego")

    else:

        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

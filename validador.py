class ValidadorError(Exception):
    pass

import re

class Validador:

    __regex_sintaxis_correcta_produccion = "^<\w+>->(\w+|<\w+>|\s|(\D^>^<))+$"

    def validar_todo(self,lista_gramatica):
        self.__validar_lista_vacia(lista_gramatica)
        self.__validar_producciones(lista_gramatica)

    def __validar_lista_vacia(self, lista_gramatica):

        if lista_gramatica == None:

            raise ValidadorError("La lista está vacía")
    
    def __validar_producciones(self, lista_gramatica):

        sintaxis_correcta_produccion = re.compile(self.__regex_sintaxis_correcta_produccion)

        for i in range(0, len(lista_gramatica)):

            if sintaxis_correcta_produccion.match(lista_gramatica[i]) == False:

                raise ValidadorError("La sintaxis de la produccion {0}".format(lista_gramatica[i]))
                
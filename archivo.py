from typing import List


class Archivo:
    __archivo = None
    __lista = []

    def cargar_archivo(self, ruta_completa, modo):
        self.__archivo = open(ruta_completa, modo)

    def obtener_lista_desde_archivo(self):

        if not self.__lista:
            self.__lista = self.__archivo.read().splitlines()

        return self.__lista

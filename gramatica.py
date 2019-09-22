class Gramatica:

    __producciones = []
    __terminales = []
    __no_terminales = []

    def asignar_produciones(self,producciones):
        self.__producciones = producciones

    def asignar_terminales(self,terminales):
        self.__terminales = terminales

    def asignar_no_terminales(self,no_terminales):
        self.__no_terminales = no_terminales

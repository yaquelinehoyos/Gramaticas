class Gramatica:

    __producciones = []
    __terminales = []
    __no_terminales = []

    __simbolos = {"nulo":"λ","fin_secuencia":"┤"}

    @staticmethod
    def obtener_simbolo_nulo():
        return Gramatica.__simbolos["nulo"]

    def asignar_produciones(self,producciones):
        self.__producciones = producciones

    def asignar_terminales(self,terminales):
        self.__terminales = terminales

    def asignar_no_terminales(self,no_terminales):
        self.__no_terminales = no_terminales

    def obtener_producciones(self):
        return self.__producciones

    def obtener_terminales(self):
        return self.__terminales

    def obtener_no_terminales(self):
        return self.__no_terminales

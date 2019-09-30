import re

from gramatica import Gramatica

class Adaptador:

    __regex_split_por_termino = r"(<\w>->)|(\w)|(<\w>)|(\D)"
    __regex_no_terminal = r"(<\w>)"
    __regex_terminal = r"(\w)"
    __regex_lado_derecho = r"(<\w>->)"
    __separador_lados_produccion = "->"
    
    def pasar_lista_a_gramatica(self, lista_gramatica):

        producciones = self.__obtener_producciones(lista_gramatica)
        no_terminales = self.__obtener_no_terminales(producciones)
        terminales = self.__obtener_terminales(producciones)

        gramatica = Gramatica()
        gramatica.asignar_produciones(producciones)
        gramatica.asignar_no_terminales(no_terminales)
        gramatica.asignar_terminales(terminales)

        return gramatica        

    def __obtener_producciones(self, lista_gramatica):
        
        producciones = []
        
        for i in range(0,len(lista_gramatica)):
            produccion = []

            for match in re.finditer(self.__regex_split_por_termino, lista_gramatica[i]):
                
                elemento = match.group()
                elemento = self.__quitar_separador(elemento)
                produccion.append(elemento)
            producciones.append(produccion)

        return producciones

    def __obtener_no_terminales(self, producciones):

        no_terminales = []

        for i in range(0,len(producciones)):
            produccion = producciones[i]
            
            for j in range(0,len(produccion)):

                elemento = produccion[j]

                if re.match(self.__regex_no_terminal,elemento):
                    no_terminales.append(elemento)

        no_terminales = list(dict.fromkeys(no_terminales))

        return no_terminales
    
    def __obtener_terminales(self, producciones):

        terminales = []

        for i in range(0,len(producciones)):
            produccion = producciones[i]
            
            for j in range(0,len(produccion)):

                elemento = produccion[j]

                if re.match(self.__regex_terminal,elemento) and elemento != Gramatica.obtener_simbolo_nulo():
                      terminales.append(elemento)
        
        terminales = list(dict.fromkeys(terminales))

        return terminales
    
    def __quitar_separador(self, elemento):

        if re.match(self.__regex_lado_derecho,elemento):
            elemento = elemento.replace(self.__separador_lados_produccion,"")
        
        return elemento

        

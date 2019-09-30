class Reconocer:

    __anulables = []
    __producciones_anulables = []
    __primeros_no_terminales = {}
    __primeros_produccion = {}
    __siguientes_no_terminales = {}
    __seleccion = {}

    # falta
    def primeros_producciones(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0, len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _produccion[1] in __terminales:
                self.__primeros_produccion[_recorrer] = _produccion[1]
            else:
                # falta verificar
                if _produccion[1] in __no_terminales:
                    print(_produccion[1])
                    if _produccion[1] in self.__anulables:
                        _anulable_local
                        _iteracion = 1
                        while _produccion[_iteracion] and _iteracion <= len(_produccion) and _produccion[_iteracion] in self.__anulables:
                            _anulable_local = _produccion[_iteracion]
                            _iteracion = _iteracion + 1
                        for _verificar in range(0, len(_anulable_local)):
                            __primeros_produccion = {
                                _recorrer: self.__primeros_no_terminales[_anulable_local[_verificar]]}
                        if _produccion[_iteracion] in __terminales:
                            __primeros_producciones = {
                                _recorrer: _produccion[_iteracion]}
                        else:
                            __primeros_producciones = {
                                _recorrer: self.__primeros_no_terminales[_produccion[_iteracion]]}
                    else:
                        # si algo .index o verificar
                        __primeros_producciones = {
                            _recorrer: self.__primeros_no_terminales[_produccion[1]]}
                    if _produccion[1] == '@':
                        __primeros_produccion[_recorrer] = _produccion[1]
            # print(self.__primeros_produccion)

    # listo
    def anulables_produccion(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0, len(__producciones)):
            _anulable = False
            _produccion = __producciones[_recorrer]
            if _produccion[1] == '@':
                self.__producciones_anulables.append(_recorrer)
            else:
                for _seguir in range(1, len(_produccion)):
                    if _produccion[1] in self.__anulables:
                        if _produccion[_seguir] in self.__anulables:
                            _anulable = True
                        else:
                            _anulable = False
                if _anulable:
                    self.__producciones_anulables.append(_recorrer)
    # listo

    def anulables(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0, len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _produccion[1] == '@':
                self.__anulables.append(_produccion[0])
    # falta
    """def primeros_no_terminales(self, __producciones, __terminales, __no_terminales):
       for _seguir in range(0,len(__no_terminales)):
            for _recorrer in range(0,len(__producciones)):
                _produccion = __producciones[_recorrer]
                if _produccion[0] == __no_terminales[_seguir]:
                    if _produccion[1] in __terminales:
                        __primeros_no_terminales = {__no_terminales[_seguir]: _produccion[1]} 
                    else: 
                        if _produccion[1] in __no_terminales:
                            if _produccion[1] in self.__anulables:
                                _anulable_local
                                _iteracion = 1
                                while _produccion[_iteracion] and _iteracion <= len(_produccion):
                                    if _produccion[_iteracion] != _produccion[0]:
                                        _anulable_local = _produccion[_iteracion]
                                    _iteracion += 1
                                primeros_no_terminales(__producciones, __terminales, _anulable_local, __anulables)                               
                        # else:
                        #     __primeros_producciones = {__no_terminales[_seguir]: primeros[produccion[1]]}#si algo .index"""
    # #falta
    # def anulables_recursivo(self, __producciones, __terminales, __no_terminales):
    # #falta
    # def siguientes_no_terminales(self, __producciones, __terminales, __no_terminales):

    # listo
    def seleccion(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0, len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _recorrer in self.__producciones_anulables:
                self.__seleccion[_recorrer] = self.__siguientes_no_terminales.get(
                    _produccion[0])
            else:
                self.__seleccion[_recorrer] = self.__primeros_produccion[_recorrer]

    # listo
    def tipo_gramatica(self, gramatica):
        __producciones = gramatica.obtener_producciones()
        __terminales = gramatica.obtener_terminales()
        __no_terminales = gramatica.obtener_no_terminales()
        self.anulables(__producciones, __terminales, __no_terminales)
        self.anulables_produccion(
            __producciones, __terminales, __no_terminales)
        #self.primeros_no_terminales(__producciones, __terminales, __no_terminales)
        self.primeros_producciones(
            __producciones, __terminales, __no_terminales)
        # self.siguientes_no_terminales(__producciones, __terminales, __no_terminales)
        self.seleccion(__producciones, __terminales, __no_terminales)
        is_s = False
        is_q = False
        is_q_maybe = True
        is_ll = False
        is_lineal = False
        is_especial = False
        tipo = 0
        if len(self.__anulables) == 0:
            is_s = self.es_s(__producciones, __terminales, __no_terminales)
        else:
            for _recorrer in range(0, len(__producciones)):
                if self.__primeros_produccion.get(_recorrer) in __no_terminales:
                    is_q_maybe = False
        if is_q_maybe:
            is_q = self.es_q(__producciones, __terminales, __no_terminales)
            is_lineal = self.es_lineal(
                __producciones, __terminales, __no_terminales)
            is_especial = self.es_especial(
                __producciones, __terminales, __no_terminales)
        else:
            is_ll = self.es_ll(__producciones, __terminales, __no_terminales)
        if is_especial:
            is_lineal = False
        if is_s:
            is_q = False
        if is_especial:
            tipo = 1
        if is_lineal:
            tipo = 2
        if is_ll:
            tipo = 3
        if is_s:
            tipo = 4
        if is_q:
            tipo = 5
        return tipo

    # falta porque faltan los metodos que alli se llaman
    # def mostrar_seleccion(self, gramatica):
    #     __producciones = gramatica.obtener_producciones()
    #     __terminales = gramatica.obtener_terminales()
    #     __no_terminales = gramatica.obtener_no_terminales()
    #     self.anulables(__producciones, __terminales, __no_terminales)
    #     self.anulables_produccion(__producciones, __terminales, __no_terminales)
    #     self.primeros_no_terminales(__producciones, __terminales, __no_terminales)
    #     self.primeros_producciones(__producciones, __terminales, __no_terminales)
    #     self.__siguientes_no_terminales(__producciones, __terminales, __no_terminales)
    #     return self.__seleccion(__producciones, __terminales, __no_terminales)

    # listo
    def es_s(self, __producciones, __terminales, __no_terminales):
        _is = True
        for _recorrer in range(0, len(__no_terminales)):
            _verificar = []
            _definir = []
            for _seguir in range(0, len(__producciones)):
                _produccion = __producciones[_seguir]
                if __no_terminales[_recorrer] == _produccion[0]:
                    _verificar.append(_seguir)
            for ver in range(0, len(_verificar)):
                _definir.append(self.__primeros_produccion[_verificar[ver]])
            _final = set(_definir)
            if len(_final) != len(_definir):
                _is = False
        return _is

    # listo
    def es_especial(self, __producciones, __terminales, __no_terminales):
        _is = False
        for _seguir in range(0, len(__producciones)):
            _produccion = __producciones[_seguir]
            if len(_produccion) == 3:
                if _produccion[1] in __terminales and _produccion[2] in __no_terminales:
                    _is = True
                else:
                    _is = False
                    break
            if len(_produccion) == 2:
                if _produccion[1] == '@':
                    _is = True
                else:
                    _is = False
                    break
        return _is

    # listo
    def es_lineal(self, __producciones, __terminales, __no_terminales):
        _is = False
        for _seguir in range(0, len(__producciones)):
            _produccion = __producciones[_seguir]
            if len(_produccion) == 2:
                if _produccion[1] == '@':
                    _is = True
                else:
                    _is = False
                    break
            else:
                for _recorrer in range(1, len(_produccion)-1):
                    if _produccion[len(_produccion)-1] in __no_terminales:
                        if _produccion[_recorrer] in __terminales:
                            _is = True
                        else:
                            _is = False
                            break
        return _is

    # listo
    def es_q(self, __producciones, __terminales, __no_terminales):
        _is = True
        for _recorrer in range(0, len(__no_terminales)):
            _verificar = []
            _definir = []
            for _seguir in range(0, len(__producciones)):
                _produccion = __producciones[_seguir]
                if __no_terminales[_recorrer] == _produccion[0]:
                    _verificar.append(_seguir)
            for ver in range(0, len(_verificar)):
                _definir.append(self.__seleccion.get(_verificar[ver]))
            for element in _definir:
                if len(element) > 1:
                    for x in element:
                        for y in _definir:
                            if x == y:
                                _is = False
                else:
                    if _definir.count(element) > 1:
                        _is = False
            return _is

    # listo
    def es_ll(self, __producciones, __terminales, __no_terminales):
        _is = True
        for _recorrer in range(0, len(__no_terminales)):
            _verificar = []
            _definir = []
            for _seguir in range(0, len(__producciones)):
                _produccion = __producciones[_seguir]
                if __no_terminales[_recorrer] == _produccion[0]:
                    _verificar.append(_seguir)
            for ver in range(0, len(_verificar)):
                _definir.append(self.__seleccion.get(_verificar[ver]))
            for element in _definir:
                if len(element) > 1:
                    for x in element:
                        for y in _definir:
                            if x == y:
                                _is = False
                else:
                    if _definir.count(element) > 1:
                        _is = False
            return _is

    def es_produccion_anulable(self, produccion, gramatica):

        no_terminales = gramatica.obtener_no_terminales()
        terminales = gramatica.obtener_terminales()

        lado_derecho_produccion = self.__obtener_lado_derecho(produccion)
        producciones_anulables_no_terminales = []

        for elemento in lado_derecho_produccion:
            if elemento == gramatica.obtener_simbolo_nulo():
                return True
            elif elemento in terminales:
                return False
            elif elemento in no_terminales:
                producciones_anulables_no_terminal = self.__son_producciones_anulables_no_terminal(
                    elemento, gramatica)
                producciones_anulables_no_terminales.append(
                    [elemento, producciones_anulables_no_terminal])

        return self.__son_anulables_producciones_no_terminales(producciones_anulables_no_terminales)

    def __son_anulables_producciones_no_terminales(self, producciones_anulables_no_terminales):
        
        for producion in producciones_anulables_no_terminales:
            if False in producion:
                son_anulables_producciones_no_terminales = False
                break
            else:
                son_anulables_producciones_no_terminales = True

        return son_anulables_producciones_no_terminales

    def __son_producciones_anulables_no_terminal(self, elemento, gramatica):

        producciones_con_lado_izquierdo = self.__producciones_con_lado_izquierdo(
            elemento, gramatica)
        producciones_anulables = []

        for produccion in producciones_con_lado_izquierdo:
            produccion_anulable = self.es_produccion_anulable(
                produccion, gramatica)
            producciones_anulables.append(produccion_anulable)

        son_producciones_anulables_no_terminal = None
        if False in producciones_anulables:
            son_producciones_anulables_no_terminal = False
        else:
            son_producciones_anulables_no_terminal = True

        return son_producciones_anulables_no_terminal

    def __producciones_con_lado_izquierdo(self, no_terminal, gramatica):

        producciones = gramatica.obtener_producciones()
        producciones_con_lado_izquierdo = []

        for produccion in producciones:
            lado_izquierdo = self.__obtener_lado_izquierdo(produccion)
            if lado_izquierdo == no_terminal:
                producciones_con_lado_izquierdo.append(produccion)

        return producciones_con_lado_izquierdo

    def __obtener_lado_derecho(self, produccion):

        return produccion[1:len(produccion)]

    def __obtener_lado_izquierdo(self, produccion):

        return produccion[0]

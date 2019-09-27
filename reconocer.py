



class Reconocer:

    __anulables = []
    __primeros_no_terminales = []
    __primeros_produccion = {}
    __primeros = []
    __siguientes_no_terminales =[]
    nulos_produccion = []
    

    def primeros_producciones(self, __producciones, __terminales, __no_terminales):
       for _recorrer in range(0,len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _produccion[1] in __terminales:
                self.__primeros_produccion[_recorrer] = _produccion[1]
            else: 
                #falta verificar
                if _produccion[1] in __no_terminales:
                    print(_produccion[1])
                    if _produccion[1] in __anulables:
                        _anulable_local
                        _iteracion = 1
                        while _produccion[_iteracion] and iteracion <= len(_produccion) and _produccion[_iteracion] in __anulables:
                            _anulable_local = _produccion[_iteracion]
                            _iteracion = _iteracion + 1
                        for _verificar in range(0,len(_anulable_local)):
                            __primeros_produccion = {_recorrer: __primeros_no_terminales[_anulable_local[_verificar]]}
                        if _produccion[_iteracion] in __terminales:
                            __primeros_producciones = {_recorrer: _produccion[_iteracion]}
                        else:   
                            __primeros_producciones = {_recorrer: __primeros_no_terminales[_produccion[_iteracion]]}
                    else:
                        __primeros_producciones = {_recorrer: __primeros_no_terminales[_produccion[1]]}#si algo .index o verificar
                    if _produccion[1] == '@':
                        __primeros_produccion[_recorrer] = _produccion[1]   
            # print(self.__primeros_produccion) 
    
    #listo
    def anulables_produccion(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0,len(__producciones)):
            _anulable = False
            _produccion = __producciones[_recorrer]
            if _produccion[1] == '@':
                self.nulos_produccion.append(_recorrer)
            else:
                for _seguir in range (1,len(_produccion)):
                    if _produccion[1] in self.__anulables:
                        if _produccion[_seguir] in self.__anulables:
                            _anulable = True
                        else: 
                            _anulable = False
                if _anulable:
                    self.nulos_produccion.append(_recorrer)
    #listo
    def anulables(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0,len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _produccion[1] == '@':
                self.__anulables.append(_produccion[0])
    #falta
    def primeros_no_terminales(self, __producciones, __terminales, __no_terminales):
       for _seguir in range(0,len(__no_terminales)):
            for _recorrer in range(0,len(__producciones)):
                _produccion = __producciones[_recorrer]
                if _produccion[0] == __no_terminales[_seguir]:
                    if _produccion[1] in __terminales:
                        __primeros_no_terminales = {__no_terminales[_seguir]: _produccion[1]} 
                    else: 
                        if _produccion[1] in __no_terminales:
                            if _produccion[1] in __anulables:
                                _anulable_local
                                _iteracion = 1
                                while _produccion[_iteracion] and iteracion <= len(_produccion):
                                    if _produccion[_iteracion] != _produccion[0]:
                                        _anulable_local = _produccion[_iteracion]
                                    _iteracion += 1
                                primeros_no_terminales( __producciones, __terminales, _anulable_local, __anulables)                               
                        # else:
                        #     __primeros_producciones = {__no_terminales[_seguir]: primeros[produccion[1]]}#si algo .index

    # def anulables_recursivo(self, __producciones, __terminales, __no_terminales):

    # def siguientes_no_terminales(self, __producciones, __terminales, __no_terminales, __primeros, __anulables):

    # def seleccion(self, __producciones, __terminales, __no_terminales):

    #falta retorno
    def tipo_gramatica(self, gramatica):
        __producciones = gramatica.obtener_producciones()
        __terminales = gramatica.obtener_terminales()
        __no_terminales = gramatica.obtener_no_terminales()
        self.anulables(__producciones, __terminales, __no_terminales)
        self.anulables_produccion(__producciones, __terminales, __no_terminales)
        self.primeros_no_terminales(__producciones, __terminales, __no_terminales)
        self.primeros_producciones(__producciones, __terminales, __no_terminales)
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
            for _recorrer in range(0,len(__producciones)):
                if self.__primeros_produccion.get(_recorrer) in __no_terminales:
                    is_q_maybe = False
        if is_q_maybe:
            # is_q = self.es_q(__producciones, __terminales, __no_terminales)
            is_lineal = self.es_lineal(__producciones, __terminales, __no_terminales)
            is_especial = self.es_especial(__producciones, __terminales, __no_terminales)
        # else:
        #     is_ll = self.es_ll(__producciones, __terminales, __no_terminales)
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
    #listo
    def es_s(self, __producciones, __terminales, __no_terminales):
        _is = True
        for _recorrer in range (0,len(__no_terminales)):
            _verificar = []
            _definir = []
            for _seguir in range (0,len(__producciones)):
                _produccion = __producciones[_seguir]                   
                if __no_terminales[_recorrer] == _produccion[0]:
                    _verificar.append(_seguir)
            for ver in range (0,len(_verificar)):
                _definir.append(self.__primeros_produccion[_verificar[ver]])
            _final = set(_definir)
            if len(_final) != len(_definir):
                _is = False
        return _is 

    #listo
    def es_especial(self, __producciones, __terminales, __no_terminales):
        _is = False
        for _seguir in range (0,len(__producciones)):
            _produccion = __producciones[_seguir]             
            if len(_produccion) == 3:
                if _produccion[1] in __terminales and _produccion[2] in __no_terminales:
                    _is = True
                else: 
                    _is = False
                    break
            if len(_produccion) == 2:
                if _produccion[1] == '@' :
                    _is = True
                else: 
                    _is = False  
                    break
        return _is

    #listo
    def es_lineal(self, __producciones, __terminales, __no_terminales):
            _is = False
            for _seguir in range (0,len(__producciones)):
                _produccion = __producciones[_seguir]             
                if len(_produccion) == 2:
                    if _produccion[1] == '@' :
                        _is = True
                    else: 
                        _is = False 
                        break 
                else:
                    for _recorrer in range (1, len(_produccion)-1):
                        if _produccion[len(_produccion)-1] in __no_terminales:
                            if _produccion[_recorrer] in __terminales:
                                _is = True
                            else: 
                                _is = False
                                break
            return _is

    # def es_q(self, __producciones, __terminales, __no_terminales):
        

    # def es_ll(self, __producciones, __terminales, __no_terminales):
    
    
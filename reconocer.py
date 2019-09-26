class Reconocer:

        __primeros_no_terminales
        __primeros_produccion
        __primeros
        __siguientes_no_terminales
        __anulables_produccion
        __anulables

    def primeros_producciones(self, __producciones, __terminales, __no_terminales, __anulables):
       for _recorrer in range(0,len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _produccion[1] in __terminales:
                __primeros_produccion[_recorrer] = _produccion[1]
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
            print(__primeros_produccion) 
    
    #listo
    def anulables_produccion(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0,len(__producciones)):
            _anulable = False
            _produccion = __producciones[_recorrer]
            if _produccion[1] == '@':
                __anulables_produccion.append(_recorrer)
            else:
                for _seguir in range (1,len(_produccion)):
                    if _produccion[1] in __anulables:
                        if _produccion[_seguir] in __anulables:
                            _anulable = True
                        else: 
                            _anulable = False
                if _anulable:
                    __anulables_produccion.append(_recorrer)
    #listo
    def anulables(self, __producciones, __terminales, __no_terminales):
        for _recorrer in range(0,len(__producciones)):
            _produccion = __producciones[_recorrer]
            if _produccion[1] == '@':
                __anulables.append(_produccion[0])
    #falta
    def primeros_no_terminales(self, __producciones, __terminales, __no_terminales, __anulables):
       for _seguir in range(0,len(__no_terminales)):
            for _recorrer in range(0,len(__producciones)):
                _produccion = __producciones[_recorrer]
                    if produccion[0] == __no_terminales[_seguir]:
                        if produccion[1] in __terminales:
                            __primeros_no_terminales = {__no_terminales[_seguir]: produccion[1]} 
                        else: 
                            if produccion[1] in __no_terminales:
                                if produccion[1] in __anulables:
                                    _anulable_local
                                    _iteracion = 1
                                    while produccion[_iteracion] and iteracion <= len(produccion):
                                        if produccion[_iteracion] != produccion[0]
                                            _anulable_local = produccion[_iteracion]
                                        _iteracion =+
                                    primeros_no_terminales( __producciones, __terminales, _anulable_local, __anulables)                               
                            else:
                            __primeros_producciones = {__no_terminales[_seguir]: primeros[produccion[1]]}#si algo .index

    def anulables_recursivo(self, __producciones, __terminales, __no_terminales):

    def siguientes_no_terminales(self, __producciones, __terminales, __no_terminales, __primeros, __anulables):

    def seleccion(self, __producciones, __terminales, __no_terminales):

    #falta retorno
    def tipo_gramatica(self, __producciones, __terminales, __no_terminales):
        anulables_produccion(__producciones, __terminales, __no_terminales)
        anulables(__producciones, __terminales, __no_terminales)
        primeros_no_terminales(__producciones, __terminales, __no_terminales)
        primeros_producciones(__producciones, __terminales, __no_terminales)
        is_s
        is_q
        is_q_maybe
        is_ll
        is_lineal
        is_especial
        if if len(__anulables) == 0:
            is_s = this.es_s(__producciones, __terminales, __no_terminales)
        else:
            for _recorrer in range(0,len(__primeros_produccion))
                if if __primeros_produccion[_recorrer] in __no_terminales::
                   is_q_maybe = False
        if is_q_maybe:
            is_q = this.es_q(__producciones, __terminales, __no_terminales)
            is_lineal = this.es_lineal(__producciones, __terminales, __no_terminales)
            is_especial = this.es_especial(__producciones, __terminales, __no_terminales)
        else:
            es_ll = this.es_ll(__producciones, __terminales, __no_terminales)

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
                _definir.append(__primeros_produccion[_verificar[ver]])
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
                        for _recorrer in range (1, len(_produccion)-1)
                            if _produccion[len(_produccion)] in __no_terminales:
                                if _produccion[_recorrer] in __terminales:
                                    _is = True
                                else: 
                                    _is = False
                                    break
            return _is

    def es_q(self, __producciones, __terminales, __no_terminales):
        

    def es_ll(self, __producciones, __terminales, __no_terminales):
    
    
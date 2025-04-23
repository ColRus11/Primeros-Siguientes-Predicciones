def es_terminal(simbolo, gramatica):
    return simbolo not in gramatica

def calcular_primeros(gramatica):
    primeros = {nt: set() for nt in gramatica}
    cambio = True

    while cambio:
        cambio = False
        for A, producciones in gramatica.items():
            for prod in producciones:
                if prod == ['ε']:
                    if 'ε' not in primeros[A]:
                        primeros[A].add('ε')
                        cambio = True
                else:
                    nullable = True
                    for X in prod:
                        if es_terminal(X, gramatica):
                            if X not in primeros[A]:
                                primeros[A].add(X)
                                cambio = True
                            nullable = False
                            break
                        else:
                            for p in primeros[X]:
                                if p != 'ε' and p not in primeros[A]:
                                    primeros[A].add(p)
                                    cambio = True
                            if 'ε' in primeros[X]:
                                continue
                            else:
                                nullable = False
                                break
                    if nullable and 'ε' not in primeros[A]:
                        primeros[A].add('ε')
                        cambio = True
    return primeros

def calcular_siguientes(gramatica, primeros):
    siguientes = {nt: set() for nt in gramatica}
    S0 = list(gramatica.keys())[0]
    siguientes[S0].add('$')
    cambio = True

    while cambio:
        cambio = False
        for A, producciones in gramatica.items():
            for prod in producciones:
                for i, B in enumerate(prod):
                    if not es_terminal(B, gramatica):
                        first_beta = set()
                        nullable_beta = True
                        for C in prod[i+1:]:
                            if es_terminal(C, gramatica):
                                first_beta.add(C)
                                nullable_beta = False
                                break
                            else:
                                first_beta |= (primeros[C] - {'ε'})
                                if 'ε' in primeros[C]:
                                    continue
                                else:
                                    nullable_beta = False
                                    break
                        if first_beta - siguientes[B]:
                            siguientes[B] |= first_beta
                            cambio = True
                        if nullable_beta or i == len(prod)-1:
                            if siguientes[A] - siguientes[B]:
                                siguientes[B] |= siguientes[A]
                                cambio = True
    return siguientes

def calcular_predicciones(gramatica, primeros, siguientes):

    predicciones = {}
    for A, producciones in gramatica.items():
        listas = []
        for prod in producciones:
            first_alpha = set()
            nullable = True
            for X in prod:
                if es_terminal(X, gramatica):
                    first_alpha.add(X)
                    nullable = False
                    break
                else:
                    first_alpha |= (primeros[X] - {'ε'})
                    if 'ε' in primeros[X]:
                        continue
                    else:
                        nullable = False
                        break
            if nullable or prod == ['ε']:
                lista_predict = first_alpha | siguientes[A]
            else:
                lista_predict = first_alpha
            listas.append(lista_predict)
        predicciones[A] = listas
    return predicciones

gramatica = {
    'S': [['A','B','C'], ['D','E']],
    'A': [['dos','B','tres'], ['ε']],
    'B': [['B','cuatro','C','cinco'], ['ε']],
    'C': [['seis','A','B'], ['ε']],
    'D': [['uno','A','E'], ['B']],
    'E': [['tres']]
}

primeros = calcular_primeros(gramatica)
siguientes = calcular_siguientes(gramatica, primeros)
predicciones = calcular_predicciones(gramatica, primeros, siguientes)

for A in gramatica:
    print(f"Primero({A}) = {primeros[A]}")
print()
for A in gramatica:
    print(f"Siguiente({A}) = {siguientes[A]}")
print()
for A, prods in gramatica.items():
    for idx, prod in enumerate(prods):
        print(f"PREDICCIÓN({A} -> {' '.join(prod)}) = {predicciones[A][idx]}")

def ingresar_numero(): 
    entrada = input("Ingrese un número: ") 
    try: 
        return int(entrada) 
    except ValueError: 
        return None 
 
def es_par(numero): 
    if numero % 2 == 0:
        return 1
    return 0
 
def agregar_a_vector(valor, vector): 
    vector.append(valor) 
 
def mostrar_vector(vector): 
    print(vector) 
 
def sumar_si_mayor_cien(valor, suma_actual): 
    if valor > 100:
        return suma_actual + valor
    return suma_actual
 
def contar_si_mayor_cien(valor, contador_actual): 
    if valor > 100:
        return contador_actual + 1
    return contador_actual
 
def calcular_promedio(suma, cantidad): 
    if cantidad > 0:
        return suma / cantidad
    return 0
 
def obtener_maximo(valor, max_actual): 
    if valor > max_actual:
        return valor
    return max_actual
 
def obtener_posicion(valor, max_actual, pos_actual, indice): 
    if valor > max_actual:
        return indice
    return pos_actual
 
def es_menor_diez(valor): 
    if valor < 10:
        return 1
    return 0
 
def insertar_despues_de_mayor_a_menos_cinco(valor, vector_resultado): 
    agregar_a_vector(valor, vector_resultado) 
    if valor > -5: 
        agregar_a_vector(999, vector_resultado) 
 
def ordenar_descendente(vector): 
    longitud = len(vector)
    for i in range(longitud):
        for j in range(0, longitud - i - 1):
            if vector[j] < vector[j + 1]:
                # Intercambiar valores
                temporal = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = temporal
    return vector
 
def programa(): 
    # Ingreso de números 
    numeros = [] 
    for _ in range(5):  
        numero = None 
        while numero is None: 
            numero = ingresar_numero() 
            if numero is None: 
                print("Entrada inválida. Intente de nuevo.") 
        agregar_a_vector(numero, numeros) 
 
    # Separar pares e impares 
    pares = [] 
    impares = [] 
    for numero in numeros: 
        if es_par(numero) == 1: 
            agregar_a_vector(numero, pares) 
        else: 
            agregar_a_vector(numero, impares) 
 
    # 1. Mostrar pares e impares 
    print("\n1. Mostrar números pares e impares:") 
    print("Pares:") 
    mostrar_vector(pares) 
    print("Impares:") 
    mostrar_vector(impares) 
 
    # 2. Promedio de pares mayores a 100 
    print("\n2. Promedio de los números pares mayores a 100:") 
    suma_pares = 0 
    contador_pares = 0 
    for par in pares: 
        suma_pares = sumar_si_mayor_cien(par, suma_pares) 
        contador_pares = contar_si_mayor_cien(par, contador_pares) 
 
    promedio = calcular_promedio(suma_pares, contador_pares) 
    print(promedio) 
 
    # 3. Máximo y posición en impares 
    print("\n3. Máximo y su posición en impares:") 
    if impares:  # Verificar si el vector no está vacío
        maximo_impares = impares[0] 
        posicion_maximo = 0 
        for i in range(len(impares)): 
            maximo_impares = obtener_maximo(impares[i], maximo_impares) 
            posicion_maximo = obtener_posicion( 
                impares[i], maximo_impares, posicion_maximo, i 
            ) 
 
        print(f"Máximo en impares: {maximo_impares}, posición: {posicion_maximo}") 
        if posicion_maximo < len(pares): 
            print("Número en la misma posición en pares:", pares[posicion_maximo]) 
        else: 
            print("No hay un número en la misma posición en pares.") 
    else:
        print("No hay números impares.")
 
    # 4. Crear vector con elementos menores a 10 
    menores_diez = [] 
    for par in pares: 
        if es_menor_diez(par) == 1: 
            agregar_a_vector(par, menores_diez) 
 
    for impar in impares: 
        if es_menor_diez(impar) == 1: 
            agregar_a_vector(impar, menores_diez) 
 
    print("\n4. Números menores a 10:") 
    mostrar_vector(menores_diez) 
 
    # 5. Insertar 999 después de números mayores a -5 
    vector_modificado = [] 
    for valor in menores_diez: 
        insertar_despues_de_mayor_a_menos_cinco(valor, vector_modificado) 
 
    print("\n5. Vector modificado:") 
    mostrar_vector(vector_modificado) 
 
    # 6. Ordenar vector descendentemente 
    vector_ordenado = ordenar_descendente(vector_modificado) 
    print("\n6. Vector ordenado descendentemente:") 
    mostrar_vector(vector_ordenado) 
 
# Ejecutar el programa 
programa()
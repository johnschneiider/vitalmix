def leer_modelo():
    modelo = ""
    while modelo not in ["ALTA", "BAJA", "STOP"]:
        modelo = input("Ingrese el modelo ( 'ALTA', 'BAJA', 'STOP' para terminar ): ").strip().upper()
        if modelo not in ["ALTA", "BAJA", "STOP"]:
            print("Re ingrese el modelo: ")
    return modelo
    
def leer_cantidad():
    cantidad = -1
    while cantidad <= 0:
        entrada = int(input("Ingrese la cantidad solicitada ( debe ser mayor a 0): "))
        if entrada:
            cantidad = entrada
        if cantidad <= 0:
            print("Cantidad invalida. ingrese un numero mayor a cero: ")
    return cantidad
    
 
 
def agregar_datos(modelos, cantidades, modelo, cantidad):
    modelos.append(modelo)
    cantidades.append(cantidad)
    
def obtener_datos_modelos(modelos,cantidades):
    contador = 0
    max_lecturas = 650
    
    while contador < max_lecturas:
        modelo = leer_modelo()
        if modelo == "STOP":
            return contador
        cantidad = leer_cantidad()
        agregar_datos(modelos,cantidades,modelo,cantidad)
        contador += 1
    return contador
    
def mostrar_tabla(modelos,cantidades):
    print("\nTabla de modelos y cantidades: ")
    print(f"{'modelo':<10} {'cantidad':<10}")
    print("-" * 20)
    for i in range(len(modelos)):
        print(f"{modelos[i]:<10} {cantidades[i]:<10}")
        
def encontrar_maximo(cantidades):
    max_valor = cantidades[0]
    for cantidad in cantidades:
        if cantidad > max_valor:
            max_valor = cantidad
    return max_valor
    
def obtener_modelo_mayor_cantidad(modelos,cantidades):
    max_cantidad = encontrar_maximo(cantidades)
    for i in range(len(cantidades)):
        if cantidades[i] == max_cantidad:
            return modelos[i]
 
 
def calcular_promedio(cantidades):
    suma = 0
    for cantidad in cantidades:
        suma += cantidad
    promedio = suma / len(cantidades)
    return promedio
        
def eliminar_mayores_promedio(modelos, cantidades, promedio):
    i = 0
    while i < len(cantidades):
        if cantidades[i] > promedio:
            modelos.pop(i)
            cantidades.pop(i)
        else:
            i += 1
    
        
 
 
def insertar_agregado_multiplo_cinco(modelos,cantidades):
    i = 0
    while i < len(cantidades):
        if cantidades[i] % 5 == 0:
            modelos.insert(i+1, "AGREGADO")
            cantidades.insert(i + 1, cantidades[i] // 2)
            i += 1
        i += 1        
        
def ordenar_por_cantidades(modelos, cantidades):
    for i in range(len(cantidades)):
        for j in range(i + 1, len(cantidades)):
            if cantidades[i] > cantidades[j]:
                cantidades[i], cantidades[j] = cantidades[j], cantidades[i]
                modelos[i], modelos[j] = modelos[j], modelos[i]
                
def principal():
    modelos = []
    cantidades = []
    datos_leidos = obtener_datos_modelos(modelos, cantidades)
    if datos_leidos == 0:
        print("No se encontro datos. Fin")
        return
    
    mostrar_tabla(modelos,cantidades)
    mayor_modelo = obtener_modelo_mayor_cantidad(modelos,cantidades)
    print(f"\nModelo con mayor cantidad solicitada: {mayor_modelo}")
    
    
    promedio = calcular_promedio(cantidades)
    print(f"\nPromedio de cantidades solicitadas: {promedio: .2f}")
    
    eliminar_mayores_promedio(modelos,cantidades,promedio)
    print("\nDatos despues de eliminar cantidades mayores al promedio: ")
    mostrar_tabla(modelos,cantidades)
    
    insertar_agregado_multiplo_cinco(modelos,cantidades)
    print("\nDatos despues de insertar modelos 'AGREGADO': ")
    mostrar_tabla(modelos,cantidades)
    
    ordenar_por_cantidades(modelos,cantidades)
    print("\nDatos ordenados por cantidad")
    mostrar_tabla(modelos,cantidades)
 
 
 
 
    
principal()
        
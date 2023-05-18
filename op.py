print("Hola mundo por consola")

# Función para mostrar una tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)
# Menú de opciones
while True:
    print("Elige una tabla de multiplicar del 1 al 10: ")
    #la entrada del usuario se guarda en la variable (opcion)
    opcion = input()
    
    # Validación de entrada para saber si la opcion esta entre el 1 y el 10
    try:
        opcion = int(opcion)
        #si (opcion) es menor a 1 o (opcion) es mayor que 10 entonces:
        if opcion < 1 or opcion > 10:
            print("Opción inválida. Intente de nuevo.")
            continue
    except:
        print("Opción inválida. Intente de nuevo.")
        continue
    
    # si la opcion es valida, funcion (tabla_multiplicar) se llama con el numero elegido como argumento
    #lo que muestra la tabla correspondiente por consola
    tabla_multiplicar(opcion)
    
    # Salida del menú
    # Se le pregunta al usuario si desea salir
    #Se crea una variable (salir) en donde se pregunta si desea salir

    salir = input("¿Desea salir? (s/n): ")
    if salir == 's' or salir == 'S':
        #break rompe el codigo y termina el programa si la condicion es (s o S)
        break

def contador_palabras(oracion):
    palabras = oracion.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

oracion_usuario = input("Ingrese una oracion: ")
cantidad_palabras = contador_palabras(oracion_usuario)
print("Su oracion tiene: ", cantidad_palabras, " Palabras")
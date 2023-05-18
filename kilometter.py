numero = int(input("Ingresa un número entero positivo: "))
# usaremos (suma_pares) para almacenar la suma de todos los números pares.
suma_pares = 0


# for para iterar de 2 en 2 
for i in range(2, numero+1, 2):
    suma_pares += i 

print("La suma de todos los números pares entre 1 y", numero, "es", suma_pares)

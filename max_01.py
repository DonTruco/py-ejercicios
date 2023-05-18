"""
    Toma 2 numero cmo argumentos y hacer que devuelva el mayor de ellos
    
    definimos una funcion custom_max() que tiene como paramentro 2 variables llamadas:

    n1, n2 tipo enteros

    Si n1 es mayor a que n2 entonces devuleve (n1) porque es el mayor.
    else devuelve el numero 2 porque si el (n1) no es mayor el (n2) sí.

    if n1> n2:
        return n1
    else:
        return n2

    Mostrar los resultador por consola y pasar los valores a custom_max(n1 es 300, n2 es400)
"""
def custom_max(n1:int , n2: int):
    if n1> n2:
        return n1
    else:
        return n2
    
print(custom_max(300, 400))
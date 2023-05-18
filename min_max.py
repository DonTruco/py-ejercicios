import random
#crear lista vacia 
lista_valores  = []
#for i en rango del 1 al 10 
for i in range (10):
    #a la lista de valores le vamos a agregar un numero aleatorio dentro del rango del 1 al 100
    lista_valores.append(random.randint(1, 100))
    #crear variable (maximo) que tendra el metodo max y min para calcular el maximo y minimo de la (lista_valores)
    maximo = max(lista_valores)
    minimo = min(lista_valores)

#mostrar la lista completa
print('la lista aleatoria es: ', lista_valores)
#muestra el maximo
print('El maximo es: ', maximo)
#muestra el minimo
print('El minimo es: ', minimo)
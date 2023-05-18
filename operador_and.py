# se crea la variable (valor) que contiene un numero elegido por el usuario entre el 1 y el 10
valor = int(input("Elija un numero del 1 al 10: "))
#Si el (valor) es mayor o igual a 1 Y el valor es menor o igual a 10 entonces:
if (valor >= 1 and valor<=10):
    #resultado si es exitoso
    print("Tu valor se encuentra en el rango del 1 al 10")
elif (valor >=10 and valor<=20):
    print("Tu valor se encuentra en el rango del 10 al 20")
elif (valor >=20 and valor <=30):
    print("Tu valor se encuentra en el rango del 20 al 30")
else:
    #mensaje de error por ingresar un numero que no es
    print("Elija una opcion valida")
#informe de que valor ingreson el usuario
print("Su opcion fue: ", valor)
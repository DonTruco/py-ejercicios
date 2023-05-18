#numeros que van a  estar en todo el programa
def numeros():
    num1 = int(input('Primer numero : '))
    num2 = int(input('Segundo numero : '))
    #Debe devolver los valores num1 y num2 para que puedan ser utilizados por las demás funciones.
    return num1, num2

#funcion para la suma
def suma(num1, num2):
    #la variable(resutado_suma va hacer el proceso de suma)
    resultado_suma= num1+num2
    #imprimimos el resultado de la operacion
    print('El resultado de la suma es: ', resultado_suma)

#funcion para la resta
def resta(num1, num2):
    #la variable(resutado_rest va hacer el proceso de resta)
    resultado_rest = num1 - num2
    #imprimimos el resultado de la operacion
    print('El resultado de la resta es: ', resultado_rest)

#funcion para la multiplicacion
def multiplicacion(num1, num2):
    #la variable(resutado_mult va hacer el proceso de multiplicacion)
    resultado_mult = num1 * num2  
    #imprimimos el resultado de la operacion
    print('El resultado de la multiplicacion es: ', resultado_mult)

#funcion para la division
def division(num1, num2):
    #la variable(resutado_div va hacer el proceso de division)
    resultado_div = num1 / num2
    #imprimimos el resultado de la operacion
    print('El resultado de la division es: ', resultado_div)


#funcion MAIN LO PRINCIPAL
def run():
    #miestras que TOD sea TRUE ejecuta (eleccion) 
    while True:
        eleccion = int(input("""
        
            Elija una opcion: 

                1. quiero sumar 
                2. quiero restar
                3. quiero multiplicar
                4. quiero dividir 
        
        """))
        #Si el usuario elige la opción 1,
        if eleccion == 1:
            #se llama a la función numeros() para obtener los dos números a operar
            num1, num2 = numeros()
            #Luego, se llama a la función suma() y se pasan los dos números obtenidos como argumentos.
            suma(num1, num2)
        elif eleccion == 2:
            num1, num2 = numeros()
            resta(num1, num2)
        elif eleccion == 3:
            num1, num2 = numeros()
            multiplicacion(num1, num2)
        elif eleccion == 4:
            num1, num2 = numeros()
            division(num1, num2)
            
        else:
            #Si el usuario elige una opción que no está en el menú, se muestra un mensaje de error.
            print("Opción inválida. Por favor, seleccione una opción válida.")
           
        #aca se rompe el bucle while
        #si lo borro se ejecuta varias veces
        break

if __name__ == '__main__':
    run()
#LA TRIPLE COMILLA SIRVE PARA QUE LA CONSOLA 
#LEA TODAS LAS LINEAS DE TEXTO


#definir la funcion 
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos "+tipo_pesos+" tienes ?: ")
    #pesos se convierte de un string a un numero con (float)
    pesos = float(pesos)
    #la variable (dolares) define cuanto cuesta con base en los pesos ingresados anteriormente
    dolares = pesos / valor_dolar
    #round sirve para reducir el (float) a numeros mas chicos
    dolares = round(dolares, 2)
    #ya que los (dolares) son obtenidos con numeros
    #se traducen a strings por medio del operador (str)
    dolares = str(dolares)
    #Se imprime el resultado
    print("tienes: $ "+ dolares + " Dolares ")

#La variable (menu) contiene el menu donde el usuario ingresa un n.
#la Variable (menu) almacena el numero que el usuario ingrese
menu = """
    Bienvenido al conversor de monedas a dolares

    Elige una opcion:
    1. Pesos Colombianos
    2. Pesos Argentinos
    3. Pesos Mexicanos
"""
#le voy a mostrar el mensaje de arriba al usuario
#y lo que escriba el usuario se almacena gracias al (input)
#y a ese valor se alamcenara dentro de la variable de (opcion)
opcion = int(input(menu))


#Inicio de la condicional
if opcion == 1:
    #El protocolo de valor del dólar se define con base en el tipo de peso
    conversor("Colombianos", 3875)

elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else :
    print('Ingrese la opcion correcta')
    











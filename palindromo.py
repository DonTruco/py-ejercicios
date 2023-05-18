#la funcion palindromo recibe una palabra
def palindromo(palabra):
    #reemplazar los espacios enblanco a nada
    #eliminar espacios en blanco
    palabra = palabra.replace(' ', '')
    #poner todas las letras en minuscula
    palabra = palabra.lower()
    #esto va desde el final hasta el principio en pasos negativos
    #genera la palabra al reves
    palabra_invertida = palabra[:: -1]
    #condicionales
    if palabra == palabra_invertida:
        return True
    else:
        return False
#siempre dejar 2 espacios en cada funcion
#obligatorio una funcion inicial
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

#obligatorio para escribir codigo py
if __name__ == '__main__':
    run()

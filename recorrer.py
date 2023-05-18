def run():
    #variable (nombre) almacena cada letra
    # nombre = input('Escribe tu nombre: ')
    #para las letras en el nombre, vamos imprimir cada letra en cada repeticion
    # for letra in nombre:
    #     print('letra: ' + letra)

    frase = input('Escribe una frase: ')
    for caracter in frase:
        print('letra: '+ caracter.upper())

    for i in ('hola mundo'):
        print(i)

if __name__ == '__main__':
    run()
import os
import random

def eleccion ():

    while True:
        print("¿Qué acción deseas realizar?")
        print("1. Agregar una nueva palabra")
        print("2. Mostrar la lista de palabras")
        print("3. Salir")

        choice = input("Ingresa el número correspondiente a la acción que deseas realizar:\n")

        if choice == "1":
            new_word = input("Ingresa una nueva palabra:")
            word_list.append(new_word)
            print("Palabra agregada con éxito.\n") 
            
        elif choice == "2":
            print("Lista de palabras:")
            for word in word_list:
                print(word)
        elif choice == "3":
            print("¡Hasta luego!")
            break
        elif choice == "4":
            print ("Opcion 3 ya puedes JUGAR !")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
    word_list = []

def run():
    IMAGES = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        ========='''
    ]

    DB = [
        "C",
        "PYTHON",
        "JAVA",
        "JAVASCRIPT",
        "PHP"
    ]

    # Con el módulo random se elige una palabra aleatoria de DB
    word = random.choice(DB)
    # Lista llamada (spaces) que contiene guiones bajos por la cantidad de letras que tenga en la palabra
    spaces = ["_"] * len(word)
    # variable para crear las oportunidades
    attempts = 6
    # bucle infinito
    while True:
        # limpiar la consola
        os.system("cls")
        # imprimir la imagen en el índice de los intentos que le quedan al usuario
        print(IMAGES[attempts])
        # mostrar los guiones bajos preparados con un for
        # para los caracteres en la variable (spaces)
        for character in spaces:
            # imprime el caracter y termina con un espacio para que no se haga un salto de linea
            print(character, end=" ")
        # al digitar la letra, se convierte en mayúscula con (upper)
        letter = input('\nElige una letra: ').upper()
        # crear variable (found) con valor de (false) es la que indica si la persona encontró la letra en cada uno de los ciclos
        found = False
        # para ver si el usuario encuentra las letras
        # recorrer índices y caracteres de enumerate de la palabra que eligió la computadora random
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        if not found:
            attempts -= 1
        if "_" not in spaces:
            os.system("cls")
            print('¡Ganaste!')
            break
        if attempts == 0:
            os.system("cls")
            print('¡Perdiste! La palabra era: ', word)
            break

if __name__ == '__main__':
    run()



palabra = input("Ingresa una palabra: ")
vocales = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        vocales += 1

print("El número de vocales en la palabra es:", vocales)


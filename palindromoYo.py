def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    input_reves = palabra[::-1]

    if palabra == input_reves:
        return True
    else:
        return False
print(palindromo('Ana '))
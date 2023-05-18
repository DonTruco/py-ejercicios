def run():
    edad=int(input('Ingrese su edad para ingresar a la licoreria: '))

    if edad > 18:
        print("Menú de cervezas:")
        print("1. Cerveza A - $2.50")
        print("2. Cerveza B - $3.00")
        print("3. Cerveza C - $3.50")
        print("4. Cerveza D - $4.00")

        opcion=int(input('Seleccione una cerveza del 1 al 4: '))
        cantidad=int(input('Seleccione la cantidad de cervezas que desea llevar'))
        if opcion == 1:
            total=cantidad*2.50
        elif opcion == 2:
            total=cantidad*3.00
        elif opcion == 3:
            total=cantidad*3.50
        elif opcion == 4:
            total=cantidad*4.00
        else:
            print('opcion invalida')
            total=0
        
        if total >0:
            print('El precio total a pagar es de: $', total)
        else:
            print('Solo para mayores de edad')

if __name__ == '__name__':
    run()
"""
    Creación de una clase básica:

    -En este ejercicio, se crea la clase (Persona) con un constructor( __init__) que inicializa los atributos (nombre) y (edad.)
    -La clase también tiene un método (saludar) que imprime un mensaje de saludo con el nombre y la edad de la persona.
    -Se crean dos objetos de la clase Persona y se llama al método saludar para cada objeto.
"""
class Persona:
    #__init__ es un constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #metodo saludar que va imprimir el nombre y la edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear objetos y llamar a métodos
persona1 = Persona("Juan", 25)
#llamar al metodo saludar 
persona1.saludar()

persona2 = Persona("María", 30)
persona2.saludar()


def contador ():
    print('Hola mundo')
contador()

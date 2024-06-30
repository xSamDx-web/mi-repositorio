class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}!")

# Ejemplo de uso
objeto = MiClase("Sam")
objeto.saludar()

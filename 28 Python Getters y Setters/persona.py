class Persona:
    __edad = 55
    def __init__(self, nombre, apellido): # constructor
        self.__nombre = nombre
        self.apellido = apellido

    @property
    def nombre(self):
        return self.__nombre + '!!!'

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) >= 5:
            self.__nombre = nombre

    def __saludar(self):
        print('Hola', self.__nombre)

    def __str__(self):
        # self.__nombre = 'Federico'
        # self.__saludar()
        return "Me llamo: " + self.__nombre + ' ' + self.apellido

juan = Persona('Juan Pablo', 'Garcia')
# juan.__nombre = 'Pedro Peter'
print(juan)
juan.nombre = 'Pedro Peter'
print(juan.nombre)

juan.apellido = 'Fernandez'
print(juan.apellido)

# print(Persona.__edad)

# juan.__saludar()

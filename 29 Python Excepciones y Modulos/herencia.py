class Animal:
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje = mensaje

    def hablar(self):
        pass

    def __str__(self):
        return 'Soy un ' + self.nombre

class Perro(Animal):
    def hablar(self):
        print('Soy un ' + self.nombre + ' y Ladro: ' + self.mensaje)

class Gato(Animal):
    def hablar(self):
        print('Soy un ' + self.nombre + ' y Maullo: ' + self.mensaje)

perro = Perro('Firulais', 'Guau guau')
perro.hablar()
print(perro)

gato = Gato('Michi', 'Miau')
gato.hablar()
print(gato)

# animal = Animal('Perro')
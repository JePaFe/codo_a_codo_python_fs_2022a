class Alumno:
    cantidad = 0
    def __init__(self, nombre, nota): # constructor
        self.nombre = nombre
        self.nota = nota
        Alumno.cantidad += 1

    def imprimir(self):
        print('Nombre:', self.nombre)
        print('Nota:', self.nota)
        print('Cantidad:', Alumno.cantidad)

    def mostrarEstado(self):
        if self.nota >= 4:
            print('Aprobado')
        else:
            print('Desaprobado')

alumno1 = Alumno('Juan', 3)
alumno1.nombre = 'Pedro'
alumno1.imprimir()
alumno1.mostrarEstado()

alumno2 = Alumno('María', 5)
alumno2.imprimir()
alumno2.mostrarEstado()

print('Cantidad', Alumno.cantidad)
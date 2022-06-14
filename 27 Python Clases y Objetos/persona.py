class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print('Nombre:', self.nombre, ', edad:', self.edad)

persona1 = Persona()
persona1.inicializar('Juan', 20)
persona1.imprimir()

persona2 = Persona()
persona2.inicializar('María', 21)
persona2.imprimir()
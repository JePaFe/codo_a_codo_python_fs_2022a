import random

from modulo import saludar, numeros

from paquete.hola import hola
import paquete.chau

from paquete.chau import hola as hola_chau

paquete.chau.chau()
hola()
hola_chau()

# print(modulo.numeros)
print(numeros)

saludar('Juan')
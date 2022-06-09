def saludar(nombre, mensaje = 'Hola'):
    print(mensaje, nombre)

# saludar('Juan', 'Hola')
# saludar('Maria')
# saludar('Pedro', 'Saludos')

# saludar(mensaje='Bienvenida', nombre='Claudia')
# saludar(nombre='Claudia', mensaje='Bienvenida')
# saludar(nombre='Claudia')

def mi_funcion(num1, num2=4, num3=6):
    print(num1, num2, num3)

mi_funcion(2)
mi_funcion(2, 4, 8)
mi_funcion(2, num3=7)

# def sumarIVA(monto, iva = 21):
#     print('monto con IVA')

# sumarIVA(100)
# sumarIVA(200, 10.5)
def saludar(nombre, mensaje = 'Hola'):
    resultado = mensaje + ' ' + nombre
    return resultado

msg = saludar('Juan')
print(msg)
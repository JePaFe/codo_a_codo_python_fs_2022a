def saludar_N_veces(stop, msg, lista):
    stop = 3
    lista.append(6)
    for i in range(stop):
        print(msg, str(i))

try:
    veces = int(input('Cantidad: '))
    # msg = input('Mensaje: ')
    numeros = [1, 2, 3]

    print(veces, numeros)
    saludar_N_veces(veces, 'Hola', numeros)
    print(veces, numeros)
except: 
    print('No es un numero')
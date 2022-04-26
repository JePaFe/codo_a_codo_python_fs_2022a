function saludar(nombre) {
    console.log('Hola ' + nombre);
}

saludar('Juan');
saludar('Ana');

var nombre = prompt('Ingrese su nombre');
saludar(nombre);

saludar(prompt('Ingrese su nombre'));

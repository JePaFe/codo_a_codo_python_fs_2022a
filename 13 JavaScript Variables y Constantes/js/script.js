console.log("Hola's JS", 2 + 3);

/*
    Esto es
    un comentario
*/
// document.write('Hola JavaScript');

var numero = 123;
// numero = 456;

console.log(numero);

var nombreCompletoUsuario = 'Juan Perez';

console.log(nombreCompletoUsuario);

const IVA_FINAL = 21;

console.log('El IVA es', IVA_FINAL - 5 + '%');

var num1 = {};

console.log(typeof num1);

const auto = {
    ruedas: 4,
    marca: 'Fiat',
    modelo: 2021
};

auto.marca = 'Ford';

console.log(auto, auto.marca);

const garage = {
    espacio_1: auto,
}

var num2 = '123t';
num2 = Number(num2);
console.log(typeof num2, num2, num2 + 1);

var num3 = '123.23t';
num3 = parseInt(num3);
console.log(num3);

var num4 = '123.23t';
num4 = parseFloat(num4);
console.log(num4);
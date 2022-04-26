function sumar(num1, num2) {
    // var resultado = num1 + num2;
    // return resultado;

    return num1 + num2;
}

var sumar = (num1, num2) => num1 + num2;

var resultado1 = sumar(2, 3);
console.log(resultado1)
var resultado2 = sumar(1, 6);
alert(resultado2)

var resultado3 = sumar(sumar(2, 3), sumar(1, 6));
console.log(resultado3)


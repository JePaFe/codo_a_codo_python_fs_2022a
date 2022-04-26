function multiplicarConDosParametros(tabla, desde, hasta) {
    if (desde > hasta) {
        return console.log('El desde tiene que ser menor que el hasta');
    }

    for (var i = desde; i <= hasta; i++) {
        console.log(tabla + ' x ' + i + ' = ', tabla * i);
    }
    console.log('for... ' + i);
}

var multiplicarConDosParametros = (tabla, desde, hasta) => {
    if (desde > hasta) {
        return console.log('El desde tiene que ser menor que el hasta');
    }

    for (var i = desde; i <= hasta; i++) {
        console.log(tabla + ' x ' + i + ' = ', tabla * i);
    }
    console.log('for... ' + i);
}

var devolucion = multiplicarConDosParametros(2, 10, 6);
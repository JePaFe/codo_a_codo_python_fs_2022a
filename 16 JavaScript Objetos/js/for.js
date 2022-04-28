const juan = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'juan@example.com',
    dni: 98765432,
    admin: false,
    'nombre completo': 'Juan Perez',
    detalle() {
        return 'Nombre: ' + this.nombre + ' Email: ' + this.email;
    }
}

// console.log( juan.nombre );
// console.log( juan['nombre completo'] );

for (let propiedad in juan) {
    if (typeof juan[propiedad] != 'function') {
        console.log(propiedad + ': ' + juan[propiedad]);
    }
}
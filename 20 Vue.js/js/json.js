const persona = {
    nombre: 'Juan',
    apellido: "Perez",
    edad: 43,
    dni: 98765432,
    admin: true
}

console.log( JSON.stringify(persona) );

let juan = `{"nombre":"Juan","apellido":"Perez","edad":43,"dni":98765432,"admin":true}`;

console.log(JSON.parse(juan));
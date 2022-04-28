// let nombre = 'Juan';
// let email = 'juan@example.com';
// let admin = true;

// const usuario = new Object();

const ana = {
    nombre: 'Ana',
    email: 'ana@example.com',
    admin: true,
    detalle() {
        return 'Nombre: ' + this.nombre + ' Email: ' + this.email;
    }
}

const juan = {
    nombre: 'Juan',
    apellido: 'Perez',
    email: 'juan@example.com',
    admin: false,
    detalle() {
        return 'Nombre: ' + this.nombre + ' Email: ' + this.email;
    }
}

// usuario.nombre = 'Maria';

console.log( ana.detalle() );
class Usuario {
    constructor(nombre, email) {
        this.nombre = nombre;
        this.email = email;
        this.admin = false;
    }

    detalle() {
        return 'Nombre: ' + this.nombre + ' Email: ' + this.email;
    }

    setAdmin(valor) {
        this.admin = valor;
    }
}

const juan = new Usuario('Juan', 'juan@example.com');
const maria = new Usuario('Maria', 'maria@example.com');

// maria.setAdmin();
// maria.admin = true;
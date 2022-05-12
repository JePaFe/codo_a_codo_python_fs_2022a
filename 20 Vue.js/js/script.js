const app = Vue.createApp({
    data() {
        return {
            nombre: 'Juan',
            apellido: 'Perez'
        }
    },
    methods: {
        getNombreCompleto() {
            return this.nombre + ' ' + this.apellido;
        }
    },
    computed: {
        nombreCompleto() {
            return this.nombre + ' ' + this.apellido;
        }
    }
})

app.component('cac-titulo', {
    template: `
        <h2>{{titulo}}</h2>
        <p>{{mensaje}}</p>
    `,
    data() {
        return {
            titulo: 'Hola desde el componente'
        }
    },
    props: {
        mensaje: String
    }
});

app.component('cac-usuarios', {
    template: `
        <ul>
            <li v-for="usuario in usuarios">{{usuario.name}} - {{usuario.email}}</li>
        </ul>
    `,
    data() {
        return {
            usuarios: []
        }
    },
    created() {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(response => response.json())
            .then(json => {
                this.usuarios = json;
            })
            .catch(error => console.log(error));
    }
});

app.mount('#app');
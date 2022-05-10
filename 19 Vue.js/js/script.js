const app = Vue.createApp({
    data() {
        return {
            nombre: 'Juan',
            texto: 'Hola Vue.js',
            enlace: {
                url: 'https://google.com',
                name: 'Google'
            },
            lenguajes: ['HTML', 'CSS', 'JS'],
            usuarios: [
                { id: 1, email: '1@x.com', admin: 5 },
                { id: 2, email: '2@x.com', admin: 0 },
                { id: 3, email: '3@x.com', admin: 1 }
            ],
            mensaje: '',
            contador: 0
        }
    },
    methods: {
        sumarAlContador() {
            if (this.contador < 5) {
                this.contador++;
            }
        }
    }
});

app.mount('#app');
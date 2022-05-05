const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    const nombre = document.querySelector('#nombre');
    // if (nombre.value != 'Juan') {
    //     const span = document.querySelector('#error-nombre')
    //     span.textContent = 'El nombre es incorrecto'
    // }  

    const expresion = /^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()[\]\.,;:\s@\”]{2,})$/;
    if (!nombre.value.match(expresion)) {
        const span = document.querySelector('#error-nombre')
        span.textContent = 'No es un email'
    } else {
        form.submit()
    }
})


// ---

let el = document.querySelector('p');

// el.onclick = () => alert('Hola');

el.addEventListener('click', () => {
    alert('Hola');
});

let link = document.querySelector('a');
link.addEventListener('click', (event) => {
    event.preventDefault();
    // console.log(event)
})
let segundoParrafo = document.getElementById('segundo');
let parrafos = document.getElementsByTagName('p');

for(let i = 0; i < parrafos.length; i++) {
    // parrafos[i].textContent = (i + 1) + '. ' + parrafos[i].textContent;
}

for(item of parrafos) {
    // console.log(item.textContent)
    item.textContent = '- ' + item.textContent;
}

let footer = document.getElementById('footer');

setTimeout(() => {
    footer.textContent = 'Copyright 2022';
    // footer.innerText = 'Copyright 2022';
}, 3000);

let main = document.getElementsByTagName('main');

// main[0].innerHTML = `
//     <h2>Seccion 1</h2>
//     <p>Texto de ejemplo.</p>
// `;


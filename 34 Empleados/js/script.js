fetch('http://localhost:5000/api/empleados')
    .then(response => response.json())
    .then(json => {
        console.log(json)
        let tbody = document.querySelector('tbody')

        for(let i = 0; i < json.length; i++) {
            console.log(json[i], json[i].nombre)

            let row = `
                <tr>
                    <th scope="row">${json[i].id}</th>
                    <td>${json[i].nombre}</td>
                </tr>
            `

            tbody.innerHTML += row
        }
    })
    .catch(error => console.log(error))

// fetch('https://jsonplaceholder.typicode.com/users')
//     .then(function(response) {
//         // console.log(response);
//         return response.json();
//     })
//     .then(function(json) {
//         console.log(json);
//     })
//     .catch(function(error) {
//         console.log(error);
//     });

// fetch('https://jsonplaceholder.typicode.com/users')
//     .then(response => response.json())
//     .then(json => console.log(json))
//     .catch(error => console.log(error));

const getUsuarios = async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const json = await response.json();
        console.log(json);
    } catch(error) {
        console.log(error);
    }
}

getUsuarios();

// Axios

// <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

axios.get('https://jsonplaceholder.typicode.com/users/1')
  .then(function (json) {
    console.log(json);
  })
  .catch(function (error) {
    console.log(error);
  });
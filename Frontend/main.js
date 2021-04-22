let headers = new Headers();
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', 'http://localhost:4041');
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS');

function iniciarSesion() {
    let user = document.getElementById("usuario").value;
    let password = document.getElementById("password").value;

    fetch('http://localhost:4041/login', {
        method: 'POST',
        headers: headers,
        body: `{
    	        "usuario":"${user}",
                "password":"${password}"
                }`,
    })

        .then(response => response.json())

        .then(usuario => {
            console.log(usuario);
            if (usuario == "paciente") {
                alert('Inicio de sesion correcto')
                console.log(user);
                localStorage.setItem('nombreUsuario', user);
                window.open("modulo pacientes.html", "_self")
            } else if (usuario == "doctor") {
                alert('Inicio de sesion correcto')
                window.open("modulo doctores.html", "_self")
            } else if (usuario == "enfermero") {
                alert('Inicio de sesion correcto')
                window.open("modulo enfermeros.html", "_self")
            } else {
                alert('Credenciales incorrectas')
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function cargarDatos() {
    let user = localStorage.getItem('nombreUsuario');
    fetch('http://localhost:4041/paciente', {
        method: 'POST',
        headers: headers,
        body: `{
    	        "nombre de usuario":"${user}"
                }`,
    })

        .then(response => response.json())

        .then(usuario => {
            console.log(usuario);
            document.getElementById("datos").innerHTML = JSON.stringify(usuario);
        })
}
  
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
                localStorage.setItem('nombreUsuario', user);
                localStorage.setItem('tipoDeUsuario', usuario);
                console.log(user)
                console.log(usuario)
                window.location.replace("http://localhost:4041/paciente");
            }

            if (usuario == "doctor") {
                alert('Inicio de sesion correcto')
                localStorage.setItem('nombreUsuario', user);
                localStorage.setItem('tipoDeUsuario', usuario);
                console.log(user)
                console.log(usuario)
                window.location.replace("http://localhost:4041/doctor");
            }

            if (usuario == "enfermero") {
                alert('Inicio de sesion correcto')
                localStorage.setItem('nombreUsuario', user);
                localStorage.setItem('tipoDeUsuario', usuario);
                console.log(user)
                console.log(usuario)
                window.location.replace("http://localhost:4041/enfermero");
            }

            if (usuario == "administrador") {
                alert('Inicio de sesion correcto')
                localStorage.setItem('tipoDeUsuario', usuario);
                localStorage.setItem('nombreUsuario', user);
                console.log(user)
                console.log(usuario)
                window.location.replace("http://localhost:4041/admin");
            }
            if (usuario == "Credenciales incorrectas") {
                alert('Credenciales invalidas')
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function cargarDatos() {
    let user = localStorage.getItem('nombreUsuario');
    let tipo_usuario = localStorage.getItem('tipoDeUsuario');
    let paciente = 'http://localhost:4041/paciente';
    let doctor = 'http://localhost:4041/doctor';
    let enfermero = 'http://localhost:4041/enfermero';
    let admin = 'http://localhost:4041/admin';
    console.log(user+" "+tipo_usuario)

    function cargar(dir) {
        fetch(dir, {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre de usuario":"${user}"
                }`,
        })
            .then(response => response.json())
    
            .then(usuario => {
                localStorage.setItem('usuario', usuario);
                document.getElementById('nombre').innerHTML = usuario.nombre + " " + usuario.apellido;
                document.getElementById('usuario').innerHTML = usuario["nombre de usuario"];
            })
    }

    if (tipo_usuario == "paciente") {
        cargar(paciente);
    }

    if (tipo_usuario == "doctor") {
        cargar(doctor);
    }

    if (tipo_usuario == "enfermero") {
        cargar(enfermero);
    }

    if (tipo_usuario == "administrador") {
        cargar(admin);
    }
}

function abrirMenu(evt, nombreTab) {
    var i, contenidoTab, linkTab;

    contenidoTab = document.getElementsByClassName('tabcontent');
    for (i = 0; i < contenidoTab.length; i++) {
        contenidoTab[i].style.display = "none";
    }

    linkTab = document.getElementsByClassName("tablinks");
    for (i = 0; i < linkTab.length; i++) {
        linkTab[i].className = linkTab[i].className.replace("active", "");
    }

    document.getElementById(nombreTab).style.display = "block";
    evt.currentTarget.className += " active";
}

function eliminacion(dir, usuario) {
    fetch (dir, {
        method: 'POST',
        headers: headers,
        body: `{
                "nombre de usuario": "${usuario}"
               }`,
    })

    .then(response => response.json())

    .then(eliminado => {
        console.log(eliminado)
        if (eliminado == 'Usuario eliminado') {
            alert('Usuario eliminado')
            location.reload()
        } else if (eliminado == 'Usuario no encontrado') {
            alert('El usuario no existe')
        }

        if (eliminado == 'Medicamento eliminado') {
            alert('Medicamento eliminado')
            location.reload()
        }
    })
}

function eliminar(tipo) {
    let tabla = document.getElementById('tabla'), rIndex
    let tipoDeUsuario = tipo

    if (tipoDeUsuario == 'paciente') {      
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaPacientes[rIndex-1]['nombre de usuario']
                let direccion = 'http://localhost:4041/datos-pacientes/eliminarpaciente'
                console.log(usuario)
                eliminacion(direccion, usuario)
                }
            }
       }
    } else if (tipoDeUsuario == 'enfermera') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaEnfermeras[rIndex-1]['nombre de usuario']
                let direccion = 'http://localhost:4041/datos-enfermeras/eliminarenfermera'
                console.log(usuario)
                eliminacion(direccion, usuario)
                }
            }
       }
    } else if (tipoDeUsuario == 'doctor') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaDoctores[rIndex-1]['nombre de usuario']
                let direccion = 'http://localhost:4041/datos-doctores/eliminardoctor'
                console.log(usuario)
                eliminacion(direccion, usuario)
                }
            }
       }       
    } else if (tipoDeUsuario == 'medicamento') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaMedicamentos[rIndex-1]['nombre']
                let direccion = 'http://localhost:4041/datos-medicamentos/eliminarmedicamento'
                console.log(usuario)
                eliminacion(direccion, usuario)
                }
            }
       }       
    }
}

function enviarInfo(tipo) {
    if (tipo == 'paciente') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaPacientes[rIndex-1]['nombre de usuario']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/ver-datos')                
                }
            }
        } 
    } else if (tipo == 'enfermera') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaEnfermeras[rIndex-1]['nombre de usuario']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/ver-datos')                
                }
            }
        } 
    } else if (tipo == 'doctor') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaDoctores[rIndex-1]['nombre de usuario']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/ver-datos')                
                }
            }
        } 
    } else if (tipo == 'medicamento') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaMedicamentos[rIndex-1]['nombre']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/ver-medicamento')                
                }
            }
        }
    }
}

function mostrarDatos() {
    let user = localStorage.getItem('usuarioSeleccionado')
    let tipo = localStorage.getItem('tipo')

    if (tipo == 'paciente' || tipo == 'enfermera') {
        fetch ('http://localhost:4041/ver-datos', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre de usuario": "${user}"
            }`,
        })
            .then(response => response.json())
            .then(usuario => {
                document.getElementById('nombre').innerHTML = usuario.nombre;
                document.getElementById('apellido').innerHTML = usuario.apellido;
                document.getElementById('nacimiento').innerHTML = usuario.fecha;
                document.getElementById('sexo').innerHTML = usuario.sexo;
                document.getElementById('usuario').innerHTML = usuario["nombre de usuario"];
                document.getElementById('telefono').innerHTML = usuario.telefono;

                if (tipo == 'paciente') {
                    document.getElementById('titulo').innerHTML = 'Datos del Paciente'
                } else if (tipo == 'enfermera') {
                    document.getElementById('titulo').innerHTML = 'Datos de la Enfermera'
                }
            })
    } else if (tipo == 'doctor') {
        fetch ('http://localhost:4041/ver-datos', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre de usuario": "${user}"
            }`,
        })
            .then(response => response.json())
            .then(usuario => {
                document.getElementById('nombre').innerHTML = usuario.nombre;
                document.getElementById('apellido').innerHTML = usuario.apellido;
                document.getElementById('nacimiento').innerHTML = usuario.fecha;
                document.getElementById('sexo').innerHTML = usuario.sexo;
                document.getElementById('usuario').innerHTML = usuario["nombre de usuario"];
                document.getElementById('telefono').innerHTML = usuario.telefono;
                document.getElementById('titulo').innerHTML = 'Datos del Doctor'

                let datos = document.getElementById('datos')
                const titulo = document.createElement('label')
                const tituloTexto = document.createTextNode('Especialidad: ')
                const esp = document.createElement('label')
                const espTexto = document.createTextNode(usuario.especialidad)
                titulo.classList.add('data-title')
                esp.classList.add('data')               
                const br = document.createElement('br')
                const br1 = document.createElement('br')
                titulo.appendChild(tituloTexto)
                esp.appendChild(espTexto)
                datos.appendChild(br)
                datos.appendChild(br1)
                datos.appendChild(titulo)
                datos.appendChild(esp)
            })
    } else if (tipo == 'medicamento') {
        fetch ('http://localhost:4041/ver-medicamento', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre": "${user}"
            }`,
        })
            .then(response => response.json())
            .then(medicamento => {
                console.log(medicamento)
                document.getElementById('nombre').innerHTML = medicamento.nombre
                document.getElementById('precio').innerHTML = medicamento.precio
                document.getElementById('descripcion').innerHTML = medicamento.descripcion
                document.getElementById('cantidad').innerHTML = medicamento.cantidad
            })
    }

}

function enviarInfoUsuario(tipo) {
    if (tipo == 'administrador') {
        let usuario = localStorage.getItem('nombreUsuario')
        localStorage.setItem('usuarioSeleccionado', usuario)
        localStorage.setItem('tipo', tipo)
        console.log(usuario)
        window.location.replace('http://localhost:4041/modificarperfil')
    } else if (tipo == 'paciente' || tipo =='enfermera' || tipo == 'doctor') {
        let usuario = localStorage.getItem('nombreUsuario')
        localStorage.setItem('usuarioSeleccionado', usuario)
        localStorage.setItem('tipo', tipo)
        console.log(usuario)
        window.location.replace('http://localhost:4041/modificarperfil')      
    }
}

function enviarInfoAMod(tipo) {
    if (tipo == 'paciente') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaPacientes[rIndex-1]['nombre de usuario']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/modificarperfil')                
                }
            }
        } 
    } else if (tipo == 'enfermera') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaEnfermeras[rIndex-1]['nombre de usuario']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/modificarperfil')                
                }
            }
        } 
    } else if (tipo == 'doctor') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaDoctores[rIndex-1]['nombre de usuario']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/modificarperfil')                
                }
            }
        } 
    } else if (tipo == 'medicamento') {
        for (let i = 0; i < tabla.rows.length; i++) {
            for (let j = 0; j < tabla.rows[i].cells.length; j++) {
                tabla.rows[i].cells[j].onclick = function () {
                rIndex = this.parentElement.rowIndex

                let usuario = listaMedicamentos[rIndex-1]['nombre']
                localStorage.setItem('usuarioSeleccionado', usuario)
                localStorage.setItem('tipo', tipo)
                console.log(usuario)
                window.location.replace('http://localhost:4041/modificar-medicamento')                
                }
            }
        } 
    }
}

function datosAModificar() {
    let user = localStorage.getItem('usuarioSeleccionado')
    let tipo = localStorage.getItem('tipo')

    if (tipo == 'paciente' || tipo == 'enfermera') {
        fetch ('http://localhost:4041/modificarperfil', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre de usuario":"${user}"
            }`,
        })
            .then(response => response.json())
            .then(usuario => {
                localStorage.setItem('usuarioAModificar', user)
                localStorage.setItem('tipo', tipo)
                document.getElementById('nombre').value = usuario.nombre
                document.getElementById('apellido').value = usuario.apellido
                document.getElementById('nacimiento').value = usuario.fecha
                document.getElementById('usuario').value = usuario['nombre de usuario']
                document.getElementById('password').value = usuario.password
                document.getElementById('telefono').value = usuario.telefono

                if (usuario.sexo == 'M') {
                    let boton = document.getElementById('masculino')
                    boton.checked = true
                } else if (usuario.sexo == 'F') {
                    let boton = document.getElementById('femenino')
                    boton.checked = true
                }
            })
    } else if (tipo == 'doctor') {
        fetch ('http://localhost:4041/modificarperfil', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre de usuario":"${user}"
            }`,
        })
            .then(response => response.json())
            .then(usuario => {
                localStorage.setItem('usuarioAModificar', user)
                localStorage.setItem('tipo', tipo)
                document.getElementById('nombre').value = usuario.nombre
                document.getElementById('apellido').value = usuario.apellido
                document.getElementById('nacimiento').value = usuario.fecha
                document.getElementById('usuario').value = usuario['nombre de usuario']
                document.getElementById('password').value = usuario.password
                document.getElementById('telefono').value = usuario.telefono
                const espTitle = document.createElement('label')
                const titleText = document.createTextNode('Especialidad: ')
                espTitle.appendChild(titleText)
                const espDiv = document.getElementById('esp-container')
                const espBox = document.createElement('input')
                espBox.setAttribute('type','text')
                espBox.id = 'especialidad'
                espBox.value = usuario.especialidad
                espDiv.appendChild(espTitle)              
                espDiv.appendChild(espBox)

                if (usuario.sexo == 'M') {
                    let boton = document.getElementById('masculino')
                    boton.checked = true
                } else if (usuario.sexo == 'F') {
                    let boton = document.getElementById('femenino')
                    boton.checked = true
                }
            })
    } else if (tipo == 'medicamento') {
        fetch('http://localhost:4041/modificar-medicamento', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre":"${user}"
            }`
        })
            .then(response => response.json())
            .then(medicamento => {
                localStorage.setItem('medicamento', user)
                document.getElementById('nombre').value = medicamento.nombre
                document.getElementById('precio').value = medicamento.precio
                document.getElementById('descripcion').value = medicamento.descripcion
                document.getElementById('cantidad').value = medicamento.cantidad
            })
    } else if (tipo == 'administrador') {
        fetch('http://localhost:4041/modificarperfil', {
            method: 'POST',
            headers: headers,
            body: `{
                "nombre de usuario":"${user}"
            }`
        })
            .then(response => response.json())
            .then(usuario => {
                localStorage.setItem('usuarioAModificar', user)
                localStorage.setItem('tipo', tipo)

                document.getElementById('nombre').value = usuario.nombre
                document.getElementById('apellido').value = usuario.apellido                
                document.getElementById('usuario').value = usuario['nombre de usuario']
                document.getElementById('password').value = usuario.password

                var nac = document.getElementById('contenedor-fecha')
                nac.parentNode.removeChild(nac)                
                var tel = document.getElementById('contenedor-telefono')
                tel.parentNode.removeChild(tel)
                var esp = document.getElementById('esp-container')
                esp.parentNode.removeChild(esp)
                var genero = document.getElementById('contenedor-sexo')
                genero.parentNode.removeChild(genero)
            })
    }
}

function modificarUsuario() {
    let user = localStorage.getItem('usuarioAModificar')
    let tipo = localStorage.getItem('tipo')

    if (tipo == 'paciente' || tipo == 'enfermera') {
        if (nombre == " " || apellido == " " || nacimiento == " " || usuario == " " || password == " ") {
            alert('Faltan datos por ingresar')
        } else {
            let nombre = document.getElementById('nombre').value
            let apellido = document.getElementById('apellido').value
            let nacimiento = document.getElementById('nacimiento').value
            let usuario = document.getElementById('usuario').value
            let password = document.getElementById('password').value
            let telefono = document.getElementById('telefono').value
            let m = document.getElementById('masculino')
            let f = document.getElementById('femenino')
            let sexo
    
            if (m.checked == true) {
                sexo = 'M'
            } else if (f.checked == true) {
                sexo = 'F'
            }

            fetch('http://localhost:4041/modificar', {
                method: 'POST',
                headers: headers,
                body: `{
                    "usuario":"${user}",
                    "nombre":"${nombre}",
                    "apellido":"${apellido}",
                    "fecha":"${nacimiento}",
                    "sexo":"${sexo}",
                    "nombre de usuario":"${usuario}",
                    "password":"${password}",
                    "telefono":"${telefono}"
                }`,
            })
                .then(response => response.json())
                .then(res => {
                    if (res == 'datos modificados') {
                        localStorage.setItem('nombreUsuario', usuario)
                        alert('Se han modificado los datos del usuario')
                    } else {
                        alert('El nombre de usuario ya existe')
                    }
                })
        }

    } else if (tipo == 'doctor') {
        let nombre = document.getElementById('nombre').value
        let apellido = document.getElementById('apellido').value
        let nacimiento = document.getElementById('nacimiento').value
        let usuario = document.getElementById('usuario').value
        let password = document.getElementById('password').value
        let telefono = document.getElementById('telefono').value
        let m = document.getElementById('masculino')
        let f = document.getElementById('femenino')
        let especialidad = document.getElementById('especialidad').value
        let sexo
    
        if (m.checked == true) {
            sexo = 'M'
        } else if (f.checked == true) {
            sexo = 'F'
        }

        if (nombre == " " || apellido == " " || nacimiento == " " || usuario == " " || password == " "|| especialidad == " ") {
            alert('Faltan datos por ingresar')
        } else {
            fetch('http://localhost:4041/modificar', {
                method: 'POST',
                headers: headers,
                body: `{
                    "usuario":"${user}",
                    "nombre":"${nombre}",
                    "apellido":"${apellido}",
                    "fecha":"${nacimiento}",
                    "sexo":"${sexo}",
                    "nombre de usuario":"${usuario}",
                    "password":"${password}",
                    "especialidad":"${especialidad}",
                    "telefono":"${telefono}"
                }`,
            })
                .then(response => response.json())
                .then(res => {
                    if (res == 'datos modificados') {
                        localStorage.setItem('nombreUsuario', usuario)
                        alert('Se han modificado los datos del usuario')
                    } else {
                        alert('El nombre de usuario ya existe')
                    }
                })
        }
    } else if (tipo == 'administrador') {
        let nombre = document.getElementById('nombre').value
        let apellido = document.getElementById('apellido').value
        let usuario = document.getElementById('usuario').value
        let password = document.getElementById('password').value

        fetch('http://localhost:4041/modificar', {
            method: 'POST',
            headers: headers,
            body: `{
                "usuario":"${user}",
                "nombre":"${nombre}",
                "apellido":"${apellido}",
                "nombre de usuario":"${usuario}",
                "password":"${password}"
            }`,
        })
            .then(response => response.json())
            .then(res => {
                if (res == 'datos modificados') {
                    localStorage.setItem('nombreUsuario', usuario)
                    alert('Se han modificado los datos del usuario')
                } else {
                    alert('El nombre de usuario ya existe')
                }
            })
    }
}

function modificarMedicamento() {
    let medicamento = localStorage.getItem('medicamento')
    let nombre = document.getElementById('nombre').value
    let precio = document.getElementById('precio').value
    let descripcion = document.getElementById('descripcion').value
    let cantidad = document.getElementById('cantidad').value

    fetch('http://localhost:4041/modificar-medicamento/modificar', {
        method: 'POST',
        headers: headers,
        body: `{
            "medicamento":"${medicamento}",
            "nombre":"${nombre}",
            "precio":"${precio}",
            "descripcion":"${descripcion}",
            "cantidad":"${cantidad}"
        }`
    })
        .then(response => response.json())
        .then(res =>{
            if (res == 'datos modificados') {
                alert('Se han modificado los datos del medicamento')
            } else {
                alert('No se ha podido modificar')
            }
        })
}

function cita() {
    let user = localStorage.getItem('nombreUsuario');
    localStorage.setItem('usuarioSolicitando', user)
    console.log(user)
    window.location.replace("http://localhost:4041/solicitar-cita")
}

function solicitarCita() {
    let user = localStorage.getItem('usuarioSolicitando')
    let fecha = document.getElementById('fecha-cita').value
    let hora = document.getElementById('hora-cita').value
    let motivo = document.getElementById('motivo').value
    console.log(user+" "+fecha+" "+hora+" "+motivo)
    fetch ('http://localhost:4041/solicitar-cita', {
        method: 'POST',
        headers: headers,
        body: `{
            "nombre de usuario":"${user}",
            "fecha":"${fecha}",
            "hora":"${hora}",
            "motivo":"${motivo}",
            "aceptada":"no",
            "doctor":" ",
            "completada":"no",
        }`,
    })
        .then(response => response.json())
        .then(res => {
            console.log(res)
            if (res == 'cita agregada') {
                alert('La cita ha sido agregada con exito.')
            } else if (res == 'cita pendiente/aceptada') {
                alert('Ya tiene una cita pendiente/aceptada')
            }
        })
}

function cargarCitas() {
    
}
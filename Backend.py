from flask import Flask, request, jsonify, url_for, redirect
from flask_cors import CORS
import json

datos_pacientes = []
datos_doctores = []
datos_enfermeros = []
nombres_usuarios = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify('Proyecto 2')

@app.route('/registrodoctores', methods=['POST'])
def registro_doctores():
    data = request.get_json(force=True)
    if not datos_doctores and not datos_enfermeros and not datos_pacientes:
        datos_doctores.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_doctores)
        return jsonify({"mensaje":"datos ingresados"})

    if data["nombre de usuario"] in nombres_usuarios:
        return jsonify({"error":"El nombre de usuario ya existe"})
    else:
        datos_doctores.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_doctores)
        return jsonify({"mensaje":"datos ingresados"})
    return jsonify({"mensaje":"El nombre de usuario ya existe"})

@app.route('/registropacientes', methods=['POST'])
def registro_pacientes():
    data = request.get_json(force=True)
    if not datos_doctores and not datos_enfermeros and not datos_pacientes:
        datos_pacientes.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_pacientes)
        print(nombres_usuarios)
        return jsonify({"mensaje":"datos ingresados"})

    if data["nombre de usuario"] in nombres_usuarios:
        return jsonify({"error":"El nombre de usuario ya existe"})
    else:
        datos_pacientes.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_pacientes)
        return jsonify({"mensaje":"datos ingresados"})
    return jsonify({"mensaje":"El nombre de usuario ya existe"})

@app.route('/registroenfermeros', methods=['POST'])
def registro_enfermeros():
    data = request.get_json(force=True)
    if not datos_doctores and not datos_enfermeros and not datos_pacientes:
        datos_enfermeros.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_enfermeros)
        return jsonify({"mensaje":"datos ingresados"})

    if data["nombre de usuario"] in nombres_usuarios:
        return jsonify({"error":"El nombre de usuario ya existe"})
    else:
        datos_enfermeros.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_enfermeros)
        return jsonify({"mensaje":"datos ingresados"})
    return jsonify({"mensaje":"El nombre de usuario ya existe"})

@app.route('/datospacientes')
def pacientes():
    return jsonify({"usuarios": datos_pacientes, "titulo": "Lista de pacientes"})

@app.route('/datosdoctores')
def doctores():
    return jsonify({"usuarios": datos_doctores, "titulo":"Lista de doctores"})

@app.route('/datosenfermeros')
def enfermeros():
    return jsonify({"usuarios": datos_enfermeros, "titulo":"Lista de enfermeros"})

@app.route('/login', methods = ['POST'])
def login():
    usuario = request.get_json(force=True)
    for i in range(len(datos_pacientes)):
        if usuario["usuario"] == datos_pacientes[i]["nombre de usuario"] and usuario["contraseña"] == datos_pacientes[i]["password"]:
            return jsonify({"mensaje":"Bienvenido "+datos_pacientes[i]["nombre"]+" "+datos_pacientes[i]["apellido"], "datos del usuario":datos_pacientes[i]})

    for i in range(len(datos_doctores)):
        if usuario["usuario"] == datos_doctores[i]["nombre de usuario"] and usuario["contraseña"] == datos_doctores[i]["password"]:
            return jsonify({"mensaje":"Bienvenido Dr. "+datos_doctores[i]["nombre"]+" "+datos_doctores[i]["apellido"], "datos del usuario":datos_doctores[i]})

    for i in range(len(datos_enfermeros)):
        if usuario["usuario"] == datos_enfermeros[i]["nombre de usuario"] and usuario["contraseña"] == datos_enfermeros[i]["password"]:
            return jsonify({"mensaje":"Bienvenido "+datos_enfermeros[i]["nombre"]+" "+datos_enfermeros[i]["apellido"], "datos del usuario":datos_enfermeros[i]})
    return jsonify({"mensaje":"Usuario no encontrado"})

@app.route('/datospacientes/<string:usuarios_nombredeusuario>', methods=['PUT'])
def mod_paciente(usuarios_nombredeusuario):
    usuario = [usuarios for usuarios in datos_pacientes if usuarios['nombre de usuario'] == usuarios_nombredeusuario]
    data = request.get_json(force=True)
    if data['nombre de usuario'] in nombres_usuarios:
        return jsonify({"mensaje":"El nombre de usuario ya existe"})
    else :
        if (len(usuario) > 0):
            usuario[0]['nombre'] = data['nombre']
            usuario[0]['apellido'] = data['apellido']
            usuario[0]['fecha de nacimiento'] = data['fecha de nacimiento']
            usuario[0]['nombre de usuario'] = data['nombre de usuario']
            usuario[0]['password'] = data['contraseña']
            usuario[0]['telefono'] = data['telefono']
            return jsonify({"mensaje": "Datos Actualizados"})           
    return jsonify({"mensaje":"No se pudieron modificar los datos"})

@app.route('/datosdoctores/<string:usuarios_nombredeusuario>', methods=['PUT'])
def mod_doctor(usuarios_nombredeusuario):
    usuario = [usuarios for usuarios in datos_doctores if usuarios['nombre de usuario'] == usuarios_nombredeusuario]
    data = request.get_json(force=True)
    if data['nombre de usuario'] in nombres_usuarios:
        return jsonify({"mensaje":"El nombre de usuario ya existe"})
    else :
        if (len(usuario) > 0):
            usuario[0]['nombre'] = data['nombre']
            usuario[0]['apellido'] = data['apellido']
            usuario[0]['fecha de nacimiento'] = data['fecha de nacimiento']
            usuario[0]['nombre de usuario'] = data['nombre de usuario']
            usuario[0]['password'] = data['contraseña']
            usuario[0]['telefono'] = data['telefono']
            return jsonify({"mensaje": "Datos Actualizados"})           
    return jsonify({"mensaje":"No se pudieron modificar los datos"})

@app.route('/datosenfermeros/<string:usuarios_nombredeusuario>', methods=['PUT'])
def mod_enfermero(usuarios_nombredeusuario):
    usuario = [usuarios for usuarios in datos_enfermeros if usuarios['nombre de usuario'] == usuarios_nombredeusuario]
    data = request.get_json(force=True)
    if data['nombre de usuario'] in nombres_usuarios:
        return jsonify({"mensaje":"El nombre de usuario ya existe"})
    else :
        if (len(usuario) > 0):
            usuario[0]['nombre'] = data['nombre']
            usuario[0]['apellido'] = data['apellido']
            usuario[0]['fecha de nacimiento'] = data['fecha de nacimiento']
            usuario[0]['nombre de usuario'] = data['nombre de usuario']
            usuario[0]['password'] = data['contraseña']
            usuario[0]['telefono'] = data['telefono']
            return jsonify({"mensaje": "Datos Actualizados"})           
    return jsonify({"mensaje":"No se pudieron modificar los datos"})

@app.route('/eliminarusuario', methods=['DELETE'])
def eliminarUsuario():
    data = request.get_json(force=True)
    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify({"mensaje":"Usuario no encontrado."})
    else:
        for i in range(len(datos_enfermeros)):
            if data['nombre de usuario'] == datos_enfermeros[i]['nombre de usuario'] and data['nombre de usuario'] == nombres_usuarios[i]:
                del datos_enfermeros[i], nombres_usuarios[i]
            return jsonify({"mensaje":"Usuario eliminado"})  
    
    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify({"mensaje":"Usuario no encontrado."})
    else:
        for i in range(len(datos_pacientes)):
            if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario'] and data['nombre de usuario'] == nombres_usuarios[i]:
                del datos_pacientes[i], nombres_usuarios[i]
            return jsonify({"mensaje":"Usuario eliminado"}) 

    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify({"mensaje":"Usuario no encontrado."})
    else:
        for i in range(len(datos_doctores)):
            if data['nombre de usuario'] == datos_doctores[i]['nombre de usuario'] and data['nombre de usuario'] == nombres_usuarios[i]:
                del datos_doctores[i], nombres_usuarios[i]
            return jsonify({"mensaje":"Usuario eliminado"}) 
    return jsonify({"mensaje":"No se ha podido eliminar al usuario"})

if __name__ == '__main__':
    app.run(debug=True,port=4041)
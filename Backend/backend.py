from flask import Flask, request, jsonify, url_for, redirect, make_response, render_template
from flask_cors import CORS
import json

datos_pacientes = []
datos_doctores = []
datos_enfermeros = []
datos_medicamentos = []
nombres_usuarios = []
nombres_medicamentos = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify("proyecto 2")

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
        return jsonify("datos ingresados")

    if data["nombre de usuario"] in nombres_usuarios:
        print("El nombre de usuario ya existe")
        return jsonify("El nombre de usuario ya existe")
    else:
        datos_pacientes.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_pacientes)
        return jsonify("datos ingresados")
    return jsonify("No se pudo crear el usuario")

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

@app.route('/agregarmedicamentos', methods = ['POST'])
def agregar_medicamentos():
    data = request.get_json(force=True)
    datos_medicamentos.append(data)
    nombres_medicamentos.append(data['nombre'])
    print(datos_medicamentos)
    return jsonify({"mensaje":"datos ingresados"})

@app.route('/datospacientes')
def pacientes():
    return jsonify({"usuarios": datos_pacientes, "titulo": "Lista de pacientes"})

@app.route('/datosdoctores')
def doctores():
    return jsonify({"usuarios": datos_doctores, "titulo":"Lista de doctores"})

@app.route('/datosenfermeros')
def enfermeros():
    return jsonify({"usuarios": datos_enfermeros, "titulo":"Lista de enfermeros"})

@app.route('/datosmedicamentos')
def medicamentos():
    return jsonify({"medicamentos": datos_medicamentos, "titulo": "Lista de medicamentos"})

@app.route('/login', methods = ['POST'])
def login():
    usuario = request.get_json(force=True)
    for i in range(len(datos_pacientes)):
        if usuario["usuario"] == datos_pacientes[i]["nombre de usuario"] and usuario["password"] == datos_pacientes[i]["password"]:
            return jsonify("Credenciales correctas")

    for i in range(len(datos_doctores)):
        if usuario["usuario"] == datos_doctores[i]["nombre de usuario"] and usuario["contraseña"] == datos_doctores[i]["password"]:
            return jsonify("Credenciales correctas")

    for i in range(len(datos_enfermeros)):
        if usuario["usuario"] == datos_enfermeros[i]["nombre de usuario"] and usuario["contraseña"] == datos_enfermeros[i]["password"]:
            return jsonify("Credenciales correctas")
    return jsonify("Credenciales incorrectas")

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
            usuario[0]['password'] = data['password']
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
            usuario[0]['password'] = data['password']
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
            usuario[0]['password'] = data['password']
            usuario[0]['telefono'] = data['telefono']
            return jsonify({"mensaje": "Datos Actualizados"})           
    return jsonify({"mensaje":"No se pudieron modificar los datos"})

@app.route('/datosmedicamentos/<string:medicamentos_nombre>', methods=['PUT'])
def mod_medicamento(medicamentos_nombre):
    medicamento = [medicamentos for medicamentos in datos_medicamentos if medicamentos['nombre'] == medicamentos_nombre]
    data = request.get_json(force=True)

    if (len(medicamento) > 0):
        medicamento[0]['nombre'] = data['nombre']
        medicamento[0]['precio'] = data['precio']
        medicamento[0]['descripcion'] = data['descripcion']
        medicamento[0]['cantidad'] = data['cantidad']
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
               print(datos_enfermeros[i])
               del datos_enfermeros[i], nombres_usuarios[i]
            return jsonify({"mensaje":"Usuario eliminado"})  
    
    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify({"mensaje":"Usuario no encontrado."})
    else:
        for i in range(len(datos_pacientes)):
            if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario'] and data['nombre de usuario'] == nombres_usuarios[i]:
                print(datos_pacientes[i])
                del datos_pacientes[i], nombres_usuarios[i]
            return jsonify({"mensaje":"Usuario eliminado"}) 

    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify({"mensaje":"Usuario no encontrado."})
    else:
        for i in range(len(datos_doctores)):
            if data['nombre de usuario'] == datos_doctores[i]['nombre de usuario'] and data['nombre de usuario'] == nombres_usuarios[i]:
               print(datos_doctores[i])
               del datos_doctores[i], nombres_usuarios[i]
            return jsonify({"mensaje":"Usuario eliminado"}) 
    return jsonify({"mensaje":"No se ha podido eliminar al usuario"})

@app.route('/eliminarmedicamento', methods=['DELETE'])
def eliminarMedicamento():
    data = request.get_json(force=True)
    if data['nombre'] not in nombres_medicamentos:
        return jsonify({"mensaje":"Medicamento no encontrado."})
    else:
        for i in range(len(datos_medicamentos)):
            if data['nombre'] == datos_medicamentos[i]['nombre'] and data['nombre'] == nombres_medicamentos[i]:
               print(datos_medicamentos[i])
               del datos_medicamentos[i], nombres_medicamentos[i]
            return jsonify({"mensaje":"Medicamento eliminado"})  
    return jsonify({"mensaje":"No se ha podido eliminar el medicamento"})

if __name__ == '__main__':
    app.run("0.0.0.0",port=4041)
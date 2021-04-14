from flask import Flask, request, jsonify, url_for, redirect
from flask_cors import CORS
import json

datos_pacientes = []
datos_doctores = []
datos_enfermeros = []
nombres_usuarios = []
existe = True

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
        print(nombres_usuarios)
        return jsonify({"mensaje":"datos ingresados"})

    if data["nombre de usuario"] in nombres_usuarios:
        print("Nombre de usuario existente")
    else:
        existe=False
        datos_doctores.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_doctores)
        print(nombres_usuarios)
        print(existe)
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
        print("Nombre de usuario existente")
    else:
        existe = False
        print(existe)
        datos_pacientes.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_pacientes)
        print(nombres_usuarios)
        return jsonify({"mensaje":"datos ingresados"})
    return jsonify({"mensaje":"El nombre de usuario ya existe"})

@app.route('/registroenfermeros', methods=['POST'])
def registro_enfermeros():
    data = request.get_json(force=True)
    if not datos_doctores and not datos_enfermeros and not datos_pacientes:
        datos_enfermeros.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_enfermeros)
        print(nombres_usuarios)
        return jsonify({"mensaje":"datos ingresados"})

    if data["nombre de usuario"] in nombres_usuarios:
        print("Nombre de usuario existente")
    else:
        existe = False
        print(existe)
        datos_enfermeros.append(data)
        nombres_usuarios.append(data["nombre de usuario"])
        print(datos_enfermeros)
        print(nombres_usuarios)
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
    return jsonify({"mensaje":"Usuario no encontrado"})

if __name__ == '__main__':
    app.run(debug=True,port=4041)
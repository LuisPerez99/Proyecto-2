from flask import Flask, request, jsonify, url_for, redirect
from flask_cors import CORS
import json

datos_pacientes = []
datos_doctores = []
datos_enfermeras = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify('Proyecto 2')

@app.route('/creardatos', methods=['POST'])
def asignarnombres():
    data = request.get_json(force=True)
    datos_pacientes.append(data)
    print(datos_pacientes)
    return jsonify("ingresado")

@app.route('/datos')
def obtenernombres():
    return jsonify({"usuarios": datos_pacientes, "titulo": "Lista de usuarios"})

@app.route('/login', methods = ['POST'])
def login():
    usuario = request.get_json(force=True)
    for i in range(len(datos_pacientes)):
        if usuario["usuario"] == datos_pacientes[i]["nombre de usuario"] and usuario["contraseña"] == datos_pacientes[i]["password"]:
            return jsonify({"mensaje":"Bienvenido "+datos_pacientes[i]["nombre"]+" "+datos_pacientes[i]["apellido"], "datos del usuario":datos_pacientes[i]})
    return jsonify({"mensaje":"Usuario no encontrado"})

if __name__ == '__main__':
    app.run(debug=True,port=4041)
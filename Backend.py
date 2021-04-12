from flask import Flask, request, jsonify, url_for, redirect
from flask_cors import CORS
import json

datos_usuarios = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify('Proyecto 2')

@app.route('/creardatos', methods=['POST'])
def asignarnombres():
    data = request.get_json(force=True)
    datos_usuarios.append(data)
    print(datos_usuarios)
    return jsonify("ingresado")

@app.route('/datos')
def obtenernombres():
    return jsonify({"usuarios": datos_usuarios, "titulo": "Lista de usuarios"})

@app.route('/login', methods = ['POST'])
def login():
    usuario = request.get_json(force=True)
    for i in range(len(datos_usuarios)):
        if usuario["usuario"] == datos_usuarios[i]["nombre de usuario"] and usuario["contraseña"] == datos_usuarios[i]["password"]:
            return jsonify({"mensaje":"Bienvenido "+datos_usuarios[i]["nombre"]+" "+datos_usuarios[i]["apellido"], "datos del usuario":datos_usuarios[i]})
    return jsonify({"mensaje":"Usuario no encontrado"})

if __name__ == '__main__':
    app.run(debug=True,port=4041)
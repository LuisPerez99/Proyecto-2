from flask import Flask,request,jsonify
from flask_cors import CORS
import json

nombre = []
apellido = []
nacimiento = []
genero = []
usuario = []
password = []
telefono = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify('Pagina')

@app.route('/creardatos', methods=['POST'])
def asignarnombres():
    data = request.get_json(force=True)
    nombres = data["nombre"]
    apellidos = data["apellido"]
    f_nacimiento = data["fecha de nacimiento"]
    sexo = data["sexo"]
    nombre_usuario = data["nombre de usuario"]
    contraseña = data["contraseña"]
    n_telefono = data["telefono"]
    nombre.append(nombres)
    apellido.append(apellidos)
    nacimiento.append(f_nacimiento)
    genero.append(sexo)
    usuario.append(nombre_usuario)
    password.append(contraseña)
    telefono.append(n_telefono)
    print(nombre)
    print(apellido)
    print(nacimiento)
    print(genero)
    print(usuario)
    print(password)
    print(telefono)
    return jsonify("ingresado")

@app.route('/obtenerdatos')
def obtenernombres():
    return jsonify(nombre,apellido,nacimiento,genero,usuario,password,telefono)

@app.route('/ingresar', methods=['POST'])
def ingresar():
    data = request.get_json(force=True)
    nombre_usuario = data["nombre de usuario"]
    password = data["contraseña"]
    for i in range (len(nombre)):
        if nombre_usuario == nombre[i] and contraseña == password[i]:
            return jsonify(nombre[i]+" ha ingresado")
    return jsonify("ingresado")

if __name__ == '__main__':
    app.run("0.0.0.0",port=4041)
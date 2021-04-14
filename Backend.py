from flask import Flask, request, jsonify, url_for, redirect
from flask_cors import CORS
import json

datos_pacientes = []
datos_doctores = []
datos_enfermeros = []

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
        print(datos_doctores)
        return jsonify({"mensaje":"datos ingresados"})

    if not datos_doctores and not datos_enfermeros:
        for i in range (len(datos_pacientes)):
             if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"]:
                 datos_doctores.append(data)
                 print(datos_doctores)
                 return jsonify({"mensaje":"datos ingresados"})
    if not datos_pacientes and not datos_enfermeros:
        for i in range (len(datos_doctores)):
             if data["nombre de usuario"] != datos_doctores[i]["nombre de usuario"]:
                 datos_doctores.append(data)
                 print(datos_doctores)
                 return jsonify({"mensaje":"datos ingresados"})
    if not datos_pacientes and not datos_doctores:
        for i in range (len(datos_enfermeros)):
             if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"]:
                 datos_doctores.append(data)
                 print(datos_doctores)
                 return jsonify({"mensaje":"datos ingresados"})

    if not datos_pacientes:
        for i in range (len(datos_enfermeros)):
            for j in range (len(datos_doctores)):
                if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"]:
                    datos_doctores.append(data)
                    print(datos_doctores)
                    return jsonify({"mensaje":"datos ingresados"})
    if not datos_doctores:
        for i in range (len(datos_enfermeros)):
            for j in range (len(datos_pacientes)):
                if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"] and data["nombre de usuario"] != datos_pacientes[j]["nombre de usuario"]:
                    datos_doctores.append(data)
                    print(datos_doctores)
                    return jsonify({"mensaje":"datos ingresados"})
    if not datos_enfermeros:
        for i in range (len(datos_pacientes)):
            for j in range (len(datos_doctores)):
                if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"]:
                    datos_doctores.append(data)
                    print(datos_doctores)
                    return jsonify({"mensaje":"datos ingresados"})

    for i in range (len(datos_pacientes)):
        for j in range (len(datos_doctores)):
            for k in range (len(datos_enfermeros)):
                if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"] and data["nombre de usuario"] != datos_enfermeros[k]["nombre de usuario"]:
                    datos_doctores.append(data)
                    print(datos_doctores)
                    return jsonify({"mensaje":"datos ingresados"})
    return jsonify({"mensaje":"El nombre de usuario ya existe"})

@app.route('/registropacientes', methods=['POST'])
def registro_pacientes():
    data = request.get_json(force=True)
    if not datos_doctores and not datos_enfermeros and not datos_pacientes:
        datos_pacientes.append(data)
        print(datos_pacientes)
        return jsonify({"mensaje":"datos ingresados"})

    if not datos_doctores and not datos_enfermeros:
        for i in range (len(datos_pacientes)):
             if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"]:
                 datos_pacientes.append(data)
                 print(datos_pacientes)
                 return jsonify({"mensaje":"datos ingresados"})
    if not datos_pacientes and not datos_enfermeros:
        for i in range (len(datos_doctores)):
             if data["nombre de usuario"] != datos_doctores[i]["nombre de usuario"]:
                 datos_pacientes.append(data)
                 print(datos_pacientes)
                 return jsonify({"mensaje":"datos ingresados"})
    if not datos_pacientes and not datos_doctores:
        for i in range (len(datos_enfermeros)):
             if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"]:
                 datos_pacientes.append(data)
                 print(datos_pacientes)
                 return jsonify({"mensaje":"datos ingresados"})

    if not datos_pacientes:
        for i in range (len(datos_enfermeros)):
            for j in range (len(datos_doctores)):
                if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"]:
                    datos_pacientes.append(data)
                    print(datos_pacientes)
                    return jsonify({"mensaje":"datos ingresados"})
    if not datos_doctores:
        for i in range (len(datos_enfermeros)):
            for j in range (len(datos_pacientes)):
                if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"] and data["nombre de usuario"] != datos_pacientes[j]["nombre de usuario"]:
                    datos_pacientes.append(data)
                    print(datos_pacientes)
                    return jsonify({"mensaje":"datos ingresados"})
    if not datos_enfermeros:
        for i in range (len(datos_pacientes)):
            for j in range (len(datos_doctores)):
                if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"]:
                    datos_pacientes.append(data)
                    print(datos_pacientes)
                    return jsonify({"mensaje":"datos ingresados"})

    for i in range (len(datos_pacientes)):
        for j in range (len(datos_doctores)):
            for k in range (len(datos_enfermeros)):
                if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"] and data["nombre de usuario"] != datos_enfermeros[k]["nombre de usuario"]:
                    datos_pacientes.append(data)
                    print(datos_pacientes)
                    return jsonify({"mensaje":"datos ingresados"})
    return jsonify({"mensaje":"El nombre de usuario ya existe"})

@app.route('/registroenfermeros', methods=['POST'])
def registro_enfermeros():
    data = request.get_json(force=True)
    if not datos_doctores and not datos_enfermeros and not datos_pacientes:
        datos_enfermeros.append(data)
        print(datos_enfermeros)
        return jsonify({"mensaje":"datos ingresados"})

    if not datos_doctores and not datos_enfermeros:
        for i in range (len(datos_pacientes)):
             if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"]:
                 datos_enfermeros.append(data)
                 print(datos_enfermeros)
                 return jsonify({"mensaje":"datos ingresados"})
    if not datos_pacientes and not datos_enfermeros:
        for i in range (len(datos_doctores)):
             if data["nombre de usuario"] != datos_doctores[i]["nombre de usuario"]:
                 datos_enfermeros.append(data)
                 print(datos_enfermeros)
                 return jsonify({"mensaje":"datos ingresados"})
    if not datos_pacientes and not datos_doctores:
        for i in range (len(datos_enfermeros)):
             if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"]:
                 datos_enfermeros.append(data)
                 print(datos_enfermeros)
                 return jsonify({"mensaje":"datos ingresados"})

    if not datos_pacientes:
        for i in range (len(datos_enfermeros)):
            for j in range (len(datos_doctores)):
                if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"]:
                    datos_enfermeros.append(data)
                    print(datos_enfermeros)
                    return jsonify({"mensaje":"datos ingresados"})
    if not datos_doctores:
        for i in range (len(datos_enfermeros)):
            for j in range (len(datos_pacientes)):
                if data["nombre de usuario"] != datos_enfermeros[i]["nombre de usuario"] and data["nombre de usuario"] != datos_pacientes[j]["nombre de usuario"]:
                    datos_enfermeros.append(data)
                    print(datos_enfermeros)
                    return jsonify({"mensaje":"datos ingresados"})
    if not datos_enfermeros:
        for i in range (len(datos_pacientes)):
            for j in range (len(datos_doctores)):
                if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"]:
                    datos_enfermeros.append(data)
                    print(datos_enfermeros)
                    return jsonify({"mensaje":"datos ingresados"})

    for i in range (len(datos_pacientes)):
        for j in range (len(datos_doctores)):
            for k in range (len(datos_enfermeros)):
                if data["nombre de usuario"] != datos_pacientes[i]["nombre de usuario"] and data["nombre de usuario"] != datos_doctores[j]["nombre de usuario"] and data["nombre de usuario"] != datos_enfermeros[k]["nombre de usuario"]:
                    datos_enfermeros.append(data)
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
    return jsonify({"mensaje":"Usuario no encontrado"})

if __name__ == '__main__':
    app.run(debug=True,port=4041)
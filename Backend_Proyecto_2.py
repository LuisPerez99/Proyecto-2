from flask import Flask,request,jsonify
from flask_cors import CORS
import json

lista_pacientes = []

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify('Pagina')

@app.route('/asignarnombres', methods=['POST'])
def asignarnombres():
    data = request.get_json(force=True)
    nombres = data["nombre"]
    lista_pacientes.append(nombres)
    print(lista_pacientes)
    return jsonify("ingresado")

@app.route('/obtenernombres')
def obtenernombres():
    return jsonify(lista_pacientes)

if __name__ == '__main__':
    app.run("0.0.0.0",port=4041)
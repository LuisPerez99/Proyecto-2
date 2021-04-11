from flask import Flask,request,jsonify,url_for,redirect
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

@app.route('/datos/<string:datos_usuario>')
def getNombre(datos_usuario):
    print(datos_usuario)
    nombreHallado = [usuarios for usuarios in datos_usuarios if usuarios['usuario'] == datos_usuario]
    if (len(nombreHallado) > 0):
        return jsonify({"datos": nombreHallado[0]})
    return jsonify({"mensaje":"Usuario no encontrado"})
    

@app.route('/success/<name>')
def success(name):
   return 'Bienvenido %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug=True,port=4041)
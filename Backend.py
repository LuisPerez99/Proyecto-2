from flask import Flask,request,jsonify,url_for,redirect
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
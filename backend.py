from flask import Flask, request, jsonify, url_for, redirect, make_response, render_template
from flask_cors import CORS
import json, csv, os

datos_pacientes = []
datos_doctores = []
datos_enfermeros = []
datos_medicamentos = []
nombres_usuarios = []
datos_admin = {
    "nombre":"Javier",
    "apellido":"Golon",
    "nombre de usuario":"admin",
    "password":"1234"
}

app = Flask(__name__)
app.config['FILE_UPLOADS'] = "static/file/uploads"
ALLOWED_EXTENSIONS = {'csv'}
CORS(app)

@app.route('/')
def index():
    return render_template('UHospital.html')

@app.route('/registropacientes', methods=['GET','POST'])
def registro_pacientes():
    if request.method == 'POST':
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
    
    if request.method == 'GET':
        return render_template('registro.html')
    return jsonify("No se pudo crear el usuario")

@app.route('/pacientes')
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

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.get_json(force=True)
        if usuario["usuario"] == datos_admin["nombre de usuario"] and usuario["password"] == datos_admin["password"]:
            return jsonify("administrador")

        for i in range(len(datos_pacientes)):
            if usuario["usuario"] == datos_pacientes[i]["nombre de usuario"] and usuario["password"] == datos_pacientes[i]["password"]:
                return jsonify("paciente")

        for i in range(len(datos_doctores)):
            if usuario["usuario"] == datos_doctores[i]["nombre de usuario"] and usuario["password"] == datos_doctores[i]["password"]:
                return jsonify("doctor")

        for i in range(len(datos_enfermeros)):
            if usuario["usuario"] == datos_enfermeros[i]["nombre de usuario"] and usuario["password"] == datos_enfermeros[i]["password"]:
                return jsonify("enfermero")
    
    if request.method == 'GET':
        return render_template('login.html')
    return jsonify("Credenciales incorrectas")

@app.route('/paciente', methods=['GET','POST'])
def paciente():
    if request.method == 'POST':
        data = request.get_json(force=True)
        for i in range (len(datos_pacientes)):
            if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario']:
                return jsonify(datos_pacientes[i])
    
    if (request.method == 'GET'):
        return render_template('modulo pacientes.html')
    return jsonify("Error, usuario no encontrado")

@app.route('/doctor', methods=['GET','POST'])
def doctor():
    if request.method == 'POST':
        data = request.get_json(force=True)
        for i in range (len(datos_doctores)):
            if data['nombre de usuario'] == datos_doctores[i]['nombre de usuario']:
                return jsonify(datos_doctores[i])
    
    if (request.method == 'GET'):
        return render_template('modulo doctores.html')
    return jsonify("Error, usuario no encontrado")

@app.route('/enfermero', methods=['GET','POST'])
def enfermero():
    if request.method == 'POST':
        data = request.get_json(force=True)
        for i in range (len(datos_enfermeros)):
            if data['nombre de usuario'] == datos_enfermeros[i]['nombre de usuario']:
                return jsonify(datos_enfermeros[i])
    
    if (request.method == 'GET'):
        return render_template('modulo enfermeros.html')
    return jsonify("Error, usuario no encontrado")

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        data = request.get_json(force=True)
        if data['nombre de usuario'] == datos_admin['nombre de usuario']:
            return jsonify(datos_admin)
    
    if (request.method == 'GET'):
        return render_template('modulo administrador.html')
    return jsonify("Error, usuario no encontrado")

@app.route('/admin/cargarpacientes', methods=['POST'])
def cargar_pacientes():
    if request.method == 'POST':
        if request.files:
            doc = request.files['pacientes']
            doc.save(os.path.join(app.config['FILE_UPLOADS'], doc.filename))
            print("archivo guardado")

            with open('static/file/uploads/pacientes.csv', 'r') as csv_file:
                lector = csv.reader(csv_file)
                next(lector)

                for line in lector:
                    datos_usuario = {
                        "nombre": line[0],
                        "apellido": line[1],
                        "fecha": line[2],
                        "sexo": line[3],
                        "nombre de usuario": line[4],
                        "password": line[5],
                        "telefono": line[6]
                        }
                    datos_pacientes.append(datos_usuario)
                    nombres_usuarios.append(datos_usuario['nombre de usuario'])
                print("Pacientes: "+str(datos_pacientes))
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin/cargardoctores', methods=['POST'])
def cargar_doctores():
    if request.method == 'POST':
        if request.files:
            doc = request.files['doctores']
            doc.save(os.path.join(app.config['FILE_UPLOADS'], doc.filename))
            print("archivo guardado")

            with open('static/file/uploads/doctores.csv', 'r') as csv_file:
                lector = csv.reader(csv_file)
                next(lector)

                for line in lector:
                    datos_usuario = {
                        "nombre": line[0],
                        "apellido": line[1],
                        "fecha": line[2],
                        "sexo": line[3],
                        "nombre de usuario": line[4],
                        "password": line[5],
                        "especialidad": line[6],
                        "telefono": line[7]
                        }
                    datos_doctores.append(datos_usuario)
                    nombres_usuarios.append(datos_usuario['nombre de usuario'])
                print("Doctores: "+str(datos_doctores))
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin/cargarenfermeros', methods=['POST'])
def cargar_enfermeros():
    if request.method == 'POST':
        if request.files:
            doc = request.files['enfermeras']
            doc.save(os.path.join(app.config['FILE_UPLOADS'], doc.filename))
            print("archivo guardado")

            with open('static/file/uploads/enfermeras.csv', 'r') as csv_file:
                lector = csv.reader(csv_file)
                next(lector)

                for line in lector:
                    datos_usuario = {
                        "nombre": line[0],
                        "apellido": line[1],
                        "fecha": line[2],
                        "sexo": line[3],
                        "nombre de usuario": line[4],
                        "password": line[5],
                        "telefono": line[6]
                        }
                    datos_enfermeros.append(datos_usuario)
                    nombres_usuarios.append(datos_usuario['nombre de usuario'])
                print("Enfermeras: "+str(datos_enfermeros))
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/admin/cargarmedicamentos', methods=['POST'])
def cargar_medicamentos():
    if request.method == 'POST':
        if request.files:
            doc = request.files['medicamentos']
            doc.save(os.path.join(app.config['FILE_UPLOADS'], doc.filename))
            print("archivo guardado")

            with open('static/file/uploads/medicamentos.csv', 'r') as csv_file:
                lector = csv.reader(csv_file)
                next(lector)

                for line in lector:
                    datos_medicamento = {
                        "nombre": line[0],
                        "precio": line[1],
                        "descripcion": line[2],
                        "cantidad": line[3],
                        }
                    datos_medicamentos.append(datos_medicamento)
                print("Medicamentos: "+str(datos_medicamentos))
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route('/modificarperfil', methods=['GET','POST'])
def mod_perfil():
    if request.method == 'POST':
        data = request.get_json(force=True)

        for i in range(len(datos_pacientes)):
            if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario']:
                datos_pacientes[i] = data
                print(datos_pacientes[i])
                return jsonify(datos_pacientes[i])
    
    if request.method == 'GET':
        return render_template('modificar perfil.html')
    return jsonify({"mensaje":"Error"})

@app.route('/modificarperfil/modificar', methods=['POST'])
def modificar():
    data = request.get_json(force=True)

    for i in range(len(datos_pacientes)):
        if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario']:
            datos_pacientes[i] = data
            print(datos_pacientes[i])
            return jsonify("modificado")
    return jsonify({"error":"no se pudo modificar la informacion"})

@app.route('/datos-pacientes')
def ver_pacientes():
    data = datos_pacientes
    return render_template('datos pacientes.html', data = json.dumps(data))

@app.route('/datos-doctores')
def ver_doctores():
    data = datos_doctores
    return render_template('datos doctores.html', data = json.dumps(data))

@app.route('/datos-enfermeras')
def ver_enfermeras():
    data = datos_enfermeros
    return render_template('datos enfermeros.html', data = json.dumps(data))

@app.route('/datos-medicamentos')
def ver_medicamentos():
    data = datos_medicamentos
    return render_template('datos medicamentos.html', data = json.dumps(data))

@app.route('/datos-pacientes/eliminarpaciente', methods=['POST'])
def eliminarPaciente():
    data = request.get_json(force=True)
    
    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify("Usuario no encontrado.")
    else:
        for i in range(len(datos_pacientes)):
            if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario']:
                print("Datos eliminados: "+str(datos_pacientes[i]))
                del datos_pacientes[i]

                for j in range(len(nombres_usuarios)):
                    if data['nombre de usuario'] == nombres_usuarios[j]:
                        del nombres_usuarios[j]
                        return jsonify("Usuario eliminado")
    return jsonify({"mensaje":"No se ha podido eliminar al usuario"})

@app.route('/datos-enfermeras/eliminarenfermera', methods=['POST'])
def eliminarEnfermera():
    data = request.get_json(force=True)

    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify("Usuario no encontrado.")
    else:
        for i in range(len(datos_enfermeros)):
            if data['nombre de usuario'] == datos_enfermeros[i]['nombre de usuario']:
                print("Datos eliminados: "+str(datos_enfermeros[i]))
                del datos_enfermeros[i]

                for j in range(len(nombres_usuarios)):
                    if data['nombre de usuario'] == nombres_usuarios[j]:
                        del nombres_usuarios[j]
                        return jsonify("Usuario eliminado") 
    return jsonify({"mensaje":"No se ha podido eliminar al usuario"})

@app.route('/datos-doctores/eliminardoctor', methods=['POST'])
def eliminarDoctor():
    data = request.get_json(force=True)

    if data['nombre de usuario'] not in nombres_usuarios:
        return jsonify("Usuario no encontrado.")
    else:
        for i in range(len(datos_doctores)):
            if data['nombre de usuario'] == datos_doctores[i]['nombre de usuario']:
                print("Datos eliminados: "+str(datos_doctores[i]))
                del datos_doctores[i]

                for j in range(len(nombres_usuarios)):
                    if data['nombre de usuario'] == nombres_usuarios[j]:
                        del nombres_usuarios[j]
                        return jsonify("Usuario eliminado")
    return jsonify({"mensaje":"No se ha podido eliminar al usuario"})

@app.route('/datos-medicamentos/eliminarmedicamento', methods=['POST'])
def eliminarMedicamento():
    data = request.get_json(force=True)

    for i in range(len(datos_medicamentos)):
        if data['nombre de usuario'] == datos_medicamentos[i]['nombre']:
            print(datos_medicamentos[i])
            del datos_medicamentos[i]
            return jsonify("Medicamento eliminado")  
    return jsonify({"mensaje":"No se ha podido eliminar el medicamento"})

@app.route('/ver-datos', methods = ['GET','POST'])
def ver_datos():
    if request.method == 'POST':
        data = request.get_json(force=True)

        for i in range(len(datos_pacientes)):
            if data['nombre de usuario'] == datos_pacientes[i]['nombre de usuario']:
                print(datos_pacientes[i])
                return jsonify(datos_pacientes[i])

        for i in range(len(datos_enfermeros)):
            if data['nombre de usuario'] == datos_enfermeros[i]['nombre de usuario']:
                print(datos_enfermeros[i])
                return jsonify(datos_enfermeros[i])

        for i in range(len(datos_doctores)):
            if data['nombre de usuario'] == datos_doctores[i]['nombre de usuario']:
                print(datos_doctores[i])
                return jsonify(datos_doctores[i])
    
    if request.method == 'GET':
        return render_template('ver datos.html')
    return jsonify({"error":"no se encontro al usuario"})

@app.route('/ver-medicamento', methods = ['GET','POST'])
def ver_medicamento():
    if request.method == 'POST':
        data = request.get_json(force=True)

        for i in range(len(datos_medicamentos)):
            if data['nombre'] == datos_medicamentos[i]['nombre']:
                print(datos_medicamentos[i])
                return jsonify(datos_medicamentos[i])

    if request.method == 'GET':
        return render_template('ver medicamento.html')
    return jsonify({"error":"no se encontro el medicamento"})

if __name__ == '__main__':
    app.run(debug=True,port=4041)
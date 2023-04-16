from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'saludos!'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username:
        return 'Bienvenido, {}!'.format(username)
    else:
        return 'Revise Datos!'
    

@app.route('/perfiles', methods=['POST'])
def perfil():
    nombrePerfil = request.form['nombrePerfil']
    palabras = request.form['palabras'].split(',')
    
    print(type(palabras))

    nueva_lista = []
    for elemento in palabras:
        if " " in elemento:
            palabras = elemento.split()
            for palabra in palabras:
                nueva_lista.append(palabra)
        else:
            nueva_lista.append(elemento)

    return nueva_lista


@app.route('/mensaje', methods=['POST'])
def perfil():
    mensaje = request.form['mensaje']
    
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, port=5000)


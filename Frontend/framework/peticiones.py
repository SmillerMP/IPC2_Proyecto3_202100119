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


if __name__ == '__main__':
    app.run(debug=True, port=5000)


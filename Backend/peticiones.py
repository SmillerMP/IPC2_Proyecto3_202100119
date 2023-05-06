from flask import Flask, request, jsonify, make_response
import xml.etree.ElementTree as ET
from flask_cors import CORS
from leerXML import *
from mensaje import *

from leerXML import convertirXMLData

app = Flask(__name__)
CORS(app)

@app.route('/BaseDatos', methods=['POST'])
def postEntradaSalida():
    xmlEntrada  = request.data
    carga = BaseDatos(xmlEntrada)
    carga._leerXML()

    #respuesta = Respuesta1(carga.pefilesCreados, carga.perfilesActualizados, carga.nuevasDescartadas)
    
    #Creacion de la respuesta XML
    raiz = ET.Element('respuesta')
    perfilesNuevos = ET.SubElement(raiz, 'perfilesNuevos')
    perfilesNuevos.text = f'Se han creados {carga.pefilesCreados} perfiles nuevos'

    perfilesExistentes = ET.SubElement(raiz, 'perfilesExistentes')
    perfilesExistentes.text = f'Se han actualizado {carga.perfilesActualizados} perfiles'

    descartadas = ET.SubElement(raiz, 'descartadas')
    descartadas.text = f'Se han creado {carga.nuevasDescartadas} nuevas palabras a descartar'

    # Crea la estructura de xml para luego enviarla
    xml_respuesta = ET.tostring(raiz, encoding='utf-8', method='xml', xml_declaration=True)
    respuesta = make_response(xml_respuesta)
    respuesta.headers.set('Content-Type', 'application/xml')

    return respuesta




@app.route('/Mensaje', methods=['POST'])
def MensajeExaminar():
    mensajeEntrada  = request.data
    
    mensajeEntrante = Mensaje(mensajeEntrada)
    mensajeEntrante._leerMensaje()

    raiz = ET.Element('respuesta')
    perfilesNuevos = ET.SubElement(raiz, 'usuarios')
    perfilesNuevos.text = f'Se procesaron mensajes para {len(mensajeEntrante.listaUsuarios)} usuarios distintos'

    perfilesExistentes = ET.SubElement(raiz, 'mensaje')
    perfilesExistentes.text = f'Se procesaron {mensajeEntrante.contadorMensajes} mensajes en total'

    # Crea la estructura de xml para luego enviarla
    xml_respuesta = ET.tostring(raiz, encoding='utf-8', method='xml', xml_declaration=True)
    respuesta = make_response(xml_respuesta)
    respuesta.headers.set('Content-Type', 'application/xml')
    
    return respuesta


@app.route('/Filtrar', methods=['GET'])
def filtrarUsuarios():
    
    with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
        datos = json.load(archivo_json)
        
    return jsonify(datos)




@app.route('/datos-xml')
def obtener_datos_xml():
    # Crear un árbol XML
    root = ET.Element('datos')
    nombre = ET.SubElement(root, 'nombre')
    nombre.text = 'Juan Muñoz'
    edad = ET.SubElement(root, 'edad')
    edad.text = '25'

    # Convertir el árbol XML en una cadena
    xml_string = ET.tostring(root, encoding='utf-8', method='xml', xml_declaration=True)

    # Crear una respuesta HTTP con el contenido XML
    response = make_response(xml_string)
    response.headers.set('Content-Type', 'application/xml')
    return response


@app.route('/Reset', methods=['POST'])
def resetear():
    archivo = {
        "Perfiles": {},
        "Descartadas": []
    }
    with open('Backend\Data\DataBase.json', 'w', encoding='utf-8') as carga:
        json.dump(archivo, carga, indent=4, ensure_ascii=False) 
    convertirXMLData()
    

    archivo = {}
    with open('Backend\Data\MensajesDataBase.json', 'w', encoding='utf-8') as carga:
        json.dump(archivo, carga, indent=4, ensure_ascii=False)
    
    with open('Backend\Data\MensajesDataBase.xml', 'w', encoding='utf-8') as xml:
        xml.write('<?xml version="1.0" ?>')

    return jsonify({"Mensaje": "Reseteado"})


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username:
        return 'Bienvenido, {}!'.format(username)
    else:
        return 'Revise Datos!'
    

# @app.route('/perfiles', methods=['POST'])
# def perfil():
#     nombrePerfil = request.form['nombrePerfil']
#     palabras = request.form['palabras'].split(',')
    
#     print(type(palabras))

#     nueva_lista = []
#     for elemento in palabras:
#         if " " in elemento:
#             palabras = elemento.split()
#             for palabra in palabras:
#                 nueva_lista.append(palabra)
#         else:
#             nueva_lista.append(elemento)

#     return nueva_lista


@app.route('/mensaje', methods=['POST'])
def perfil():
    mensaje = request.form['mensaje']
    
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, port=5000)


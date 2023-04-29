from flask import Flask, request, jsonify, make_response
import xml.etree.ElementTree as ET
from leerXML import *



app = Flask(__name__)

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
    perfilesExistentes.text = f'Se han actualizado {carga.perfilesActualizados} perfiles nuevos'

    descartadas = ET.SubElement(raiz, 'descartadas')
    descartadas.text = f'Se han creado {carga.nuevasDescartadas} nuevas palabras a descartar'

    # Crea la estructura de xml para luego enviarla
    xml_respuesta = ET.tostring(raiz, encoding='utf-8', method='xml', xml_declaration=True)
    respuesta = make_response(xml_respuesta)
    respuesta.headers.set('Content-Type', 'application/xml')

    return respuesta




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


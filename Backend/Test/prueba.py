import xml.etree.ElementTree as ET
import re
from json2xml import json2xml
import json

ruta = 'D:\\Samuellllll\\Documentos\\Universidad\\CUARTO SEMESTRE\\IPC 2\\Proyectos IPC2\\Proyecto 3\\Backend\\Test\\mensaje.xml'

#Lee el mensaje xml en busqeuda de sus elementos
tree = ET.parse(ruta)
raiz = tree.getroot()

for listaMensaje in raiz.findall(".//mensaje"): 
    mensaje = listaMensaje.text
    mensaje = mensaje.lower()
    
    print(mensaje)

    opcion = 1
    usuario = ''
    textoAnalizar = ''
    ciudad = ''
    FechaHora = ''

    while opcion != 5:
        if opcion == 1:
            match = re.search(r'lugar y fecha', mensaje)
            inicio = match.start()
            final = match.end()
            print(mensaje[15-1])

            print(f'incio: {inicio}, final:{final}')

            index = final+1
            while mensaje[index] != ',':
                ciudad += mensaje[index]
                index +=1

            ciudad = ciudad.strip()
            print(ciudad)

            index +=1
            while mensaje[index] != '\n':
                FechaHora += mensaje[index]
                index +=1

            FechaHora = FechaHora.strip()
            print(FechaHora)

            # if 'lugar y fecha:' in mensaje:
            #     print("encontrado")
            opcion = 2

        elif opcion == 2:
            match = re.search(r'usuario', mensaje)
            inicio = match.start()
            final = match.end()

            print(f'incio: {inicio}, final:{final}')
            index = final + 1
            while mensaje[index] != '\n':
                usuario += mensaje[index]
                index += 1

            usuario = usuario.replace(" ", '')
            print(usuario)

            opcion = 3
        elif opcion == 3:
            match = re.search(r'red social', mensaje)
            inicio = match.start()
            final = match.end()
            print(f'incio: {inicio}, final:{final}')

            match = re.search(r'chapinchat', mensaje)
            inicio = match.start()
            final = match.end()
            print(f'incio: {inicio}, final:{final}')

            linaCorrespondiente = int(final)
            opcion += 1
        elif opcion == 4:
            try:
                while mensaje[linaCorrespondiente] != '':
                    textoAnalizar += mensaje[linaCorrespondiente]
                    linaCorrespondiente += 1
            except:
                pass
            
            print(textoAnalizar)
            opcion = 5





def _convertirXML():
        with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
            data = json.load(archivo_json)

        xml_data = json2xml.Json2xml(data).to_xml()

        with open('Backend\Data\MensajesDataBase.xml', 'w', encoding='utf-8') as archivo_xml:
            archivo_xml.write(xml_data)

_convertirXML()
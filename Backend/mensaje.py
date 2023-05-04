import xml.etree.ElementTree as ET
import re
import json
from json2xml import json2xml

class Mensaje:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.ciudad = ''
        self.fechayhora = ''
        self.usuario = ''


    def _leerMensaje(self):
        raiz = ET.fromstring(self.mensaje)

        #Lee el mensaje xml en busqeuda de sus elementos
        for listaMensaje in raiz.findall(".//mensaje"): 
            mensaje = listaMensaje.text
            mensaje = mensaje.lower()
            self._analizar(mensaje)




    def _analizar(self, mensaje):

        opcion = 1
        usuario = ''
        textoAnalizar = ''
        ciudad = ''
        FechaHora = ''

        while opcion != 5:
            if opcion == 1:
                # Busca el subtitulo lugar y fecha
                match = re.search(r'lugar y fecha', mensaje)
                inicio = match.start()
                final = match.end()

                #print(f'incio: {inicio}, final:{final}')

                index = final+1
                while mensaje[index] != ',':
                    ciudad += mensaje[index]
                    index +=1

                ciudad = ciudad.strip()
                self.ciudad = ciudad
                #print(ciudad)

                index +=1
                while mensaje[index] != '\n':
                    FechaHora += mensaje[index]
                    index +=1

                FechaHora = FechaHora.strip()
                self.fechayhora = FechaHora
                #print(FechaHora)

                # if 'lugar y fecha:' in mensaje:
                #     print("encontrado")
                opcion = 2

            elif opcion == 2:
                # Busca el subtitulo usuario
                match = re.search(r'usuario', mensaje)
                inicio = match.start()
                final = match.end()

                #print(f'incio: {inicio}, final:{final}')
                index = final + 1
                while mensaje[index] != '\n':
                    usuario += mensaje[index]
                    index += 1

                usuario = usuario.replace(" ", '')
                self.usuario = usuario
                #print(usuario)

                opcion = 3
            elif opcion == 3:
                # Busca el sub titulo red social
                match = re.search(r'red social', mensaje)
                inicio = match.start()
                final = match.end()
                #print(f'incio: {inicio}, final:{final}')

                # Busca el nommbre de la red social
                match = re.search(r'chapinchat', mensaje)
                inicio = match.start()
                final = match.end()
                #print(f'incio: {inicio}, final:{final}')

                linaCorrespondiente = int(final)
                opcion += 1
            elif opcion == 4:
                # Crea una variable con todo el mensaje que se desea analizar
                try:
                    while mensaje[linaCorrespondiente] != '':
                        # Suma la variable del mensaje
                        textoAnalizar += mensaje[linaCorrespondiente]
                        linaCorrespondiente += 1
                except:
                    pass
                
                #print(textoAnalizar)
                # Llama la funcion que analiza el mensaje
                self._comparar(textoAnalizar)
                opcion = 5

        
    def _comparar(self, mensaje):
        signosExcluidos = [',', '.', ';', ':']
        texto = ''
        listaAnalizar = []

        # Manda a traer todas las palabras excluidas y las presenta en unalista
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
        palabrasExcluidad = datos["Descartadas"]

        
        #print(type(mensaje))
        
        # Remplzada los espacios vacios y saltos de linea por el #
        for letra in mensaje:
            letra = letra.replace(" ", "#").replace("\n", "#")

            # Eliminar los signos, como la coma, punto, 2 putos, etc
            for signo in signosExcluidos:
                letra = letra.replace(signo, "")
            
            # Suma en la variable texto cada una de las letras del mensaje, incluido los numerales
            texto += letra

        # Crea una lista separando los elementos apartir del numeral
        listaSucia = texto.split('#')
        # Comprueba que las palabras no sean vacias o sean numeros
        for palabra in listaSucia:
            if palabra != '':
                try:
                    prueba = float(palabra)
                except:
                    listaAnalizar.append(palabra)

        # Elimina todas las palabras excluidas de la base de datos en la lista a analizar
        for i in palabrasExcluidad:
            while i in listaAnalizar:
                listaAnalizar.pop(listaAnalizar.index(i))

        #print(listaAnalizar, len(listaAnalizar))
        
        # Comparacion de los perfiles en la base de datos con la lista limpia de palabras del mensaje
        elementosTotales = len(listaAnalizar)
        Perfiles = {}
        for perfil in datos["Perfiles"]:
            coincidencias = 0
            for palabrasClave in datos["Perfiles"][perfil]:
                for x in listaAnalizar:
                    if x == palabrasClave:
                        coincidencias += 1
            
            porsentaje = round(((coincidencias*100)/elementosTotales), 2)
            Perfiles[f'{perfil}'] = str(porsentaje) + '%'
        
        MensajesIndividual = {"FechayHora": self.fechayhora, "Perfiles": Perfiles}

        
        with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)

        
        lista_usuarios = datos.keys()
        if self.usuario in lista_usuarios:
            datos[f"{self.usuario}"]["Mensajes"].append(MensajesIndividual)
        else:
            datos[f"{self.usuario}"] = {"Mensajes": [MensajesIndividual]}
        
        with open('Backend\Data\MensajesDataBase.json', 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        convertirXMLMensajes()
            


        
                
        
def convertirXMLMensajes():
    with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
        data = json.load(archivo_json)

    xml_data = json2xml.Json2xml(data).to_xml()

    with open('Backend\Data\MensajesDataBase.xml', 'w', encoding='utf-8') as archivo_xml:
        archivo_xml.write(xml_data)
        

        



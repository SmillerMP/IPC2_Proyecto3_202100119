import xml.etree.ElementTree as ET
import re
import json

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
                match = re.search(r'lugar y fecha', mensaje)
                inicio = match.start()
                final = match.end()

                print(f'incio: {inicio}, final:{final}')

                index = final+1
                while mensaje[index] != ',':
                    ciudad += mensaje[index]
                    index +=1

                ciudad = ciudad.strip()
                self.ciudad = ciudad
                print(ciudad)

                index +=1
                while mensaje[index] != '\n':
                    FechaHora += mensaje[index]
                    index +=1

                FechaHora = FechaHora.strip()
                self.fechayhora = FechaHora
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
                self.usuario = usuario
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
                self._comparar(textoAnalizar)
                opcion = 5

        
    def _comparar(self, mensaje):
        signosExcluidos = [',', '.', ';', ':']
        texto = ''
        listaAnalizar = []
        
        print(type(mensaje))
        
        for letra in mensaje:
            letra = letra.replace(" ", "#").replace("\n", "#")

            for signo in signosExcluidos:
                letra = letra.replace(signo, "")

            texto += letra

        listaSucia = texto.split('#')
        for palabra in listaSucia:
            if palabra != '':
                try:
                    prueba = float(palabra)
                except:
                    listaAnalizar.append(palabra)

        print(listaAnalizar)
        
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
        
        elementosTotales = len(listaAnalizar)
        for perfil in datos["Perfiles"]:
            coincidencias = 0
            for palabrasClave in datos["Perfiles"][perfil]:
                for x in listaAnalizar:
                    if x == palabrasClave:
                        pass


        
                
        
        # with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
        #     datos = json.load(archivo_json)

        # # Buscar el perfil
        # perfiles = datos.get('Perfiles')
        # if perfiles != None:
        #     if NombrePerfil in perfiles:
        #         return True
        #     else:
        #         return False
        # else:
        #     return 'Vacio'
        

        



import xml.etree.ElementTree as ET
import re
import json

class Mensaje:
    def __init__(self, mensaje):
        self.mensaje = mensaje


    def _leerMensaje(self):
        raiz = ET.fromstring(self.mensaje)

        #Lee el mensaje xml en busqeuda de sus elementos
        for listaMensaje in raiz.findall(".//mensaje"): 
            mensaje = listaMensaje.text
            mensaje = mensaje.lower()
            self._analizar(mensaje)




    def _analizar(self, mensaje):

        # signosExcluidos = [',', '.', ';', ':']
        # texto = ''
        # listaAnalizar = []
        
        # print(type(mensaje))
        
        # for letra in mensaje:
        #     letra = letra.replace(" ", "#").replace("\n", "#")

        #     for signo in signosExcluidos:
        #         letra = letra.replace(signo, "")

        #     texto += letra

        # listaSucia = texto.split('#')
        # for palabra in listaSucia:
        #     if palabra != '':
        #         try:
        #             prueba = float(palabra)
        #         except:
        #             listaAnalizar.append(palabra)
                
        
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




        opcion = 1

        while opcion != 5:
            if opcion == 1:
                match = re.search(r'lugar y fecha:', mensaje)
                inicio = match.start()
                final = match.end()
                print(mensaje[15-1])

                print(f'incio: {inicio}, final:{final}')

                # if 'lugar y fecha:' in mensaje:
                #     print("encontrado")
                opcion = 2

            elif opcion == 2:
                match = re.search(r'usuario:', mensaje)
                inicio = match.start()
                final = match.end()

                print(f'incio: {inicio}, final:{final}')

                opcion = 3
            elif opcion == 3:
                match = re.search(r'red social:', mensaje)
                inicio = match.start()
                final = match.end()
                print(f'incio: {inicio}, final:{final}')

                match = re.search(r'chapinchat', mensaje)
                inicio = match.start()
                final = match.end()
                print(f'incio: {inicio}, final:{final}')
                print(mensaje[final-1])

                opcion = 5


        

        



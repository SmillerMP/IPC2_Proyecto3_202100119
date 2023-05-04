import xml.etree.ElementTree as ET
import json
from json2xml import json2xml


ruta = 'Backend//Test//entrada.xml'
class BaseDatos:
    def __init__(self, entrada):
        self.entrada = entrada
        self.pefilesCreados = 0
        self.perfilesActualizados = 0
        self.nuevasDescartadas = 0

    def _leerXML(self):

        # arbol = ET.parse(self.entrada)
        # raiz = arbol.getroot()

        raiz = ET.fromstring(self.entrada)

        # Busca en el xml, los perfiles
        for perfiles in raiz.findall(".//perfiles/perfil"):
            nombrePerfil = perfiles.find("nombre").text
            nombrePerfil = nombrePerfil.lower()
            
            if self._verificarPefil(nombrePerfil) == True:

                actualizado = False
                # Recorre las palbras clave de cada uno de los perfiles
                for PalabraClave in perfiles.findall("palabrasClave/palabra"):
                    palabra = PalabraClave.text
                    palabra = palabra.lower()
                    Simple_Compuesta, palabra = self._palbrasSimples(palabra)
                    if Simple_Compuesta == True:
                        if self._verificarPalabraClave(nombrePerfil, palabra) == False:
                            actualizado = True
                            self._agregarPalabraClave(nombrePerfil, palabra)
                    else:
                        for x in palabra:
                            if self._verificarPalabraClave(nombrePerfil, x) == False:
                                actualizado = True
                                self._agregarPalabraClave(nombrePerfil, x)
                
                # En caso de que se haya actualizado ese perfil, suma un contador
                if actualizado == True:
                    self.perfilesActualizados += 1
            

            elif self._verificarPefil(nombrePerfil) == False:
                self.pefilesCreados += 1
                
                self._agregarPerfil(nombrePerfil)

                for PalabraClave in perfiles.findall("palabrasClave/palabra"):
                    palabra = PalabraClave.text
                    palabra = palabra.lower()

                    Simple_Compuesta, palabra = self._palbrasSimples(palabra)
                    if Simple_Compuesta == True:
                        if self._verificarPalabraClave(nombrePerfil, palabra) == False:
                            self._agregarPalabraClave(nombrePerfil, palabra)
                    else:
                        for x in palabra:
                            if self._verificarPalabraClave(nombrePerfil, x) == False:
                                self._agregarPalabraClave(nombrePerfil, x)
                    
                    
        
        # Recorre las palabras clavez
        for descartadas in raiz.findall(".//descartadas/palabra"):
            palabra = descartadas.text
            palabra = palabra.lower()

            Simple_Compuesta, palabra = self._palbrasSimples(palabra)
            if Simple_Compuesta == True:
                self._verificarDescartadas(palabra)
            else:
                for x in palabra:
                    self._verificarDescartadas(x)

            self._verificarDescartadas(palabra)

        convertirXMLData()

    def _palbrasSimples(self, palabra):
        
        palabra = palabra.strip()
        palabra = palabra.split(' ')
        while '' in palabra:
            palabra.pop(palabra.index(''))
        #print(len(palabra), palabra)
        if len(palabra) == 1:
            return True, palabra[0]
        else:
            return False, palabra


    # Verifica que el perfil exista
    def _verificarPefil(self, NombrePerfil):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)

        # Buscar el perfil
        perfiles = datos.get('Perfiles')
        if perfiles != None:
            if NombrePerfil in perfiles:
                return True
            else:
                return False
        else:
            return 'Vacio'
        
        # En caso de que el perfil exista, retorna True, de lo contrario False

    
    # Verifica que la palabra clave exista
    def _verificarPalabraClave(self, NombrePerfil, palabraClave):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
    
    
        palabras = datos["Perfiles"][NombrePerfil]
        if palabraClave in palabras:
            return True
        else:
            return False

    
    # Agrea la palabra clave en base al perfil, y si ya fue comprobado que no existe
    def _agregarPalabraClave(self, perfil, palabra):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        datos["Perfiles"][perfil].append(palabra)

        with open('Backend\Data\DataBase.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)


    # Agrega el perfil en caso de que no exista
    def _agregarPerfil(self, perfil):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        datos["Perfiles"][perfil] = []

        with open('Backend\Data\DataBase.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    
    # Verifica y agrega las palabras descartadas
    def _verificarDescartadas(self, descartada):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
    
        palabrasDescartadas = datos["Descartadas"]
        if descartada in palabrasDescartadas:
            return True
        
        else:
            with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)

            datos["Descartadas"].append(descartada)
            self.nuevasDescartadas += 1

            with open('Backend\Data\DataBase.json', 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
    
    
def convertirXMLData():
    with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
        data = json.load(archivo_json)

    xml_data = json2xml.Json2xml(data).to_xml()

    with open('Backend\Data\DataBase.xml', 'w', encoding='utf-8') as archivo_xml:
        archivo_xml.write(xml_data)

        

# cargar = BaseDatos(ruta)
# cargar._leerXML()
# print(f"Crados: {cargar.pefilesCreados}, Actualizados: {cargar.perfilesActualizados}")

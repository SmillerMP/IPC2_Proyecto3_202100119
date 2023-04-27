import xml.etree.ElementTree as ET
import json

ruta = 'Backend//Test//entrada.xml'
class BaseDatos:
    def __init__(self, entrada):
        self.entrada = entrada
        self.pefilesCreados = 0
        self.perfilesActualizados = 0
        self.nuevasDescartadas = 0

    def _leerXML(self):

        arbol = ET.parse(self.entrada)
        raiz = arbol.getroot()

        #raiz = ET.fromstring(self.entrada)

        for perfiles in raiz.findall(".//perfiles/perfil"):
            nombrePerfil = perfiles.find("nombre").text
            
            if self._verificarPefil(nombrePerfil) == True:
                self.perfilesActualizados += 1

                for PalabraClave in perfiles.findall("palabrasClave/palabra"):
                    palabra = PalabraClave.text

                    if self._verificarPalabraClave(nombrePerfil, palabra) == False:
                        self._agregarPalabraClave(nombrePerfil, palabra)
            
            elif self._verificarPefil(nombrePerfil) == False:
                self.pefilesCreados += 1
                
                self._agregarPerfil(nombrePerfil)

                for PalabraClave in perfiles.findall("palabrasClave/palabra"):
                    palabra = PalabraClave.text

                    if self._verificarPalabraClave(nombrePerfil, palabra) == False:
                        self._agregarPalabraClave(nombrePerfil, palabra)
                    
                    
        

        for descartadas in raiz.findall(".//descartadas/palabra"):
            palabra = descartadas.text

            self._verificarDescartadas(palabra)






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

    
    def _verificarPalabraClave(self, NombrePerfil, palabraClave):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)
    
    
        palabras = datos["Perfiles"][NombrePerfil]
        if palabraClave in palabras:
            return True
        else:
            return False


    def _agregarPalabraClave(self, perfil, palabra):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        datos["Perfiles"][perfil].append(palabra)

        with open('Backend\Data\DataBase.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)


    def _agregarPerfil(self, perfil):
        with open('Backend\Data\DataBase.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

        datos["Perfiles"][perfil] = []

        with open('Backend\Data\DataBase.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)

    
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
                json.dump(datos, archivo, indent=4)
        
    
    



cargar = BaseDatos(ruta)
cargar._leerXML()
print(f"Crados: {cargar.pefilesCreados}, Actualizados: {cargar.perfilesActualizados}")


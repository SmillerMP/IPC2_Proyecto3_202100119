

listaExcluidos = ['a', 'un', 'una', 'en', 'para', 'por', 'que', 'qué', 'la', 'las', 'los', 'el', 'unas', 'si', 'no', 'sino', 'entre', 
                  'otro', 'otra', 'otros', 'otras', 'de', 'del', 'nos', 'sus', 'su', 'am', 'pm']

listaNumeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

perfilDeportista = ['fútbol', 'balonmano', 'baloncesto', 'balompié', 'football', 'basketball', 'handball', 'estadio', 'selección', 
                    'champions' 'league', 'liga de campeones', 'tenis', 'natación', 'olimpiada','gym', 'gimnasio']

perfilCulturaSaludable = ['gimnasio', 'comida' 'saludable', 'ejercicio', 'maratón', 'carrera', 'entreno','entrenar', 'entrenamiento', 
                          'pesas', 'karate', 'tae kwon do', 'boxeo', 'gym', 'healthy food', 'vitaminas', 'caminata', 'caminar', 'ropa deportiva', 
                          'bebida hidratante', 'bebidas hidratantes']

signosExcluidos = [',', '.', ';', ':']


# Guarda en la variable contenido, cada una de las lineas del archivo
with open("Backend\Test\mensaje.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()


print(type(contenido))
print(contenido)
texto = ''

# Recorre el string de contenido
for x in contenido:

    # remplaza el espacio por un signo #, y en caso de que exista un 
    # salto de linea lo elimina
    x = x.replace(" ", "#").replace("\n", "#")

    # Busca signos, como la coma o punto y los elimina
    for signo in signosExcluidos:
        x = x.replace(signo, "")

    texto += x
    print(texto)

texto = texto.lower()
texto = texto.split('#')
print(texto)


for j in texto:

    for excluidos in listaExcluidos:
        if excluidos == j:
            texto.pop(texto.index(j))
    
    try:
        prueba = float(j)
        texto.pop(texto.index(j))
    except:
        continue



print(texto)

contadorCoincidencias = 0
for palabra in texto:

    for busqueda in perfilDeportista:

        if palabra == busqueda:
            contadorCoincidencias += 1
            break


print(contadorCoincidencias)


class analizador():

    def __init__(self, texto, diccionarioPerfiles):
        self.text = texto
        self.palabras = ''
        self.diccionarioPerfiles = diccionarioPerfiles
        

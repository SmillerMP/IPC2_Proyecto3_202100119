import json
import os

class tablaDot:
    
    def __init__(self, usuario):
        self.usuario = usuario


    def _buscar(self):

        
        with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)

        listaUsuarios = datos.keys()
        if listaUsuarios == []:
            with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
                datos = json.load(archivo_json)

            with open("Backend\Reports\Tabla.dot", "w", encoding="utf-8") as grafo_dot:
                grafo_dot.write('digraph { \n')
                grafo_dot.write(f'graph [label="No existen Usuarios", labelloc=top]\n')
                grafo_dot.write('rankdir = LR \n' )
                grafo_dot.write('ranksep=1.5 \n' )
                grafo_dot.write(f'node[shape=none, style="filled" fontname="Arial", fontsize=12] \n\n')
                
                            
                grafo_dot.write('\n\n}')
            os.system("dot.exe -Tpdf Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.pdf")
            os.system("dot.exe -Tsvg Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.svg")


        
        elif self.usuario == "todos":
            self._tablaTodos()

        elif self.usuario in listaUsuarios:
            self._tabla(self.usuario)
        else:
            with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
                datos = json.load(archivo_json)

            with open("Backend\Reports\Tabla.dot", "w", encoding="utf-8") as grafo_dot:
                grafo_dot.write('digraph { \n')
                grafo_dot.write(f'graph [label="No se ha encontrado ningun Usuario llamado {self.usuario}", labelloc=top]\n')
                grafo_dot.write('rankdir = LR \n' )
                grafo_dot.write('ranksep=1.5 \n' )
                grafo_dot.write(f'node[shape=none, style="filled" fontname="Arial", fontsize=12] \n\n')
                
                            
                grafo_dot.write('\n\n}')
            os.system("dot.exe -Tpdf Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.pdf")
            os.system("dot.exe -Tsvg Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.svg")





    def _tabla(self, user):
        with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)

        usuario = datos[f"{user}"]["Mensajes"]
        #print(usuario)
        textoPefil = ''
        with open("Backend\Reports\Tabla.dot", "w", encoding="utf-8") as grafo_dot:
            grafo_dot.write('digraph { \n')
            grafo_dot.write(f'graph [label="Lista de Mensajes", labelloc=top]\n')
            grafo_dot.write('rankdir = LR \n' )
            grafo_dot.write('ranksep=1.5 \n' )
            grafo_dot.write(f'node[shape=none, style="filled" fontname="Arial", fontsize=12] \n\n')
            
            # creara el encabezado en graphviz
            grafo_dot.write(f'''
            
        n{1} [ label = <
            <table>
                <tr><td bgcolor="#bb8fce" colspan="3" align="center"><b>Usuario: {user}</b></td></tr>
                <tr><td bgcolor="#e74c3c"> Fecha </td><td bgcolor="#f39c12 "> Hora </td><td bgcolor="#f1c40f"> Pefiles </td></tr>
                        ''')

            # Recorre la lista con diccionarios, donde se ecuentra cada uno de los tokens encontrados
            for mensaje in usuario:
                textoPefil = '<br/>'
                for perfil, valor in mensaje["Perfiles"].items():
                    textoPefil += f"{perfil}: {valor} <br/>"

                grafo_dot.write(f'''     
                <tr><td bgcolor="#f1948a "> {mensaje["Fecha"]} </td><td bgcolor="#f8c471 "> {mensaje["Hora"]} </td><td bgcolor="#f7dc6f"> {textoPefil} </td> </tr>                
                                ''')
                                
                        
            # Cierra la tabla
            grafo_dot.write(f'''
            </table>
        > ]
                        ''')
                        
            grafo_dot.write('\n\n}')
        os.system("dot.exe -Tpdf Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.pdf")
        os.system("dot.exe -Tsvg Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.svg")


    def _tablaTodos(self):
        with open('Backend\Data\MensajesDataBase.json', 'r', encoding='utf-8') as archivo_json:
            datos = json.load(archivo_json)

        #print(usuario)
        textoPefil = ''
        with open("Backend\Reports\Tabla.dot", "w", encoding="utf-8") as grafo_dot:
            grafo_dot.write('digraph { \n')
            grafo_dot.write(f'graph [label="Lista de Mensajes Todos los Usuarios", labelloc=top]\n')
            grafo_dot.write('rankdir = LR \n' )
            grafo_dot.write('ranksep=1.5 \n' )
            grafo_dot.write(f'node[shape=none, style="filled" fontname="Arial", fontsize=12] \n\n')
            
            for usuarios in datos:
                usuario = datos[f"{usuarios}"]["Mensajes"]
            # creara el encabezado en graphviz
                grafo_dot.write(f'''
                
            n{usuarios} [ label = <
                <table>
                    <tr><td bgcolor="#bb8fce" colspan="3" align="center"><b>Usuario: {usuarios}</b></td></tr>
                    <tr><td bgcolor="#e74c3c"> Fecha </td><td bgcolor="#f39c12 "> Hora </td><td bgcolor="#f1c40f"> Pefiles </td></tr>
                            ''')

                # Recorre la lista con diccionarios, donde se ecuentra cada uno de los tokens encontrados
                for mensaje in usuario:
                    textoPefil = '<br/>'
                    for perfil, valor in mensaje["Perfiles"].items():
                        textoPefil += f"{perfil}: {valor} <br/>"

                    grafo_dot.write(f'''     
                    <tr><td bgcolor="#f1948a "> {mensaje["Fecha"]} </td><td bgcolor="#f8c471 "> {mensaje["Hora"]} </td><td bgcolor="#f7dc6f"> {textoPefil} </td> </tr>                
                                    ''')
                                    
                            
                # Cierra la tabla
                grafo_dot.write(f'''
                </table>
            > ]
                            ''')
                            

            grafo_dot.write('\n\n}')
        os.system("dot.exe -Tpdf Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.pdf")
        os.system("dot.exe -Tsvg Backend\Reports\Tabla.dot -o  Backend\Reports\Tabla.svg")

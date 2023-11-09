playlist = {} #diccionario vacío
playlist['canciones'] = [] #lista de canciones vacía

#función principal
def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Cómo deseas nombrar la playlist? \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            #cuando ya tenemos un nombre, descativar el true
            agregar_playlist = False

            #mandar a llamar la función para agregar canciones
            agregar_canciones()

def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #pregunta al usuario qué quiere agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para tu playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "x" cuando hayas finalizado'

        cancion = input(pregunta)

        if cancion == 'x':
            #deja de agregar canciones
            agregar_cancion = False
            
            #ver resumen de la playlist
            mostrar_resumen()
        else:
            #sigue agregando canciones
            playlist['canciones'].append(cancion)
            print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()    
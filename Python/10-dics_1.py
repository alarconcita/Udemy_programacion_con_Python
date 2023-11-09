#creando un diccionario simple
cancion = {
    'artista' : 'Metallica', #llave=artista (a la izquierda de los :) 
    'canción' : 'Enter Sandman', 
    'lanzamiento' : 1992, #valor=1992 (a la derecha de los :)
    'likes' : 3000
}
#acceder a los elementos del diccionario
print(cancion['artista'])

#mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando {artista}')

print(cancion)

#agregar nuevos valores
cancion['playlist'] = 'Heavy metal'
print(cancion)

#reemplazar valor 
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#eliminar valor
del cancion ['lanzamiento']
print(cancion)
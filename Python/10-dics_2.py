#iniciar un diccionario vacío
jugador = {}
print(jugador)

#se une un jugador
jugador['nombre'] = 'Juan'
jugador['puntaje'] = 0
print(jugador)

#incremento del puntaje
jugador['puntaje'] = 100
print(jugador)

jugador['puntaje'] = 200
print(jugador)

#acceder a un valor
print(jugador.get()'consola', 'No existe ese valor'))

#iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#eliminar 
del jugador['nombre']
del jugador['puntaje']
print(jugador)
#variables
me_llamo = 'Mariana Alarcón'
comida = 'facturas'

print('Mi nombre es ' + me_llamo)
print('Mi última comida fue ' + comida)

#funciones_1
def mensaje_1():
    print('Hola, estoy practicando funciones en Python')

mensaje_1()

#funciones_2
def mensaje_2(usuario):
    return usuario

practicando = mensaje_2('Hola, bienvenida Lupe')
print(practicando)

#funciones_3
def mensaje_3(actividad):
    return actividad

practicando1 = mensaje_3('Estoy practicando inglés y Python')
print(practicando1)

#input
#realizar un examen con 3 preguntas con respuestas SI/NO
#calificar con variable que inicia en 0
#se incrementa en 1 con cada respuesta correcta
print('Bienvenid@ al examen, responde SI o NO y al final verás tu nota:')
nota = 0

pregunta_1 = input('La bandera de Argentina es celeste y blanca? \r\n')
pregunta_1 = pregunta_1.upper()
if pregunta_1 == 'SI':
    print('Acertaste en la pregunta 1!')
    nota += 1
else:
    print('Respuesta incorrecta.')

pregunta_2 = input('En el año 2002 Argentina salió campeón en el mundial de fútbol? \r\n')
pregunta_2 = pregunta_2.upper()
if pregunta_2 == 'NO':
    print('Acertaste en la pregunta 2!')
    nota += 1
else:
    print('Respuesta incorrecta.')

pregunta_3 = input('Argentina tiene 3 copas del mundo en fútbol masculino? \r\n')
pregunta_3 = pregunta_3.upper()
if pregunta_3 == 'NO':
    print('Acertaste en la pregunta 3!')
    nota += 1
else:
    print('Respuesta incorrecta.')

print('Tu nota final es:', nota)
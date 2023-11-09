#se ejecuta mientras una condición sea verdadera
pregunta = 'Pon un número y veremos si es par o no: \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación) \r\n'
preguntar= True

while preguntar:
    numero = input(pregunta)
    if numero ==  'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else:
            print(f'El número {numero} es impar')

number = 0

while number <= 10:
    print(number)
    number += 1 #incremento para evitar loop infinito

#if dentro del while
while number <= 10:
    if number == 5:
        print('Cinco!')
    else: 
        print(number)
    number += 1
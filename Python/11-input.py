nombre = input('Ingresa tu nombre: \r\n')

print(f'Hola {nombre}')

#leer datos que sean numéricos
edad = input('Ingresa tu edad:') #la entrada siempre es un string
edad = int(edad) #convertir edad (string) a int
if edad >= 18:
    print('Puedes votar')
else:
    print('Aún no puedes votar')

#mezclar con operadores
numero = input('Pon un número y veremos si es par o no: \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')
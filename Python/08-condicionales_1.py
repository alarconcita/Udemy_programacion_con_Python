balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

#likes
likes = 200
if likes == 200:
    print('200 likes')

#if con texto y 'not'
lenguaje = 'Python'
if not lenguaje == 'Python':
    print('Excelente decisión')

#evaluar un boolean
usuario_autenticado = True
if usuario_autenticado:
    print('Acceso correcto')
else:
    print('Debes iniciar sesión')

#evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
if 'PHP' in lenguajes:
    print('PHP está')
else:
    print('No está en la lista')

#if anidados
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('Acceso total')
    else: 
        print('Acceso correcto')
else:
    print('Debes iniciar sesión')
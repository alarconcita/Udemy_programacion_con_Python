def informacion(nombre, rol):
    print(f'Soy {nombre} y soy {rol}')

informacion('Lupe', 'la hija')
informacion('Juan', 'el papá')
informacion('Mariana', 'la mamá')


def otro_ejemplo(persona, dato = 'desconocido'):
    print(f'Soy {persona} y soy {dato}')

otro_ejemplo('Lupe', 'la hija')
otro_ejemplo('Juan', 'el papá')
otro_ejemplo('Mariana', 'la mamá')
otro_ejemplo('Francio')
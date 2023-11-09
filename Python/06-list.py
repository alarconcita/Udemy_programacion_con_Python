lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

#Arrays comienzan en la posición 0
print(lenguajes[2]) #Java

#ordenar alfabéticamente
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#agregar elementos
lenguajes.append('Ruby')
print(lenguajes)

#eliminar elementos
del lenguajes[1]
print(lenguajes)

#eliminar elementos, otro método
lenguajes.pop() #elimina el último elemento
print(lenguajes)

#eliminar elementos con pop en posición específica
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)
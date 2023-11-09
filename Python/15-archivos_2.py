def app():
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido) #también se puede usar print(contenido.rstrip()) 

app()
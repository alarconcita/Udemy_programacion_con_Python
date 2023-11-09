def app():
    #crear el archivo
    archivo = open('archivo.txt', 'w') #w es escritura, si no existe lo creará

    #generar números en archivo
    for i in range(0, 20):
        archivo.write('Esta es la línea ' + str(i) + "\r\n")
    
    #cerrar el archivo
    archivo.close()

app()
import os

CARPETA = 'Contactos/' #carpeta de contactos
EXTENSION = '.txt' #extensión de archivos

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #revisa si la carpeta existe o no
    crear_directorio()

    #muestra el menú de opciones
    mostrar_menu()

    #preguntar al usuario qué acción desea realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente nuevamente')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado correctamente \r\n')
    except expression as identifier:
        print('El contacto no existe')
        
    #reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    #reiniciar la app
    app()
    
def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
            #imprime un separador entre contactos
            print('\r\n')

def editar_contacto():
    print('Elige el contacto a editar')
    nombre_anterior = input('Nombre del contacto a editar: \r\n')
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION + 'w') as archivo:
            #resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre:\r\n')
            telefono_contacto = input('Agrega el nuevo teléfono:\r\n')
            categoria_contacto = input('Agrega la nueva categoría:\r\n')
            
            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, 
                      CARPETA + nombre_contacto + EXTENSION)
            
            #mostrar mensaje de éxito
            print('\r\n Contacto editado correctamente \r\n')

            
    else:
        print('Ese contacto no existe')
    
    #reiniciar app
    app()

def agregar_contacto():
    print('Completa los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre:\r\n')

    #validar la existencia previa de un contacto
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION + 'w') as archivo:
            telefono_contacto = input('Teléfono:\r\n')
            categoria_contacto = input('Categoría:\r\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #mostrar mensaje de éxito
            print('\r\n Contacto agregado correctamente \r\n')
    else:
        print('El contacto ya existe')
    
    #reiniciar la app para poder cargar un nuevo contacto
    app()

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer:')
    print('1- Agregar nuevo contacto')
    print('2- Editar contacto')
    print('3- Ver contactos')
    print('4- Buscar contacto')
    print('5- Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
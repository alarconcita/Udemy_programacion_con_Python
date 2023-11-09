class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
  
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, 
              Categoría: {self.categoria},
              Precio: {self.precio}')

#instanciar la clase
restaurant = Restaurant('GA_Restó', 'Comida argentina', 2500) #restaurant = objeto y Restaurant = clase
restaurant.mostrar_informacion()

restaurant2 = Restaurant('coffee.py', 'Bar&Café', 1000)
restaurant2.mostrar_informacion()
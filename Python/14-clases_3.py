class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio #Default: public, _PROTECTED, __PRIVATE
  
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, 
              Categoría: {self.categoria},
              Precio: {self.__precio}')

#Getters y setters (get obtiene un valor, set agrega)
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio

#instanciar la clase
restaurant = Restaurant('GA_Restó', 'Comida argentina', 2500) #restaurant = objeto y Restaurant = clase
# restaurant.__precio = 3000 #con PRIVATE no se puede modificar
restaurant.mostrar_informacion()
restaurant.set_precio(3000)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant('coffee.py', 'Bar&Café', 1000)
restaurant2.mostrar_informacion()
restaurant2.set_precio(1500)
precio = restaurant2.get_precio()
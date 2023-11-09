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

#Crea una clase hijo 
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 estrellas', 20000)
hotel.mostrar_informacion()
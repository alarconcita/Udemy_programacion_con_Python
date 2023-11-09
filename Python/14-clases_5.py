class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio #Default: public, _PROTECTED, __PRIVATE
  
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, 
              Categoría: {self.categoria},
              Precio: {self.precio}')

#Getters y setters (get obtiene un valor, set agrega)
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio

#Crea una clase hijo 
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, piscina):
        super().__init__(nombre, categoria, precio)
        self.piscina = piscina
    
    #reescribir un método (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, 
              Categoría: {self.categoria},
              Precio: {self.precio},
              Piscina: {self.piscina}')
    #agrega un método que solo existe en hotel, la clase hijo
    def get_piscina(self)
        return self.piscina

hotel = Hotel('Hotel POO', '5 estrellas', 20000, 'Si')
hotel.mostrar_informacion()
piscina = hotel.get_piscina()
print(piscina)
class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo de la clase
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#instanciar la clase
restaurant = Restaurant() #restaurant = objeto y Restaurant = clase
restaurant.agregar_restaurant('GA_Restó')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('coffee.py')
restaurant2.mostrar_informacion()

#mostrar la información
print(f'Nombre: {restaurant.nombre}')
print(f'Nombre: {restaurant2.nombre}')
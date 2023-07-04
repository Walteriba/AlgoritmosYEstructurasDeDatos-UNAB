# A comntinuación les comparto un ejemplo de un parcial.
# Este archivo está dividido en dos partes, esta primera con los enunciados; 
# y luego una posible solución

#Ejercicio 1
# Modelar una clase peluquería; la misma tiene como variables un nombre, una dirección, un teléfono, un email y los horarios de atención
#Ejercicio 2
# Del ejercicio anterior agregar un método que devuelva si la peluquería está abierta según su variable de horario de atención (importa el modulo datetime)
#Ejercicio 3
# Crea el módulo productos_peluqueria.py, Dentro de productos_peluqueria.py, define una clase llamada ProductoPeluqueria.
# Esta clase representará un producto específico de la peluquería, con sus propias variables como nombre, precio, descripción, etc.
#Ejercicio 4
# Agrega a la clase peluqería una lista enlazada de productos de peluquerías declarados en el modulo productos_peluqueria.py
#Ejercicio 5
# Agrega a la paluqueria una cola de clientes (puedes utilizar el modulo deque de Collections o puedes modelar 
# la cola/fila con una lista enlazada)
#Ejercicio 6
# Genera dos iteradores para el ejercicio anterior, uno que recorra la lista enlazada de productos de peluquerias e imprima el producto y 
# su precio; y el otro que recorra la cola de clientes y cuente cuantos hay esperando
#Ejercicio 7
# Agrega un método que cree una carpeta inventario, y que dentro de ella guarde la lista enlazada de productos. Agrega un segundo método para que 
# en el init de la clase, si el archivo existe, cargue la lista enlazada de productos


# Ejercicio 1
#archivo main.py

class Peluqueria:
    def __init__(self, nombre, direccion, telefono, email, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.horarios = horarios

    def mostrar_informacion(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.telefono)
        print("Email: ", self.email)
        print("Horarios de atención: ")
        for dia, horario in self.horarios.items():
            print(dia, ": ", horario)


# Ejemplo de uso
horarios_atencion = {
    "Lunes": "9:00 AM - 6:00 PM",
    "Martes": "9:00 AM - 6:00 PM",
    "Miércoles": "9:00 AM - 6:00 PM",
    "Jueves": "9:00 AM - 6:00 PM",
    "Viernes": "9:00 AM - 6:00 PM",
    "Sábado": "10:00 AM - 4:00 PM"
}

peluqueria = Peluqueria("Peluquería XYZ", "Calle Principal 123", "123456789", "info@peluqueria.com", horarios_atencion)
peluqueria.mostrar_informacion()


#En este ejemplo, la clase Peluqueria tiene un constructor __init__ que recibe los parámetros nombre,
# direccion, telefono, email y horarios. Estos parámetros se asignan a las variables de instancia
# correspondientes.

#La clase también tiene un método mostrar_informacion que imprime por pantalla la información de la peluquería,
# incluyendo los horarios de atención. Los horarios de atención se almacenan en un diccionario, donde
# las claves son los días de la semana y los valores son los horarios correspondientes.

#Luego, se crea una instancia de la clase Peluqueria con valores de ejemplo y se llama
# al método mostrar_informacion para mostrar la información de la peluquería. Puedes modificar los valores de ejemplo
# para adaptarlos a tu caso específico.


# Ejercicio 2
#archivo main.py

import datetime

class Peluqueria:
    def __init__(self, nombre, direccion, telefono, email, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.horarios = horarios

    def mostrar_informacion(self):
        print("Nombre: ", self.nombre)
        print("Dirección: ", self.direccion)
        print("Teléfono: ", self.telefono)
        print("Email: ", self.email)
        print("Horarios de atención: ")
        for dia, horario in self.horarios.items():
            print(dia, ": ", horario)

    def esta_abierta(self):
        ahora = datetime.datetime.now()
        dia_actual = ahora.strftime("%A")  # Obtenemos el nombre del día actual en formato de texto
        
        if dia_actual in self.horarios:
            horario_actual = ahora.strftime("%I:%M %p")  # Obtenemos la hora actual en formato de texto
            horario_atencion = self.horarios[dia_actual]
            
            hora_apertura, hora_cierre = horario_atencion.split(" - ")
            
            if hora_apertura <= horario_actual <= hora_cierre:
                return True
        
        return False


# Ejemplo de uso
horarios_atencion = {
    "Lunes": "9:00 AM - 6:00 PM",
    "Martes": "9:00 AM - 6:00 PM",
    "Miércoles": "9:00 AM - 6:00 PM",
    "Jueves": "9:00 AM - 6:00 PM",
    "Viernes": "9:00 AM - 6:00 PM",
    "Sábado": "10:00 AM - 4:00 PM"
}

peluqueria = Peluqueria("Peluquería XYZ", "Calle Principal 123", "123456789", "info@peluqueria.com", horarios_atencion)
peluqueria.mostrar_informacion()

if peluqueria.esta_abierta():
    print("La peluquería está abierta.")
else:
    print("La peluquería está cerrada.")


# En esta versión, se agrega el método esta_abierta, que utiliza el módulo datetime para obtener el día
# actual y la hora actual. Luego, compara el día actual con los horarios de atención de la peluquería.
# Si el día actual está en los horarios de atención y la hora actual está dentro del rango de apertura y cierre,
# se devuelve True, lo que indica que la peluquería está abierta. De lo contrario, se devuelve False.

# En el ejemplo de uso, se crea una instancia de la clase Peluqueria y se llama al método
# mostrar_informacion para mostrar la información de la peluquería. Luego, se utiliza el método esta_abierta para determinar si la peluquería
# está abierta o cerrada, y se muestra un mensaje correspondiente.

#Ejercicio 3
#archivo productos_peluqueria.py
class ProductoPeluqueria:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

# Ejercicio 4
#archivo productos_peluqueria.py
class ProductoPeluqueria:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class NodoProducto:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None

#archivo main.py

import datetime
from productos_peluqueria import ProductoPeluqueria
from productos_peluqueria import NodoProducto


class Peluqueria:
    def __init__(self, nombre, direccion, telefono, email, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.horarios = horarios
        self.primer_producto = None

    #..............#

    def agregar_producto(self, producto):
    nuevo_nodo = NodoProducto(producto)

    if self.primer_producto is None:
        self.primer_producto = nuevo_nodo
    else:
        nodo_actual = self.primer_producto
        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo


    def sacar_producto(self, nombre_producto):
    if self.primer_producto is None:
        return  # Si la lista está vacía, no se puede sacar ningún producto

    # Si el primer producto de la lista coincide con el nombre buscado
    if self.primer_producto.producto.nombre == nombre_producto:
        self.primer_producto = self.primer_producto.siguiente
        return  # Se sacó el producto y se finaliza el método

    # Si el producto está en otro lugar de la lista
    nodo_actual = self.primer_producto
    while nodo_actual.siguiente is not None:
        if nodo_actual.siguiente.producto.nombre == nombre_producto:
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente
            return  # Se sacó el producto y se finaliza el método
        nodo_actual = nodo_actual.siguiente

    # Si no se encontró el producto en la lista
    print("El producto no se encuentra en la lista de productos.")





peluqueria = Peluqueria("Peluquería XYZ", "Calle Principal 123", "123456789", "info@peluqueria.com", horarios_atencion)

producto1 = ProductoPeluqueria("Champú", 10.99, "Limpia y nutre el cabello")
producto2 = ProductoPeluqueria("Acondicionador", 8.99, "Suaviza y desenreda el cabello")
producto3 = ProductoPeluqueria("Gel fijador", 5.99, "Fija el peinado")

peluqueria.agregar_producto(producto1)
peluqueria.agregar_producto(producto2)
peluqueria.agregar_producto(producto3)

peluqueria.sacar_producto("Acondicionador")



# En este ejemplo, se agrega un nuevo método sacar_producto a la clase Peluqueria. Este método recibe como parámetro el nombre
# del producto que se desea sacar de la lista enlazada.

# El método verifica si la lista está vacía. Si no está vacía, busca el producto en la lista enlazada.
# Si encuentra el producto, lo saca actualizando los enlaces de los nodos. Si no encuentra el producto, muestra
# un mensaje indicando que el producto no se encuentra en la lista.

# Luego, en el archivo principal, se crea una instancia de la clase Peluqueria, se agregan varios productos a la
# lista enlazada y se utiliza el método sacar_producto para eliminar el producto con el nombre "Acondicionador" de la lista.



# Ejercicio 5
#archivo main.py

import datetime
from productos_peluqueria import ProductoPeluqueria
from productos_peluqueria import NodoProducto
from collections import deque

class Peluqueria:
    def __init__(self, nombre, direccion, telefono, email, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.horarios = horarios
        self.productos = []
        self.cola_clientes = deque()

#........#

	def agregar_cliente(self, nombre_cliente):
    	self.cola_clientes.append(nombre_cliente)

# Puedes agregar otros métodos relacionados con la cola de clientes según tus necesidades, 
# como un método atender_siguiente_cliente que retire y devuelva el próximo cliente de la cola:


    def atender_siguiente_cliente(self):
	    if self.cola_clientes:
    	    return self.cola_clientes.popleft()
    	else:
        	return None  # La cola está vacía

# De esta manera, puedes utilizar la cola de clientes en la clase Peluqueria 
# para gestionar el orden de atención de los clientes. Puedes agregar clientes a la cola utilizando 
# el método agregar_cliente, y luego atender al siguiente cliente en orden utilizando el método atender_siguiente_cliente.

# Ejercicio 6

class Peluqueria:
    # ...

    def __iter__(self):
        # Iterador para la lista enlazada de productos
        class ProductosIterator:
            def __init__(self, primer_producto):
                self.nodo_actual = primer_producto

            def __iter__(self):
                return self

            def __next__(self):
                if self.nodo_actual is None:
                    raise StopIteration
                producto = self.nodo_actual.producto
                self.nodo_actual = self.nodo_actual.siguiente
                return producto

        return ProductosIterator(self.primer_producto)

    def __len__(self):
        # Cuenta el número de clientes en la cola
        return len(self.cola_clientes)

#...

peluqueria = Peluqueria("Peluquería XYZ", "Calle Principal 123", "123456789", "info@peluqueria.com", horarios_atencion)

producto1 = ProductoPeluqueria("Champú", 10.99, "Limpia y nutre el cabello")
producto2 = ProductoPeluqueria("Acondicionador", 8.99, "Suaviza y desenreda el cabello")
producto3 = ProductoPeluqueria("Gel fijador", 5.99, "Fija el peinado")

peluqueria.agregar_producto(producto1)
peluqueria.agregar_producto(producto2)
peluqueria.agregar_producto(producto3)

# Iterador para la lista enlazada de productos
for producto in peluqueria:
    print(producto.nombre, producto.precio)

# Obtener el número de clientes en espera
print(len(peluqueria))


# En este ejemplo, se agrega una clase interna ProductosIterator dentro de la clase Peluqueria. Esta clase implementa
# los métodos especiales __iter__() y __next__(), que permiten recorrer la lista enlazada de productos de peluquería.

# El método __iter__() devuelve una instancia del iterador ProductosIterator, que se inicializa con el primer
# producto de la lista enlazada. El método __next__() devuelve el siguiente producto en cada iteración, hasta que se
# llegue al final de la lista.

# Luego, en el archivo principal, se crea una instancia de la clase Peluqueria y se agregan varios productos
# a la lista enlazada. Luego, se utiliza un bucle for para recorrer la lista enlazada de productos, imprimiendo
# el nombre y precio de cada producto.

# Además, se utiliza la función len() para obtener el número de clientes en espera en la cola.
# Hacemos sobrecarga de métodos!!!

# Ejercicio 7
#archivo main.py

# ....
import os

# ....
class Peluqueria:

	def __init__(self, nombre, direccion, telefono, email, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.horarios = horarios
        self.primer_producto = None
        self.cola_clientes = deque()

        self.crear_carpeta_inventario()
        self.cargar_productos_desde_archivo()

    # ...

    def crear_carpeta_inventario(self):
        if not os.path.exists('inventario'):
            os.makedirs('inventario')

    def guardar_productos_en_archivo(self):
        archivo = os.path.join('inventario', 'productos.txt')
        with open(archivo, 'w') as f:
            nodo_actual = self.primer_producto
            while nodo_actual is not None:
                producto = nodo_actual.producto
                f.write(f'{producto.nombre},{producto.precio},{producto.descripcion}\n')
                nodo_actual = nodo_actual.siguiente

    def cargar_productos_desde_archivo(self):
        archivo = os.path.join('inventario', 'productos.txt')
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    nombre = datos[0]
                    precio = float(datos[1])
                    descripcion = datos[2]
                    producto = ProductoPeluqueria(nombre, precio, descripcion)
                    self.agregar_producto(producto)


# En este código, el método crear_carpeta_inventario() verifica si la carpeta "inventario" existe. Si no existe
#, crea la carpeta utilizando la función os.makedirs().

# El método guardar_productos_en_archivo() guarda la lista enlazada de productos en un archivo llamado "productos.txt" dentro de
# la carpeta "inventario". Utiliza un bucle para recorrer la lista enlazada y escribe cada producto en una línea separada con 
# el formato "nombre,precio,descripcion".

# El método cargar_productos_desde_archivo() verifica si el archivo "productos.txt" existe en la carpeta "inventario". Si existe
#, lee cada línea del archivo, separa los datos utilizando la coma como separador y crea un objeto ProductoPeluqueria con los 
# datos obtenidos. Luego, llama al método agregar_producto() para agregar cada producto a la lista enlazada.

# Finalmente, el método __init__() de la clase Peluqueria llama a los métodos crear_carpeta_inventario() y 
# cargar_productos_desde_archivo()
# para crear la carpeta y cargar los productos al crear una instancia de la clase.

# De esta manera, puedes utilizar los nuevos métodos para crear la carpeta "inventario", guardar los productos
# en un archivo










# EJERCICIO 2:

# 2.1: Modelar una clase Biblioteca; la misma tiene como variables un nombre, 
# una dirección, un teléfono, un email y los horarios de atención de la misma. Ademas de estos 
# datos básicos, la biblioteca debe contener una lista de los libros disponibles. La biblioteca 
# debera proveer métodos para: ingresar nuevos usuarios, prestar libros y aceptar devoluciones de los mismos.

# 2.2: Agregar a la clase Biblioteca una lista de los usuarios, la lista deberá contener como 
# información adicional la lista de los libros que el usuario tiene en su posesión. Las listas deben 
# ser representadas utilizando un Lista Enlazadas.
# Nota: los usuarios y libros son del tipo declarado en el Ejercicio 1

# 2.3:
# Agregar a la clase Biblioteca una lista enlazada que contenga los libros que han sido prestados, 
# la lista deberá estar ordenada de forma ascendente según la fecha de vencimineto del prestamo, es decir, 
# aquellos libros que el prestamo expira pronto van primero. Si se detectan libros con periodo de prestamo 
# expirados se deberá enviar un mensaje al usuario.
# Nota: el tiempo de un prestamo es de 30 dias

# 2.4 Genrar los Iteradores correspondientes para recorrer:
# La lista de usuarios;
# La lista de libros que cada ususrio tiene en su posesion;
# Los libros prestados.


# 2.5 Agrega un método que cree una carpeta llamada "inventario", y que dentro de ella guarde en 
# distintos archivos la lista libros disponibles y los libros prestados.
# Nota: los archivos pueden ser de texto o binarios

# 2.6 Agrega en el __init__ de la clase, si los archivos existen, se carguen las listas de libros.
# Nota: los archivos pueden ser de texto o binarios

# ANTES DE CREAR LA CLASE BIBLIOTECA, CREAMOS LOS NODOS PARA LA LISTA ENLAZADA DEL PUNTO 2.2

import datetime
import os

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_en_posesion = ListaEnlazada()

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

# Definición de la clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, info):
        self.data = info
        self.next = None

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insert(self, info):
        # Inserta un nuevo nodo al final de la lista enlazada
        nuevo_nodo = Nodo(info)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def remove(self, info):
        # Elimina un nodo que contiene la información dada de la lista enlazada
        if self.head is None:
            return

        if self.head.data == info:
            self.head = self.head.next
            return

        actual = self.head
        while actual.next:
            if actual.next.data == info:
                actual.next = actual.next.next
                return
            actual = actual.next

    def __iter__(self):
        # Iterador para recorrer la lista enlazada
        actual = self.head
        while actual:
            yield actual.data
            actual = actual.next

# 2.1: MODELADO DE LA CLASE BIBLIOTECA - Definición e inicializacion de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Inicialización de los atributos de la biblioteca
        self.nombre = input("Ingrese el nombre de la biblioteca: ")
        self.direccion = input("Ingrese la dirección de la biblioteca: ")
        self.telefono = input("Ingrese el teléfono de la biblioteca: ")
        self.email = input("Ingrese el email de la biblioteca: ")
        self.horarios = input("Ingrese los horarios de atención de la biblioteca: ")
        self.libros_disponibles = ListaEnlazada()  # Lista enlazada para almacenar los libros disponibles
        self.libros_prestados = ListaEnlazada()  # Lista enlazada para almacenar los libros prestados
        self.usuarios = ListaEnlazada()  # Lista enlazada para almacenar los usuarios registrados
    # Verificar si los archivos existen y cargar las listas de libros
        if os.path.exists("inventario/libros_disponibles.txt"):
            self.cargar_libros_disponibles()

        if os.path.exists("inventario/libros_prestados.txt"):
            self.cargar_libros_prestados()
# 2.2: METODOS PARA CREAR LISTA DE USUARIOS Y LIBROS
    def ingresar_usuario(self, nombre):
        # Crea una instancia de la clase Usuario y la agrega a la lista de usuarios de la biblioteca
        usuario = Usuario(nombre)
        self.usuarios.insert(usuario)
        print(f"Usuario '{nombre}' ha sido registrado en la biblioteca.")

    def agregar_libro_disponible(self, titulo):
        # Crea una instancia de la clase Libro y la agrega a la lista de libros disponibles de la biblioteca
        libro = Libro(titulo)
        self.libros_disponibles.insert(libro)
        print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

    def prestar_libro(self, libro_titulo, usuario_nombre):
        # Busca el usuario y el libro en las listas correspondientes y realiza el préstamo
        usuario = None
        libro = None

        for usuario_actual in self.usuarios:
            if usuario_actual.nombre == usuario_nombre:
                usuario = usuario_actual
                break

        for libro_actual in self.libros_disponibles:
            if libro_actual.titulo == libro_titulo:
                libro = libro_actual
                break

        if usuario and libro:
            self.libros_disponibles.remove(libro)
            self.libros_prestados.insert((libro, None))
            usuario.libros_en_posesion.insert(libro)
            print(f"El libro '{libro_titulo}' ha sido prestado a '{usuario_nombre}'.")
        else:
            print("Usuario o libro no encontrado.")

    def aceptar_devolucion(self, libro_titulo, usuario_nombre):
        # Busca el usuario y el libro en las listas correspondientes y acepta la devolución
        usuario = None
        libro = None

        for usuario_actual in self.usuarios:
            if usuario_actual.nombre == usuario_nombre:
                usuario = usuario_actual
                break

        for libro_actual in usuario.libros_en_posesion:
            if libro_actual.titulo == libro_titulo:
                libro = libro_actual
                break

        if usuario and libro:
            usuario.libros_en_posesion.remove(libro)
            self.libros_disponibles.insert(libro)
            self.libros_prestados.remove((libro, None))
            print(f"El libro '{libro_titulo}' ha sido devuelto por '{usuario_nombre}'.")
        else:
            print("Usuario o libro no encontrado.")

    def revisar_prestamos_vencidos(self):
        # Revisa los préstamos vencidos comparando la fecha actual con la fecha de vencimiento
        fecha_actual = datetime.date.today()
        for prestamo in self.libros_prestados:
            libro, fecha_vencimiento = prestamo
            if fecha_vencimiento and fecha_vencimiento < fecha_actual:
                print(f"El libro '{libro.titulo}' prestado ha vencido.")

    def mostrar_libros_prestados(self):
        # Muestra la lista de libros prestados y su estado (prestado o devuelto)
        for prestamo in self.libros_prestados:
            libro, fecha_vencimiento = prestamo
            if fecha_vencimiento:
                print(f"Libro: {libro.titulo}, Prestado, Fecha de vencimiento: {fecha_vencimiento}")
            else:
                print(f"Libro: {libro.titulo}, Devuelto")

    # PUNTO 2.5: CREAR CARPETA INVENTARIO

    def guardar_inventario(self):
        # Crea la carpeta "inventario" SOLO si no existe, en caso contrario usará la existente
        if not os.path.exists("inventario"):
            os.makedirs("inventario")
        # Guarda la lista de libros disponibles en un archivo
        with open("inventario/libros_disponibles.txt", "w") as archivo_disponibles:
            for libro in self.libros_disponibles:
                archivo_disponibles.write(libro.titulo + "\n")

        # Guarda la lista de libros prestados en un archivo
        with open("inventario/libros_prestados.txt", "w") as archivo_prestados:
            for prestamo in self.libros_prestados:
                libro, _ = prestamo
                archivo_prestados.write(libro.titulo + "\n")

        print("El inventario ha sido guardado en la carpeta 'inventario'.")

    # Iteracion para recorrer la lista de usuarios, lista de libros prestados y disponibles y los préstamos.
    
    def menu_principal(self):
        # Menú principal de la biblioteca con opciones para interactuar con el sistema
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Ingresar nuevo usuario")
            print("2. Agregar libro disponible")
            print("3. Prestar libro")
            print("4. Aceptar devolución")
            print("5. Revisar préstamos vencidos")
            print("6. Mostrar libros prestados")
            print("7. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                self.ingresar_usuario(nombre_usuario)

            elif opcion == "2":
                titulo_libro = input("Ingrese el título del libro: ")
                self.agregar_libro_disponible(titulo_libro)

            elif opcion == "3":
                titulo_libro = input("Ingrese el título del libro a prestar: ")
                nombre_usuario = input("Ingrese el nombre del usuario que lo solicita: ")
                self.prestar_libro(titulo_libro, nombre_usuario)

            elif opcion == "4":
                titulo_libro = input("Ingrese el título del libro a devolver: ")
                nombre_usuario = input("Ingrese el nombre del usuario que lo devuelve: ")
                self.aceptar_devolucion(titulo_libro, nombre_usuario)

            elif opcion == "5":
                self.revisar_prestamos_vencidos()

            elif opcion == "6":
                self.mostrar_libros_prestados()

            elif opcion == "7":
                self.guardar_inventario()
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Por favor, ingrese un número válido.")

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()
# Ejecutar el menú principal
biblioteca.menu_principal()

# Ejercicio 3:
# Crear métodos que nos permitan abrir los archivos creados en el Ejercicio 2 y añadir o quitar elementos.

    def cargar_libros_disponibles(self):
        # Abre el archivo de libros disponibles y carga los libros en la lista correspondiente
        with open("inventario/libros_disponibles.txt", "r") as archivo_disponibles:
            for linea in archivo_disponibles:
                titulo_libro = linea.strip()
                self.agregar_libro_disponible(titulo_libro)
              
    def cargar_libros_prestados(self):
        # Abre el archivo de libros prestados y carga los libros en la lista correspondiente
        with open("inventario/libros_prestados.txt", "r") as archivo_prestados:
            for linea in archivo_prestados:
                titulo_libro = linea.strip()
                self.agregar_libro_prestado(titulo_libro)

    def agregar_libro_disponible(self, titulo):
        # Crea una instancia de la clase Libro y la agrega a la lista de libros disponibles de la biblioteca
        libro = Libro(titulo)
        self.libros_disponibles.insert(libro)
        print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

    def agregar_libro_prestado(self, titulo):
        # Crea una instancia de la clase Libro y la agrega a la lista de libros prestados de la biblioteca
        libro = Libro(titulo)
        self.libros_prestados.insert(libro)
        print(f"El libro '{titulo}' ha sido registrado como prestado.")

    def eliminar_libro_disponible(self, titulo):
        # Elimina un libro de la lista de libros disponibles de la biblioteca
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"El libro '{titulo}' ha sido eliminado de la lista de libros disponibles.")
                return
        print(f"No se encontró el libro '{titulo}' en la lista de libros disponibles.")

    def eliminar_libro_prestado(self, titulo):
        # Elimina un libro de la lista de libros prestados de la biblioteca
        for libro in self.libros_prestados:
            if libro.titulo == titulo:
                self.libros_prestados.remove(libro)
                print(f"El libro '{titulo}' ha sido eliminado de la lista de libros prestados.")
                return
        print(f"No se encontró el libro '{titulo}' en la lista de libros prestados.")

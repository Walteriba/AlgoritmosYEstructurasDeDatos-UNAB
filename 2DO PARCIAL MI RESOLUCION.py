from datetime import datetime, timedelta
import pickle
import os
#import Ejercicio1
#---------------------------------------- Lista de Productos Enlazada ---------------------------------------# 
class ListaEnlazada():
#-------- Clase Anidada - NODO ------------# 
    class _Nodo():
        def __init__(self,dato=None,prox=None):
            self.dato=dato
            self.prox=prox
        
        def __str__(self):
            return str(self.dato)

#----------- Métodos de la lista ----------- #
    def __init__(self):
        self.prim = None
        self.len = 0
        
    def lista_vacia(self): # Analogo a is_empty?
        """Devuelve un booleano segun el estado de la lista"""
        return self.prim is None
    
    def largo(self): # Analogo a __len__
        """Devuelve el largo de la lista"""
        return self.len
    
    def retornar_lista(self):
        """Devuelve la lista enlazada en forma de lista""" # Se puede modificar para que imprima cada nodo y/o ser la sobrecarga de __str__
        aux=self.prim
        laux=[]
        while (aux is not None):
            laux.append(aux.dato)
            aux=aux.prox
        return laux
    
    def index(self, x):
        """Devuelve la posición de la primera aparición de 'x' en la lista."""
        if self.lista_vacia():
            # Lanza una excepción si la lista está vacía
            raise ValueError('Lista vacía')  
        current = self.prim
        index = 0
        while current is not None:
            if current.dato == x:
                # Devuelve la posición si se encuentra el elemento
                return index  
            current = current.prox
            index += 1
        # Lanza una excepción si el elemento no se encuentra en la lista
        raise ValueError('Elemento no encontrado')  
    
    def insertar(self, i, x): #Analogo a insert
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError"""
        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")
        nuevo = self._Nodo(x)
        if i == 0:
        # Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
        # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
        # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1
    
    def insertar_al_final(self,dato): #Analogo a append
        """Inserta el dato al final de la lista"""    
        nodo=self._Nodo()
        nodo.dato=dato
        if self.lista_vacia():
            nodo.prox=self.prim
            self.prim=nodo
        else:
            anterior=self.prim
            actual=self.prim.prox
            while actual is not None:
                anterior=anterior.prox
                actual=actual.prox
            nodo.prox=actual
            anterior.prox=nodo
        self.len+=1
    
    def eliminar_por_dato(self,x):  #Analogo a Remove
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError"""
        if self.lista_vacia():
            raise ValueError("Lista vacía")
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act == None:
                raise ValueError("El valor no está en la lista.")
            # Descartar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1 
    
    def buscar_por_dato(self, dato):
        # Iniciar la búsqueda desde el primer nodo
        nodo_actual = self.prim
        # Realizar la búsqueda en la lista enlazada
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                # El producto ha sido encontrado
                return nodo_actual.dato
            nodo_actual = nodo_actual.prox
        # El producto no se encontró en la lista
        return None

    #Para que responda al Iterador
    def __iter__(self):
        return IteradorListaEnlazada(self)  
    
    #Para guardar y recuperar en un archivo
    def guardar_en_archivo(self, archivo):
        contenido = self.retornar_lista()
        with open(archivo, 'wb') as file: #se abre en modo escritura binaria
            pickle.dump(contenido, file) #se guarda en modo binario con este moludo

    @staticmethod
    def recuperar_de_archivo(archivo):
        lista = ListaEnlazada()
        with open(archivo, 'rb') as file:
            contenido = pickle.load(file)
            for dato in contenido:
                lista.insertar_al_final(dato)
        return lista

#----------------------------------- Iterador ---------------------------------------# 
class IteradorListaEnlazada:
    """Almacena el estado de una iteración sobre la ListaEnlazada."""
    def __init__(self, lista):
        """Crea un iterador para la lista dada"""
        self.lista = lista
        self.anterior = None
        self.actual = lista.prim  
    
    def __next__(self):
        if self.esta_al_final():
            raise StopIteration("No hay más elementos en la lista")
        dato = self.dato_actual()
        self.avanzar()
        return dato

    def avanzar(self):
        """Avanza la iteración un paso hacia adelante.
        Pre: la iteración no debe haber llegado al final.
        """
        self.anterior = self.actual
        self.actual = self.actual.prox

    def dato_actual(self):
        """Devuelve el elemento en la posición actual de iteración.
        Pre: la iteración no debe haber llegado al final.
        """
        return self.actual.dato

    def esta_al_final(self):
        """Devuelve verdadero si la iteración llegó al final de la lista."""
        return self.actual is None 



#----------------------------------------- Ejercicio 1 ----------------------------------------#
#1.1 

class Usuario():
    def __init__(self,nombre,direccion,telefono,email,fechadenacimiento):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.email=email
        self.fechadenacimiento=fechadenacimiento
        self.inbox=[]
        self.libros_en_posesion = ListaEnlazada()
    
    def modificar_datos(self,diccionario):
        for clave, valor in diccionario.items(): #Utilizo un diccionario
            if clave == 'nombre':
                self.nombre = valor
            elif clave == 'direccion':
                self.direccion = valor
            elif clave == 'telefono':
                self.telefono = valor
            elif clave == 'email':
                self.email = valor
            elif clave == 'fechadenacimiento':
                self.fechadenacimiento =valor

    def modificar_datos_sin_dicc(self, nuevo_nombre,nueva_direccion,nuevo_telefono,nuevo_email,nueva_fechadenacimiento): #sin diccionario
        self.nombre = nuevo_nombre
        self.direccion = nueva_direccion
        self.telefono = nuevo_telefono
        self.email = nuevo_email
        self.fechadenacimiento = nueva_fechadenacimiento

    def recibir_mensajes(self,mensaje):
        self.inbox.append(mensaje)
    
#1.2
class Libro():
    def __init__(self,nombre,edicion,fechadepublicacion,sinopsis):
        self.nombre=nombre
        self.edicion=edicion
        self.fechadepublicacion=fechadepublicacion
        self.sinopsis=sinopsis

    def modificar_datos(self,diccionario):
        for clave, valor in diccionario.items(): #Utilizo un diccionario
            if clave == 'nombre':
                self.nombre = valor
            elif clave == 'edicion':
                self.edicion = valor
            elif clave == 'fechadepublicacion':
                self.fechadepublicacion = valor
            elif clave == 'sinopsis':
                self.sinopsis = valor
                
                

#----------------------------------------- Ejercicio 2 ----------------------------------------#
#2.1
class Biblioteca:
    def __init__(self, nombre, direccion, telefono, email, horarios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.horarios = horarios
        self.libros_disponibles = ListaEnlazada() 
        self.usuarios = ListaEnlazada() #2.2
        self.libros_prestados = ListaEnlazada() #2.3
        self.cargar_inventario()

    def ingresar_usuario(self, usuario):
        self.usuarios.insertar_al_final(usuario)

#2.3
    def prestar_libro(self, objeto_usuario, objeto_libro): #como el libro se agrega al final, los libros con el modulo datetime ya estan ordenado por defecto, ya que el de mayor vencimiento estan ultimo
        if objeto_libro in self.libros_disponibles.retornar_lista():
            objeto_usuario.libros_en_posesion.insertar_al_final(objeto_libro)
            self.libros_disponibles.eliminar_por_dato(objeto_libro)
            fecha_vencimiento = datetime.now() + timedelta(days=30)
            self.libros_prestados.insertar_al_final((objeto_libro, objeto_usuario, fecha_vencimiento))
        else:
            print("El libro no está disponible.") #2.6

    def aceptar_devolucion(self, objeto_libro, objeto_usuario):
        for prestamo in self.libros_prestados.retornar_lista():
            if prestamo[0] == objeto_libro and prestamo[1] == objeto_usuario:
                objeto_usuario.libros_en_posesion.eliminar_por_dato(objeto_libro)
                self.libros_disponibles.insertar_al_final(objeto_libro)
                self.libros_prestados.eliminar_por_dato(prestamo)
                return
        print("El libro no fue prestado a este usuario.")

    def verificar_libros_vencidos(self):
        fecha_actual = datetime.now()
        for prestamo in self.libros_prestados.retornar_lista():
            libro, usuario, fecha_vencimiento = prestamo
            if fecha_actual > fecha_vencimiento:
                usuario.inbox.append(f"Tienes que devolver el {libro.nombre}. Gracias") #aca envio el mensaje al usuario

#2.4
    def iterar_usuarios(self):
        for usuario in self.usuarios:
            return usuario

    def iterar_libros_prestados(self):
        for libro_prestado in self.libros_prestados:
            return libro_prestado

    def iterar_libros_en_posesion(self,objeto_usuario): #paso el usuario, asi puedo iterar en la listaenlazda de libros_en_posesion
        for libro in objeto_usuario.libros_en_posesion:
            return libro
        
#2.5

    def guardar_inventario(self):
        if not os.path.exists('inventario'):
            os.makedirs('inventario')    
            self.libros_disponibles.guardar_en_archivo("inventario/libros_disponibles.txt")
            self.libros_prestados.guardar_en_archivo("inventario/libros_prestados.txt")

    def cargar_inventario(self):
        if os.path.exists("inventario/libros_disponibles.txt"):
            self.libros_disponibles = ListaEnlazada.recuperar_de_archivo("inventario/libros_disponibles.txt")
        if os.path.exists("inventario/libros_prestados.txt"):
            self.libros_prestados = ListaEnlazada.recuperar_de_archivo("inventario/libros_prestados.txt")


#----------------------------------------- Ejercicio 3 ----------------------------------------#
#CON ESTOS METODOS SE MANEJA SIN SER UN ARCHIVO BINARIO, QUE ME ESTABA TRAYENDO COMPLICACIONES A LA HORA DE CAMBIAR DATOS
def buscar_libro_por_titulo(titulo):
    with open('libros_disponibles.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == titulo:
                libro = Libro(data[0], data[1], data[2])
                return libro
    return None


def cargar_libros_disponibles():
    with open("inventario/libros_disponibles.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            titulo = datos[0]
            edicion = datos[1]
            fecha = datos[2]
            sinopsis = datos[3]
            libro = Libro(titulo, edicion, fecha, sinopsis)
            biblioteca.libros_disponibles.insertar_al_final(libro)

def cargar_libros_prestados():
    with open("inventario/libros_prestados.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            titulo = datos[0]
            usuario = datos[1]
            fecha_vencimiento = datos[2]
            libro = buscar_libro_por_titulo(titulo)  
            if libro is not None:
                biblioteca.libros_prestados.insertar_al_final((libro, usuario, fecha_vencimiento))

def actualizar_libro_disponible(libro):
    with open("inventario/libros_disponibles.txt", "r") as archivo:
        lineas = archivo.readlines()
    with open("inventario/libros_disponibles.txt", "w") as archivo:
        for linea in lineas:
            datos = linea.strip().split(",")
            titulo = datos[0]
            if titulo == libro.nombre:
                nueva_linea = f"{libro.nombre},{libro.edicion},{libro.fechadepublicacion},{libro.sinopsis}\n"
                archivo.write(nueva_linea)
            else:
                archivo.write(linea)

def actualizar_prestamo(prestamo):
    with open("inventario/libros_prestados.txt", "r") as archivo:
        lineas = archivo.readlines()
    with open("inventario/libros_prestados.txt", "w") as archivo:
        for linea in lineas:
            datos = linea.strip().split(",")
            titulo = datos[0]
            usuario = datos[1]
            if titulo == prestamo[0].nombre and usuario == prestamo[1].nombre: #aca chequeo que sea el mismo usuario y el mismo libro
                nueva_linea = f"{prestamo[0].nombre},{prestamo[1].nombre},{prestamo[2]}\n"
                archivo.write(nueva_linea)
            else:
                archivo.write(linea)


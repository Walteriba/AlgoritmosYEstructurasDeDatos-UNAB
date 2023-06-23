#Ejercicios:
#1) Escribir un algoritmo en donde el usuario debe escribir una frase, la cual será guardada
#en un archivo (de texto). Luego el algoritmo continuará solicitando frases a
#escribir/guardar hasta que el usuario escribe "FiNaL-de-ArChIvO" (sin comillas).

def escribir_en_archivo():
    archivo = open("frases.txt", "w")  # Abre el archivo en modo escritura
    while True:
        frase = input("Ingrese una frase (o escriba 'FiNaL-de-ArChIvO' para terminar): ")
        if frase == "FiNaL-de-ArChIvO":
            break
        archivo.write(frase + "\n")  # Escribe la frase en el archivo seguida de un salto de línea

    archivo.close()  # Cierra el archivo

escribir_en_archivo()


#2) Generar un archivo con un rango de enteros positivos que se ingresan por teclado.
#Recorrer el archivo y mostrarlos en pantalla en forma de listado.

def generar_archivo_enteros():
    archivo = open("enteros.txt", "w")  # Abre el archivo en modo escritura

    inicio = int(input("Ingrese el número de inicio del rango: "))
    fin = int(input("Ingrese el número final del rango: "))

    for num in range(inicio, fin + 1):
        archivo.write(str(num) + "\n")  # Escribe el número en el archivo seguido de un salto de línea

    archivo.close()  # Cierra el archivo

def mostrar_archivo_enteros():
    archivo = open("enteros.txt", "r")  # Abre el archivo en modo lectura

    contenido = archivo.read()  # Lee todo el contenido del archivo
    enteros = contenido.split("\n")  # Divide el contenido en una lista de enteros

    for entero in enteros:
        if entero != "":
            print(entero)  # Muestra el entero en pantalla

    archivo.close()  # Cierra el archivo

generar_archivo_enteros()
mostrar_archivo_enteros()




#3) Generar 2 archivos, el primero con números pares y el segundo con números impares
#(aleatorios/random). Luego generar un tercer archivo que contenga los números de
#ambos archivos ordenados de menor a mayor.

import random

def generar_archivo_pares():
    archivo_pares = open("pares.txt", "w")  # Abre el archivo de números pares en modo escritura

    for _ in range(10):
        num_par = random.randint(1, 100) * 2  # Genera un número par aleatorio entre 2 y 100
        archivo_pares.write(str(num_par) + "\n")  # Escribe el número par en el archivo seguido de un salto de línea

    archivo_pares.close()  # Cierra el archivo de números pares

def generar_archivo_impares():
    archivo_impares = open("impares.txt", "w")  # Abre el archivo de números impares en modo escritura

    for _ in range(10):
        num_impar = random.randint(1, 100) * 2 + 1  # Genera un número impar aleatorio entre 1 y 99
        archivo_impares.write(str(num_impar) + "\n")  # Escribe el número impar en el archivo seguido de un salto de línea

    archivo_impares.close()  # Cierra el archivo de números impares

def generar_archivo_ordenado():
    archivo_pares = open("pares.txt", "r")  # Abre el archivo de números pares en modo lectura
    archivo_impares = open("impares.txt", "r")  # Abre el archivo de números impares en modo lectura
    archivo_ordenado = open("ordenado.txt", "w")  # Abre el archivo de números ordenados en modo escritura

    numeros_pares = archivo_pares.readlines()  # Lee todas las líneas del archivo de números pares
    numeros_impares = archivo_impares.readlines()  # Lee todas las líneas del archivo de números impares

    numeros = []
    numeros.extend(numeros_pares)
    numeros.extend(numeros_impares)
    numeros = [int(num) for num in numeros]  # Convierte los números de string a enteros

    numeros.sort()  # Ordena los números de menor a mayor

    for num in numeros:
        archivo_ordenado.write(str(num) + "\n")  # Escribe cada número ordenado en el archivo seguido de un salto de línea

    archivo_pares.close()  # Cierra el archivo de números pares
    archivo_impares.close()  # Cierra el archivo de números impares
    archivo_ordenado.close()  # Cierra el archivo de números ordenados

generar_archivo_pares()
generar_archivo_impares()
generar_archivo_ordenado()



#4) Generar un archivo de agenda que contenga los datos típicos de una persona. Realizar
#los procedimientos de creación, modificación y búsqueda por nombre y apellido.

def crear_contacto():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el correo electrónico: ")

    contacto = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'email': email
    }

    archivo_agenda = open("agenda.txt", "a")  # Abre el archivo en modo append (agregar)

    linea_contacto = f"{contacto['nombre']},{contacto['apellido']},{contacto['telefono']},{contacto['email']}\n"
    archivo_agenda.write(linea_contacto)  # Escribe el contacto en una línea del archivo

    archivo_agenda.close()  # Cierra el archivo

def modificar_contacto():
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    apellido = input("Ingrese el apellido del contacto a modificar: ")

    archivo_agenda = open("agenda.txt", "r")  # Abre el archivo en modo lectura

    contactos = archivo_agenda.readlines()  # Lee todas las líneas del archivo

    encontrado = False

    for i in range(len(contactos)):
        datos_contacto = contactos[i].strip().split(',')
        if datos_contacto[0] == nombre and datos_contacto[1] == apellido:
            telefono = input("Ingrese el nuevo teléfono: ")
            email = input("Ingrese el nuevo correo electrónico: ")

            contactos[i] = f"{nombre},{apellido},{telefono},{email}\n"
            encontrado = True
            break

    archivo_agenda.close()  # Cierra el archivo

    if encontrado:
        archivo_agenda = open("agenda.txt", "w")  # Abre el archivo en modo escritura

        for contacto in contactos:
            archivo_agenda.write(contacto)  # Escribe cada contacto en el archivo

        archivo_agenda.close()  # Cierra el archivo
        print("Contacto modificado correctamente.")
    else:
        print("Contacto no encontrado.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    apellido = input("Ingrese el apellido del contacto a buscar: ")

    archivo_agenda = open("agenda.txt", "r")  # Abre el archivo en modo lectura

    contactos = archivo_agenda.readlines()  # Lee todas las líneas del archivo

    encontrado = False

    for contacto in contactos:
        datos_contacto = contacto.strip().split(',')
        if datos_contacto[0] == nombre and datos_contacto[1] == apellido:
            encontrado = True
            print("Contacto encontrado:")
            print(f"Nombre: {datos_contacto[0]}")
            print(f"Apellido: {datos_contacto[1]}")
            print(f"Teléfono: {datos_contacto[2]}")
            print(f"Email: {datos_contacto[3]}")
            break

    archivo_agenda.close()  # Cierra el archivo

    if not encontrado:
        print("Contacto no encontrado.")

# Menú principal
while True:
    print("\n== Agenda de Contactos ==")
    print("1. Crear un contacto")
    print("2. Modificar un contacto")
    print("3. Buscar un contacto")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == "1":
        crear_contacto()
    elif opcion == "2":
        modificar_contacto()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")



#5) Realizar un programa que muestre un archivo de texto, si el archivo es muy grande para
#entrar en la pantalla, el programa debe “paginarlo”.
#Nota: Funcionalidad similar al programa utilitario more (MS. D.O.S.) o less (Linux).

def paginar_archivo(archivo):
    with open(archivo, 'r') as file:
        contenido = file.readlines()
        num_lineas = len(contenido)
        lineas_por_pagina = 10
        pagina_actual = 1
        inicio = 0
        fin = lineas_por_pagina

        while inicio < num_lineas:
            print(f"=== Página {pagina_actual} ===")
            for linea in contenido[inicio:fin]:
                print(linea.rstrip())

            if fin >= num_lineas:
                break

            opcion = input("\nPresione 'Enter' para continuar o 'q' para salir: ")
            if opcion == 'q':
                break

            inicio = fin
            fin += lineas_por_pagina
            pagina_actual += 1


nombre_archivo = input("Ingrese el nombre del archivo a mostrar: ")
paginar_archivo(nombre_archivo)


#6) Realice un par de funciónes o métodos que permitan guardar y recuperar el contenido
#de una Lista Enlazada en un archivo.

import pickle

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def obtener_contenido(self):
        contenido = []
        nodo_actual = self.cabeza
        while nodo_actual:
            contenido.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return contenido

    def guardar_en_archivo(self, archivo):
        contenido = self.obtener_contenido()
        with open(archivo, 'wb') as file:
            pickle.dump(contenido, file)

    @staticmethod
    def recuperar_de_archivo(archivo):
        lista = ListaEnlazada()
        with open(archivo, 'rb') as file:
            contenido = pickle.load(file)
            for dato in contenido:
                lista.agregar(dato)
        return lista

# Crear una lista enlazada y agregar elementos
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Guardar la lista en un archivo
lista.guardar_en_archivo('lista_enlazada.dat')

# Recuperar la lista desde el archivo
lista_recuperada = ListaEnlazada.recuperar_de_archivo('lista_enlazada.dat')

# Imprimir el contenido de la lista recuperada
print(lista_recuperada.obtener_contenido())


#7) Escribir un algoritmo que permita listar los contenidos de un directorio.
#Nota: Funcionalidad similar al programa utilitario dir (MS. D.O.S.) o ls (Linux).

import os

def listar_contenidos_directorio(directorio):
    contenidos = os.listdir(directorio)
    for contenido in contenidos:
        print(contenido)

directorio = input("Ingrese la ruta del directorio a listar: ")
listar_contenidos_directorio(directorio)


#8) Escribir un algoritmo que permita mover un directorio--desde su path actual a un nuevo
#path--utiizando solamente los métodos/funciones: mkdir, rmdir, remove, y/o copyfile.
#Aclaración: NO utlizar otras funciones/métodos del módulo shutil.
import os
import shutil

def mover_directorio(origen, destino):
    # Verificar si el directorio de origen existe
    if not os.path.exists(origen):
        print("El directorio de origen no existe.")
        return

    # Verificar si el directorio de destino existe
    if os.path.exists(destino):
        print("El directorio de destino ya existe.")
        return

    # Crear el directorio de destino
    os.mkdir(destino)

    # Mover los archivos y subdirectorios del directorio de origen al directorio de destino
    for item in os.listdir(origen):
        origen_item = os.path.join(origen, item)
        destino_item = os.path.join(destino, item)
        if os.path.isfile(origen_item):
            shutil.copyfile(origen_item, destino_item)
            os.remove(origen_item)
        elif os.path.isdir(origen_item):
            shutil.copytree(origen_item, destino_item)
            shutil.rmtree(origen_item)

    # Eliminar el directorio de origen
    shutil.rmtree(origen)

    print("Directorio movido exitosamente.")

# Obtener los paths del directorio de origen y destino desde el usuario
directorio_origen = input("Ingrese el path del directorio de origen: ")
directorio_destino = input("Ingrese el path del directorio de destino: ")

# Mover el directorio
mover_directorio(directorio_origen, directorio_destino)



#9) Escribir un algoritmo en donde el usuario debe escribir una frase, la cual sera guardada
#en un archivo binario. Luego leer el archivo y mostrar su contenido por pantalla.

def escribir_frase_archivo(frase, archivo):
    with open(archivo, 'wb') as file:
        file.write(frase.encode())

def leer_archivo(archivo):
    with open(archivo, 'rb') as file:
        contenido = file.read().decode()
        return contenido

frase = input("Ingrese una frase: ")
archivo = "frase.bin"

# Escribir la frase en el archivo binario
escribir_frase_archivo(frase, archivo)

# Leer el archivo y mostrar su contenido
contenido = leer_archivo(archivo)
print("Contenido del archivo:")
print(contenido)


#10) Escribir un algoritmo en donde el usuario debe escribir una serie de numeros separados
#por coma (uno o mas), los cuales seran guardadados en un archivo binario. Luego el
#algoritmo continua solicitando numeros a guardar cuando el usuario escribe "0/0" (sin
#comillas). Luego leer el archivo y mostrar los datos por pantalla.

def escribir_numeros_archivo(numeros, archivo):
    with open(archivo, 'ab') as file:
        for numero in numeros:
            file.write(str(numero).encode())
            file.write(b',')
        file.write(b'\n')

def leer_archivo(archivo):
    with open(archivo, 'rb') as file:
        contenido = file.read().decode()
        return contenido

numeros = []
archivo = "numeros.bin"

while True:
    entrada = input("Ingrese una serie de números separados por coma (0/0 para finalizar): ")
    if entrada == "0/0":
        break
    numeros.extend(entrada.split(','))

# Escribir los números en el archivo binario
escribir_numeros_archivo(numeros, archivo)

# Leer el archivo y mostrar los datos por pantalla
contenido = leer_archivo(archivo)
print("Contenido del archivo:")
print(contenido)


#11) Elegir un tipo de dato de los que hemos visto (e.g. Mascota, Persona, etc.), ó crear uno
#nuevo. Luego escribir un algoritmo que permita guardar y leer una colección (i.e. tupla,
#listas, diccionario, etc.) de este tipo de dato en un archivo binario.

import pickle

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def guardar_personas(personas, archivo):
    with open(archivo, 'wb') as file:
        pickle.dump(personas, file)

def leer_personas(archivo):
    with open(archivo, 'rb') as file:
        personas = pickle.load(file)
        return personas

# Crear una lista de personas
personas = [
    Persona("Juan", 25),
    Persona("María", 30),
    Persona("Pedro", 35)
]

archivo = "personas.bin"

# Guardar la lista de personas en el archivo binario
guardar_personas(personas, archivo)

# Leer la lista de personas desde el archivo
personas_leidas = leer_personas(archivo)

# Mostrar las personas por pantalla
print("Personas guardadas:")
for persona in personas_leidas:
    print("Nombre:", persona.nombre)
    print("Edad:", persona.edad)
    print("------------")


    
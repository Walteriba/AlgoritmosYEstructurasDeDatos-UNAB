# 1.1:
# Crear una clase Usuario, está contendrá los datos básicos de una persona: 
# nombre, dirección, teléfono, email y fecha de nacimiento, 
# además de los métodos necesarios para cambiar estos datos.
# Además el usuario tendrá un método especial para "recibir mensajes".

# 1.2:
# Crear una clase Libro, está contendrá los datos referentes al libro: 
# nombre, edición, fecha de publicación, y sinopsis, 
# además de los métodos necesarios para cambiar estos datos.

#EJERCICIO 1.1:creamos la clase usuario y definimos el constructor para incializar
class usuario:
  def __init__(self, nombre, direccion, telefono, email, fecha_nac)
    self.nombre = nombre
    self.direccion = direccion
    self.telefono = telefono
    self.email = email
    self.fecha_nac = fecha_nac

#definimos los métodos para cambiar los datos del usuario
  
  def cambiar_direc(self, nueva_direc):
    self.direccion = nueva_direccion
    print("La dirección ha sido modificada.")
    
  def cambiar_tel(self, nuevo_tel):
    self.telefono = nuevo_telefono
    print("El numero de telefono ha sido modificado.")
    
  def cambiar_mail(self, nuevo_mail):
    self.mail = nuevo_mail
    print("El correo electrónico ha sido modificado.")

  def cambiar_fecha(self, nueva_fecha):
    self.fecha = nueva_fecha
    print("La fecha de nacimiento ha sido modificado.")

#le solicitamos al usuario que ingrese los datos:
  def solicitar_datos_usuario():
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    fecha_nac = input("Ingrese la fecha de nacimiento: ")
    return nombre, direccion, telefono, email, fecha_nac

#creamos el método para recibir mensajes
  def mensajeria(self, mensaje):
    print(f"Tenés un mensaje nuevo. Contenido: {mensaje}")

#y mostramos los datos en pantalla 

nombre, direccion, telefono, email, fecha_nacimiento = solicitar_datos_usuario()
usuario1 = Usuario(nombre, direccion, telefono, email, fecha_nacimiento)
print(usuario1)

#faltaria crear los métodos para que el usuario pueda modificar la información en caso de que lo requiera

# EJERCICIO 1.2
# Creamos la clase libro y la inicializamos con la informacion necesaria:

class libro:
  def __init__(self, nombre, edicion, fecha_publi, sinopsis):
    self.nombre = nombre
    self.edicion = edicion
    self.fecha_publi = fecha_publi
    self.sinopsis = sinopsis

#definimos los métodos para cambiar los datos
  def cambiar_nombre(self, nuevo_nombre):
    print("El nombre del libro se ha modificado.")

  def cambiar_edicion(self, nueva_fecha):
    self.fecha_publi = nueva_fecha
    print("La fecha de publicacion se ha modificado.")

  def cambiar_sinopsis(self, nueva_sinopsis)
    self.sinopsis(nueva_sinopsis)
    print("La sinopsis se ha modificado.")
    
  #finalmente los imprimimos en la pantalla junto a /n para que haga el salto de línea:
  def __str__(self):
    return f"Libro: {self.nombre}\nEdición: {self.edicion}\nFecha de publicación: {self.fecha_publicacion}\nSinopsis: {self.sinopsis}"

 #me gustaria agregarle para que el usuario pueda ingresar los datos, pero dudo llegar con el tiempo :c

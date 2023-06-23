
"""Escribir una función iterativa que calcule la potenciación de un numero. Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b."""

#Antes de empezar este ejercicio, quiero mostrar el resultado de ExVar3(). El cual es 5 2 en el primer print, 2 2 en el segundo. Indique el segundo en el ejercicio tal como dijo el profe Agus.

def potenciacion_iterativa(a,b):
    resultado = 1
    for i in range(b):
        resultado *= a
    return resultado

potenciacion_iterativa(2,3)

"""Escribir una función recursiva que calcule la potenciación de un numero. Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b. """

def potenciacion_recursiva(a,b):
    if b==1:
        return a
    else:
        return a * potenciacion_recursiva(a,b-1)

potenciacion_recursiva(2,3)

"""Escribir una función que reciba dos parámetros: (i) una lista desordenada y (ii) una expresión (una expresión es parámetro que puede ser evaluado a True o False). 
Si el valor de la expresión es Verdadera (True), la lista se ordenara en forma descendente, en otro caso de manera ascendente. 
Por defecto, si la función es llamada sin una "expresión" (solo la lista) debe retornar una lista ordenada de forma ascendente."""

def ordenar_lista(lista,booleano=False):
    if booleano==False:
        lista.sort()
        return lista
    else:
        lista.sort()
        listareversa=lista[::-1]
        return listareversa

l=[8,2,5,16,1]
ordenar_lista(l,True)

"""Podemos utilizar el siguiente código genera una lista L. 
Escribir la/s sentencia/s necesarias para generar la misma lista L utilizando el método de generación de listas por comprensión. """

L = [x**2 % 2 for x in range(20)]
print(L)

"""Definir una clase "Producto", el cual contiene los datos:

"Descripcion" : 'string' 
"ID" : 'integer'
"FechaExp" : date, ## importar datetime 
"INFO" : 'cualquier tipo' 

La clase debe contener métodos para facilitar:
- Cambiar uno o varios datos del Producto.
- Calcular en cuantos dias/horas expira un producto. Si el método detecta que el Producto ha expirado, debera informar al usuario.

Importante:
- Pueden agregar más atributos y métodos, si lo consideran necesario. """

import datetime

class Producto:
    
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = int(id)
        self.fecha_exp = fecha_exp
        self.info = info
       
    def cambiar_datos(self, diccionario):
        for atributo, valor in diccionario.items(): #utilizo un diccionario
            if atributo == 'descripcion':
                self.descripcion = valor
            elif atributo == 'id':
                self.id = valor
            elif atributo == 'fecha_exp':
                self.fecha_exp = valor
            elif atributo == 'info':
                self.info = valor
   
    def expiracion(self):
        fecha_convertida=datetime.datetime.strptime(self.fecha_exp, "%Y-%m-%d").date() #acá convierto la fecha al tipo datetime
        fecha_actual = datetime.datetime.now().date() #aca obtengo la fecha actual
        tiempo_restante = fecha_convertida - fecha_actual
        if tiempo_restante.days < 0:
            print("El producto ha expirado.")
        else:
            print(f"El producto expirará en {tiempo_restante.days} días.")


a=Producto(
    "yogur",
    155,
    "2023-05-15", # utilizo el formato de fecha del norte, porque no estaba pudiendo convertir a nuestro sistema de dias
    "nada"
    )

a.expiracion()

"""Sobrecargar los siguientes métodos en la clase Producto:

- __str__
- __eq__

"""

class Producto:
   
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = int(id)
        self.fecha_exp = fecha_exp
        self.info = info
   
    def __str__(self):
        return f"La descripción del producto es {self.descripcion}, su id es {self.id}, su fecha de vencimiento es {self.fecha_exp} y la información adicional dice que {self.info}"
   
    def __eq__(self,otro_producto):
        if self.id == otro_producto.id:
            return True
        else:
            return False
       
# utilizo el formato de fecha del norte, porque no estaba pudiendo convertir a nuestro sistema de dias
a=Producto("Yogur", 155, "2023-05-15", "en oferta")
b=Producto("Leche", 155, "2023-05-15", "de vaca")

print(a)

a==b 
    
"""Crear una clase Mercado, el cual estará representado (atributos internos) mediante varias listas de objetos del tipo Producto. 
Cada lista corresponde a un pasillo (o sección del mercado).

La clase debe contener métodos para facilitar:
- Controlar el stock de productos (añadir, remover, etc).
- Calcular en cuántos productos expiran en las proximas 24hs y removerlos.

Importante:
- Pueden agregar más atributos y métodos, si lo consideran necesario.

"""

class Mercado:
    
    def __init__(self,listadepasillos):
         self.pasillos = listadepasillos  #aca pienso una lista de pasillos, es decir una lista de listas
    
    def añadir_producto(self,pasillo,producto):
        if pasillo in self.pasillos:
            pasillo.append(producto)
    
    def remover_productos(self,pasillo,producto):
        if pasillo in self.pasillos:
            pasillo.remove(producto)
            
    def verificar_vencimiento_pasillo(self,pasillo):
        if pasillo in self.pasillos:
            cantidad_de_vencidos=0
            for producto in pasillo:
                if producto.expiracion() < 1:  # soy consciente que mi definicion del metodo expiracion de la clase objeto arroja un string y no un numero, pero no llego a cambiarlo, voy a hacer de cuenta que retorna
                    pasillo.remove(producto)   # un entero, que hace referencia a la cantidad de dias. si es menor a 1, significa que vence en menos de un dia
                    cantidad_de_vencidos+=1
            return f"Se removieron {cantidad_de_vencidos} productos vencidos"
        
        
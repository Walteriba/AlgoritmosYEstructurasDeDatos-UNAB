## PARCIAL

# Ej 1: Dadas las siguientes funciones, cual es el resultado de ejecutar ExVar1(), ExVar2() y ExVar3()

x, y = 5, 2
def ExVar1():
    print(x,y)

def ExVar2():
    x=2
    def ExVar21():
        nonlocal x
        global y
        y, x = x, y
        print(x,y)
    ExVar21()

def ExVar3():
    def ExVar31():
        global x,y
        x,y = y,x
    ExVar31()
    print(y,x)


# ExVar1() --> 5,2.  2,2   --
# ExVar2() --> 5,2   2,2.  --
# ExVar3() --> 5,2.  2,2   -- 

# La función ExVar1() imprimirá los valores de x e y, que son 5 y 2 respectivamente, ya que son variables globales. La función ExVar2() no imprimirá nada, ya que la variable x se define como local dentro de la función ExVar21() y no se utiliza en la función principal; Pero si corremos la función completa vemos que imprime 2 y 2 en cada variable. La función ExVar3() intercambiará los valores de x e y utilizando una función interna llamada ExVar31(). Luego, imprimirá los valores de y y x, que serán 5 y 2 respectivamente antes de la llamada a la función ExVar31(), y 2 y 5 después de la llamada a la función. Esto se debe a que se utilizó la palabra clave global para las variables x e y dentro de la función ExVar31(), lo que les permite ser modificadas en el ámbito global.

# Ej 2: Escribir una función iterativa que calcule la potenciación de un numero. Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b.
# Una solución iterativa ingenua para calcular pow(x, n) en Python es la siguiente: 

def power(x, n):
    pow = 1
    for i in range(n):
        pow = pow * x
    return pow

# Esta función inicializa el resultado en 1 y multiplica x exactamente n veces usando un bucle for
# Otra solución iterativa para calcular la potencia de un número en Python es la siguiente:

def power(x, n):
    pow = 1
    while n > 0:
        if n % 2 == 0:
            x = x * x
            n = n / 2
        else:
            pow = pow * x
            n = n - 1
    return pow

# Esta función utiliza el algoritmo de exponenciación binaria para calcular la potencia de un número

# Ej 3: Escribir una función recursiva que calcule la potenciación de un numero. Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b. 
# Una posible solución recursiva para calcular la potenciación de un número en Python es la siguiente:

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

# Esta función recibe dos parámetros a y b, y devuelve el valor de a elevado a la potencia b. Si b es igual a cero, la función devuelve 1. En caso contrario, la función devuelve a multiplicado por el resultado de llamar a la función power con los mismos valores de a y b-1. De esta forma, la función se llama recursivamente hasta que b sea igual a cero.
# Por ejemplo, si llamamos a la función con los valores a=2 y b=3, la función devolverá el valor 8, ya que 2 elevado a la potencia 3 es igual a 8.


# Ej 4: Escribir una función que reciba dos parámetros: (i) una lista desordenada y (ii) una expresión (una expresión es parámetro que puede ser evaluado a True o False). Si el valor de la expresión es Verdadera (True), la lista se ordenara en forma descendente, en otro caso de manera ascendente. Por defecto, si la función es llamada sin una "expresión" (solo la lista) debe retornar una lista ordenada de forma ascendente.
# Para resolver este problema, podemos definir una función que reciba dos parámetros: una lista desordenada y una expresión que puede ser evaluada a True o False. Si la expresión es verdadera, la lista se ordenará en forma descendente, en otro caso de manera ascendente. Por defecto, si la función es llamada sin una expresión (solo la lista), debe retornar una lista ordenada de forma ascendente.
# Para implementar esta función, podemos utilizar el método sort() de Python, que nos permite ordenar una lista en orden ascendente o descendente. Si queremos ordenar la lista en orden descendente, podemos pasar el parámetro reverse=True al método sort(). Si queremos ordenar la lista en orden ascendente, podemos pasar el parámetro reverse=False o simplemente no pasar ningún parámetro.
# A continuación se muestra una posible implementación de esta función:

def ordenar_lista(lista, expresion=None):
    if expresion is None:
        lista.sort()
    elif expresion:
        lista.sort(reverse=True)
    else:
        lista.sort()
    return lista

# Esta función recibe dos parámetros: lista y expresion. Si expresion es None, la función ordena la lista en forma ascendente utilizando el método sort() sin ningún parámetro adicional. Si expresion es verdadera, la función ordena la lista en forma descendente utilizando el método sort() con el parámetro reverse=True. Si expresion es falsa, la función ordena la lista en forma ascendente utilizando el método sort() sin ningún parámetro adicional.
# Por ejemplo, si queremos ordenar la lista [3][1][4][1][5][9][2] en forma ascendente por defecto, podemos llamar a la función de la siguiente manera:

ordenar_lista([3, 1, 4, 1, 5, 9, 2])

# Esto nos devolverá la lista [1][1][2][3][4][5][9].
# Si queremos ordenar la misma lista en forma descendente si el número de elementos es mayor que 5 (por ejemplo), podemos llamar a la función de la siguiente manera:

ordenar_lista([3, 1, 4, 1, 5, 9, 2], len(lista) > 5)

# Esto nos devolverá la lista [9][5][4][3][2][1][1].
# En resumen, para resolver este problema podemos definir una función que reciba dos parámetros: una lista desordenada y una expresión que puede ser evaluada a True o False. Si la expresión es verdadera, la lista se ordenará en forma descendente; en otro caso de manera ascendente. Por defecto (si no se proporciona ninguna expresión), la función debe retornar una lista ordenada de forma ascendente. Podemos utilizar el método sort() de Python para ordenar la lista y los condicionales para determinar si se debe ordenar en forma ascendente o descendente.


# Ej 5: Podemos utilizar el siguiente código genera una lista L. Escribir la/s sentencia/s necesarias para generar la misma lista L utilizando el método de generación de listas por comprensión. 
x, L = 0, []
while x<20:
    L.append(x**2 % 2)
    x+=1

# Para generar la lista L utilizando el método de generación de listas por comprensión, podemos utilizar la siguiente sentencia:

L = [x**2 % 2 for x in range(20)]

# Esta sentencia es equivalente al siguiente código utilizando un bucle while y el método append():

x, L = 0, []
while x < 20:
    L.append(x**2 % 2)
    x += 1

# La sintaxis de la comprensión de listas es [expression for item in iterable], donde expression es la expresión que se evalúa para cada elemento en iterable, y item es una variable que toma el valor de cada elemento en iterable. En este caso, iterable es range(20), que genera los números del 0 al 19, y expression es x**2 % 2, que calcula el resto de la división de x**2 entre 2 para cada valor de x.
# Por lo tanto, la sentencia L = [x**2 % 2 for x in range(20)] genera una lista L que contiene los valores [0][1][0][1][0][1][0][1][0][1][0][1][0][1][0][1][0][1][0][1], que es equivalente a la lista generada por el código original.


# Ej 6: Sobrecargar los siguientes métodos en la clase Producto:

#  __str__
#  __eq__

# Para sobrecargar los métodos __str__ y __eq__ en la clase Producto en Python, podemos seguir los siguientes pasos:
# Para sobrecargar el método __str__, debemos definir una función con ese nombre dentro de la clase Producto. Esta función debe devolver una cadena que represente al objeto de la clase. Por ejemplo:

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# En este ejemplo, la función __str__ devuelve una cadena que contiene el nombre y el precio del producto.
# Para sobrecargar el método __eq__, debemos definir una función con ese nombre dentro de la clase Producto. Esta función debe recibir como parámetro otro objeto de la misma clase y devolver True si ambos objetos son iguales o False en caso contrario. Por ejemplo:

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre == other.nombre and self.precio == other.precio
        return False

# En este ejemplo, la función __eq__ compara el nombre y el precio del producto con los del otro objeto recibido como parámetro. Si ambos son iguales, devuelve True, de lo contrario devuelve False.
# Con estas dos funciones sobrecargadas, podemos utilizar los operadores == y != para comparar objetos de la clase Producto. Por ejemplo:

p1 = Producto("Leche", 2.5)
p2 = Producto("Leche", 2.5)
p3 = Producto("Pan", 1.0)

print(p1 == p2)  # True
print(p1 == p3)  # False
print(p1 != p2)  # False
print(p1 != p3)  # True



# Ej 7: Definir una clase "Producto", el cual contiene los datos:

# "Descripcion" : 'string' 
# "ID" : 'integer'
# "FechaExp" : date, ## importar datetime 
# "INFO" : 'cualquier tipo' 
# 
# La clase debe contener métodos para facilitar:
# - Cambiar uno o varios datos del Producto.
# - Calcular en cuantos dias/horas expira un producto. Si el método detecta que el Producto ha expirado, debera informar al usuario.
# 
# Importante:
# - Pueden agregar más atributos y métodos, si lo consideran necesario. 

# Para definir una clase "Producto" en Python que contenga los datos "Descripcion", "ID", "FechaExp" y "INFO", podemos seguir los siguientes pasos:
# Definir la clase "Producto" con los atributos mencionados:

import datetime

class Producto:
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = id
        self.fecha_exp = fecha_exp
        self.info = info

# En este ejemplo, la clase "Producto" tiene cuatro atributos: "descripcion", "id", "fecha_exp" y "info". El atributo "fecha_exp" es de tipo "date" y se importa del módulo "datetime".
# Agregar métodos para cambiar uno o varios datos del producto:

class Producto:
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = id
        self.fecha_exp = fecha_exp
        self.info = info

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_info(self, nueva_info):
        self.info = nueva_info

    def cambiar_fecha_exp(self, nueva_fecha_exp):
        self.fecha_exp = nueva_fecha_exp

# En este ejemplo, se agregaron tres métodos para cambiar la descripción, la información y la fecha de expiración del producto.
# Agregar un método para calcular en cuántos días/horas expira un producto:

class Producto:
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = id
        self.fecha_exp = fecha_exp
        self.info = info

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_info(self, nueva_info):
        self.info = nueva_info

    def cambiar_fecha_exp(self, nueva_fecha_exp):
        self.fecha_exp = nueva_fecha_exp

    def calcular_tiempo_expiracion(self):
        tiempo_restante = self.fecha_exp - datetime.date.today()
        if tiempo_restante.days < 0:
            print("El producto ha expirado")
        else:
            print(f"Faltan {tiempo_restante.days} días y {tiempo_restante.seconds//3600} horas para que expire el producto")

# En este ejemplo, se agregó un método llamado "calcular_tiempo_expiracion" que calcula el tiempo restante para que expire el producto. Si el tiempo restante es negativo, significa que el producto ya ha expirado y se informa al usuario.
# Con estos métodos definidos en la clase "Producto", podemos crear objetos de esta clase y utilizar sus métodos para cambiar sus datos y calcular su tiempo de expiración. Por ejemplo:

p1 = Producto("Leche", 1, datetime.date(2023, 5, 31), "Leche entera")
print(p1.descripcion)  # Leche
p1.cambiar_descripcion("Leche descremada")
print(p1.descripcion)  # Leche descremada

p1.calcular_tiempo_expiracion()  # Faltan 12 días y 14 horas para que expire el producto
p1.cambiar_fecha_exp(datetime.date(2023, 5, 18))
p1.calcular_tiempo_expiracion()  # El producto ha expirado

# Ej 6':
# Como vimos antes, podemos seguir los siguientes pasos para sobrecargar los métodos:
# Primero el método __str__:

class Producto:
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = id
        self.fecha_exp = fecha_exp
        self.info = info

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_info(self, nueva_info):
        self.info = nueva_info

    def cambiar_fecha_exp(self, nueva_fecha_exp):
        self.fecha_exp = nueva_fecha_exp

    def calcular_tiempo_expiracion(self):
        tiempo_restante = self.fecha_exp - datetime.date.today()
        if tiempo_restante.days < 0:
            print("El producto ha expirado")
        else:
            print(f"Faltan {tiempo_restante.days} días y {tiempo_restante.seconds//3600} horas para que expire el producto")

    def __str__(self):
        return f"{self.descripcion} ({self.id})"

# Segundo, el método __eq__:

class Producto:
    def __init__(self, descripcion, id, fecha_exp, info):
        self.descripcion = descripcion
        self.id = id
        self.fecha_exp = fecha_exp
        self.info = info

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_info(self, nueva_info):
        self.info = nueva_info

    def cambiar_fecha_exp(self, nueva_fecha_exp):
        self.fecha_exp = nueva_fecha_exp

    def calcular_tiempo_expiracion(self):
        tiempo_restante = self.fecha_exp - datetime.date.today()
        if tiempo_restante.days < 0:
            print("El producto ha expirado")
        else:
            print(f"Faltan {tiempo_restante.days} días y {tiempo_restante.seconds//3600} horas para que expire el producto")

    def __str__(self):
        return f"{self.descripcion} ({self.id})"

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.id == other.id
        return False

# verificamos probando:

p1 = Producto("Leche", 1, datetime.date(2023, 5, 31), "Leche entera")
p2 = Producto("Queso", 2, datetime.date(2023, 6, 30), "Queso fresco")

print(p1 == p2)  # False

p3 = Producto("Leche descremada", 1, datetime.date(2023, 5, 31), "Leche descremada")

print(p1 == p3)  # True

print(p1)  # Leche (1) 

# Ej 8: Crear una clase Mercado, el cual estará representado (atributos internos) mediante varias listas de objetos del tipo Producto. Cada lista corresponde a un pasillo (o sección del mercado).

# La clase debe contener métodos para facilitar:
# - Controlar el stock de productos (añadir, remover, etc).
# - Calcular en cuántos productos expiran en las proximas 24hs y removerlos.
# 
# Importante:
# - Pueden agregar más atributos y métodos, si lo consideran necesario. 
# 

# Definimos la clase Mercado como sigue:

class Mercado:
    def __init__(self):
        self.pasillo1 = []
        self.pasillo2 = []
        self.pasillo3 = []

    def agregar_producto(self, producto, pasillo):
        if pasillo == 1:
            self.pasillo1.append(producto)
        elif pasillo == 2:
            self.pasillo2.append(producto)
        elif pasillo == 3:
            self.pasillo3.append(producto)

    def remover_producto(self, producto, pasillo):
        if pasillo == 1:
            self.pasillo1.remove(producto)
        elif pasillo == 2:
            self.pasillo2.remove(producto)
        elif pasillo == 3:
            self.pasillo3.remove(producto)

    def calcular_expiracion(self):
        expiran_en_24h = []
        for producto in self.pasillo1 + self.pasillo2 + self.pasillo3:
            tiempo_restante = producto.fecha_exp - datetime.date.today()
            if tiempo_restante.days <= 1:
                expiran_en_24h.append(producto)
                self.remover_producto(producto, pasillo=producto.pasillo)
        return expiran_en_24h

# En esta implementación de la clase "Mercado", definimos tres listas para representar las diferentes secciones del mercado. También definimos métodos para agregar y remover productos de estas listas, y un método para calcular qué productos expirarán en las próximas 24 horas y eliminarlos de sus respectivas listas.
# Podemos agregar más atributos y métodos a esta clase según sea necesario. Por ejemplo, podríamos agregar un método para calcular el stock total de productos en el mercado o un método para ordenar los productos por su fecha de vencimiento.
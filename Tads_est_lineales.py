#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estructuras de datos Lineales
"""

### LISTA ###

class _Nodo(object):
    def __init__(self, dato=None, prox = None):
        self.dato = dato
        self.prox = prox 
    def __str__(self):
        return str(self.dato)
 

class ListaEnlazada(object):
    " Modela una lista enlazada, compuesta de Nodos. "
    def __init__(self):
        """ Crea una lista enlazada vacía. """
    # prim: apuntará al primer nodo - None con la lista vacía 
        self.prim = None
    # len: longitud de la lista - 0 con la lista vacía 
        self.len = 0

class ListaEnlazada(object):
    " Modela una lista enlazada, compuesta de Nodos. "
    def __init__(self):
        """ Crea una lista enlazada vacía. """
    # prim: apuntará al primer nodo - None con la lista vacía 
        self.prim = None
    # len: longitud de la lista - 0 con la lista vacía 
        self.len = 0
    
    def __iter__(self):
        " Devuelve el iterador de la lista. " 
        return _IteradorListaEnlazada(self.prim)
    
    def pop(self, i = None):
        """ Elimina el nodo de la posición i, y devuelve el dato contenido.
            Si i está fuera de rango, se levanta la excepción IndexError. Si no se recibe la posición, devuelve el último elemento. """
    # Si no se recibió i, se devuelve el último.
        if i is None:
            i = self.len - 1
     # Verificación de los límites
            if not (0 <= i < self.len):
                raise IndexError("Índice fuera de rango")
# Caso particular, si es el primero,
# hay que saltear la cabecera de la lista 
        if i==0:
            dato = self.prim.dato 
            self.prim = self.prim.prox
     # Para todos los demás elementos, busca la posición
        else:
            n_ant = self.prim
            n_act = n_ant.prox
        for pos in range(1, i):
            n_ant = n_act 
            n_act = n_ant.prox
         # Guarda el dato y elimina el nodo a borrar
            dato = n_act.dato 
            n_ant.prox = n_act.prox
     # hay que restar 1 de len
            self.len -= 1
     # y devolver el valor borrado
        return dato
 

    def remove(self, x):
        """ Borra la primera aparición del valor x en la lista.
            Si x no está en la lista, levanta ValueError """
        if self.len == 0:
        # Si la lista está vacía, no hay nada que borrar. 
            raise ValueError("Lista vacía")
        # Caso particular, x esta en el primer nodo
        elif self.prim.dato == x:
        # Se descarta la cabecera de la lista 
            self.prim = self.prim.prox
        # En cualquier otro caso, hay que buscar a x
        else:
        # Obtiene el nodo anterior al que contiene a x (n_ant) n_ant = self.prim
            n_act = n_ant.prox
            while n_act != None and n_act.dato != x:
                n_ant = n_act 
                n_act = n_ant.prox
            # Si no se encontró a x en la lista, levanta la excepción
        if n_act == None:
            raise ValueError("El valor no está en la lista.")
    # Si encontró a x, debe pasar de n_ant -> n_x -> n_x.prox # a n_ant -> n_x.prox
        else:
            n_ant.prox = n_act.prox
        # Si no levantó excepción, hay que restar 1 del largo
            self.len -= 1

    def insert(self, i, x):
        """ Inserta el elemento x en la posición i.
            Si la posición es inválida, levanta IndexError """
        if (i > self.len) or (i < 0): # error
            raise IndexError("Posición inválida") # Crea nuevo nodo, con x como dato:
        nuevo = _Nodo(x)
        # Insertar al principio (caso particular)
        if i==0:
    # el siguiente del nuevo pasa a ser el que era primero 
            nuevo.prox = self.prim
    # el nuevo pasa a ser el primero de la lista
            self.prim = nuevo
        # Insertar en cualquier lugar > 0
        else:
    # Recorre la lista hasta llegar a la posición deseada n_ant = self.prim
            for pos in range(1,i):
                n_ant = n_ant.prox
    # Intercala nuevo y obtiene n_ant -> nuevo -> n_ant.prox
                nuevo.prox = n_ant.prox 
                n_ant.prox = nuevo
        # En cualquier caso, incrementar en 1 la longitud
        self.len += 1

# IERADOR LISTA #

class _IteradorListaEnlazada(object):
    " Iterador para la clase ListaEnlazada "
 
    def __init__(self, prim):
        """ Constructor del iterador.
            prim es el primer elemento de la lista. """
        self.actual = prim

    def __next__(self):
        """ Devuelve uno a uno los elementos de la lista. """
        if self.actual == None:
            raise StopIteration("No hay más elementos en la lista")
        # Guarda el dato
        dato = self.actual.dato
        # Avanza en la lista
        self.actual = self.actual.prox
        # Devuelve el dato
        return dato

 
## Esto debe ir en la Clase ListaEnlazada ## 
#def __iter__(self):
#    " Devuelve el iterador de la lista. " 
#    return _IteradorListaEnlazada(self.prim)



### PILAS ###

class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y 
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
# La pila vacía se representa con una lista vacía 
        self.items=[]

    def push(self, x):
        """ Agrega el elemento x a la pila. """
# Apilar es agregar al final de la lista. 
        self.items.append(x)

# Desapilar usará el método pop de lista que hace exactamente lo requerido
    def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

# El método para indicar si se trata de una pila vacía.
    def is_empty(self):
        """ Devuelve True si la lista está vacía, False si no. """ 
        return self.items == []


# Retorna el *tope* de la Pila
## Modificar ##
    def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def top(P):
        if P.is_empty() : pass
        x = P.pop
        P.push(x)
        return x

 

#####################

"""
class ArrayStack:
”””LIFO Stack implementation using a Python list as underlying storage.”””
def init (self):
”””Create an empty stack.””” self. data = [ ]
    # nonpublic list instance ”””Return the number of elements in the stack.”””
 def len (self): return len(self. data)
     def is empty(self):
”””Return True if the stack is empty.””” return len(self. data) == 0
def push(self, e):
”””Add element e to the top of the stack.”””
self. data.append(e) # new item stored at end of list
def top(self):
”””Return (but do not remove) the element at the top of the stack.
Raise Empty exception if the stack is empty. ”””
if self.is empty():
    raise Empty( Stack is empty ) return self. data[−1]
# the last item in the list
   def pop(self):
”””Remove and return the element from the top of the stack (i.e., LIFO).
Raise Empty exception if the stack is empty. ”””
if self.is empty():
raise Empty( Stack is empty )
return self. data.pop( ) # remove last item from list
"""

#########################


### COLAS ###

class Cola:
    """ Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero en ser desencolado. """

    def __init__(self):
        """ Crea una cola vacía. """
# La cola vacía se representa por una lista vacía 
        self.items=[]
    
    
#El método encolar se implementará agregando el nuevo elemento al final de la lista:
    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """ 
        self.items.append(x)

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. """
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
            
#Por último, el método es_vacia, que indicará si la cola está o no vacía.
    def es_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no.""" 
        return self.items == []




########################
"""
class ArrayQueue:
”””FIFO queue implementation using a Python list as underlying storage.””” DEFAULT CAPACITY = 10 # moderate capacity for all new queues
def init (self):
”””Create an empty queue.”””
self. data = [None]   ArrayQueue.DEFAULT CAPACITY self. size = 0
self. front = 0
def len (self):
”””Return the number of elements in the queue.””” return self. size
def is empty(self):
”””Return True if the queue is empty.””” return self. size == 0
def first(self):
”””Return (but do not remove) the element at the front of the queue.
Raise Empty exception if the queue is empty. ”””
if self.is empty():
raise Empty( Queue is empty ) return self. data[self. front]
def dequeue(self):
”””Remove and return the first element of the queue (i.e., FIFO).
                     Raise Empty exception if the queue is empty. ”””
if self.is empty():
raise Empty( Queue is empty )
answer = self. data[self. front]
self. data[self. front] = None
self. front = (self. front + 1) % len(self. data) self. size −= 1
return answer
# help garbage collection

def enqueue(self, e):
”””Add an element to the back of queue.””” if self. size == len(self. data):
self. resize(2   len(self.data)) # double the array size avail = (self. front + self. size) % len(self. data)
self. data[avail] = e
self. size += 1
def   resize(self, cap): # we assume cap >= len(self) ”””Resize to a new list of capacity >= len(self).”””
        old = self. data
self. data = [None]   cap walk = self. front
for k in range(self. size):
self. data[k] = old[walk]
walk = (1 + walk) % len(old) self. front = 0
# keep track of existing list
# allocate list with new capacity
# only consider existing elements # intentionally shift indices
# use old size as modulus
# front has been realigned
"""


###########################



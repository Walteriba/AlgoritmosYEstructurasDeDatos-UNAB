"""
1)Modelar una panaderia (Clase y objetos)
2)Agregar a la panaderia una lista de productos (Listas enlazadas)
3)Agregar a la panaderia una cola de clientes (Colas y pilas)
4)Generar un iterador para la lista de productos y la cola de clientes (Iteradores)
5)Guardar la lista de productos en un archivo (Archivos)
6)Mover un directorio(Archivos (Ej. 8, Pract. 11))
Extra: importar uno o varios módulos
"""


#-------- Lista de Productos Enlazada ------------# 
class ListaProductosEnlazada():
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
    
    def pop(self, i = None):
        """ Elimina el nodo de la posición i, y devuelve el dato contenido.
            Si i está fuera de rango, se levanta la excepción IndexError. Si no se recibe la posición, devuelve el último elemento. """
        if self.lista_vacia():
            raise ValueError("Lista vacía")
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            #Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo    
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato  
    
    #Para que responda al Iterador
    def __iter__(self):
        return IteradorListaEnlazada(self)  


#-------- Cola de la Panadería ------------# 
class ColaClientes():
    """ Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero en ser desencolado. """

    def __init__(self,cola=[]):
        """ Se le pasa una cola, sino crea una vacia """
        # La cola vacía se representa por una lista vacía 
        self.cola = cola
        
    def __str__(self):
        return str(self.cola)
    
    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """ 
        self.cola.append(x)

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. """
        try:
            return self.cola.pop(0)
        except:
            raise ValueError("La cola está vacía")
            
    #Por último, el método es_vacia, que indicará si la cola está o no vacía.
    def cola_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no.""" 
        return self.items == []
 
    
#-------- Iterador ------------# 
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
    
    def insertar(self, x):
        """Insertar un elemento en el lugar de la iteración actual.
        Una vez insertado, el nuevo elemento será el actual de la iteración,
        y el elemento que antes era el actual será el siguiente.
        """
        nuevo = ListaProductosEnlazada._Nodo(x)
        if self.anterior:
            nuevo.prox = self.anterior.prox
            self.anterior.prox = nuevo
        else:
            nuevo.prox = self.lista.prim
            self.lista.prim = nuevo
        self.actual = nuevo
        
    def eliminar(self):
        dato = self.dato_actual()
        if self.anterior:
            self.anterior.prox = self.actual.prox
            self.actual = self.anterior.prox
        else:
            self.lista.prim = self.actual.prox
            self.actual = self.lista.prim
        return dato
    
    """
    #Forma de uso
    
    it = IteradorListaEnlazada(l)
    while not it.esta_al_final():
    print(it.dato_actual())
    it.avanzar()
    
    if 'ñ' in it.dato_actual()
    it.eliminar()
    # luego de eliminar ya estamos en el nodo siguiente
    else:
    it.avanzar()
    """


#-------- Panaderia ------------# 
class Panaderia:
    def __init__(self):
        pass
          


#----------- Probando el código ----------- #

print("PROBANDO LISTAPRODUCTOSENLAZADA")
l=ListaProductosEnlazada()
print(f"¿Vacio? : {l.lista_vacia()}")
print(f"Largo : {l.largo()}")

print("INSERTO ELEMENTOS")
l.insertar_al_final({"Pan":125})
l.insertar_al_final({"Facturas":400})
l.insertar_al_final(5)
l.insertar_al_final({"Sanguchitos":150})

print(f"¿Vacio? : {l.lista_vacia()}")
print(f"Largo : {l.largo()}")
print(l.retornar_lista())

print("ELIMINO ELEMENTO: 5")
l.eliminar_por_dato(5)
#l.pop(2)

print(f"Largo : {l.largo()}")
print(l.retornar_lista())

print("INSERTO ELEMENTO: 6")
l.insertar(2,6)
print(l.retornar_lista())


print("BUSCO ELEMENTO POSICION DE ELEMENTO : 6")
print(f"La posicion es {l.index(6)}")
l.pop(2)

for x in l:
    print(x)

print("PROBANDO COLACLIENTES")
c=ColaClientes()
c.encolar("Walter")
c.encolar("Karim")
c.encolar("Ivan")
print(c)

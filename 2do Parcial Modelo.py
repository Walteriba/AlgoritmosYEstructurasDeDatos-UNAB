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
        
    def lista_vacia(self):
        """Devuelve un booleano segun el estado de la lista"""
        return self.prim is None
    
    def largo(self):
        """Devuelve el largo de la lista"""
        return self.len
    
    def retornar_lista(self):
        """Devuelve la lista enlazada en forma de lista"""
        aux=self.prim
        laux=[]
        while (aux is not None):
            laux.append(aux.dato)
            aux=aux.prox
        return laux
    
    def insertar(self, i, x):
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
    
    def insertar_al_final(self,dato):
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
    
    def eliminar_por_dato(self,x):
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
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato    


#-------- Cola de la Panadería ------------# 
class ColaClientes:
    def __init__(self) -> None:
        pass
 
    
#-------- Iterador ------------# 
def Iter():
    pass 


#-------- Panaderia ------------# 
class Panaderia:
    def __init__(self):
        pass
          


#----------- Probando el código ----------- #
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

#print("Aca imprimo la lista")
print(l.retornar_lista())

print("ELIMINO ELEMENTO: 5")
#l.eliminar_por_dato(5)
#l.pop(2)
print(f"Largo : {l.largo()}")

#print("Aca imprimo la lista")
print(l.retornar_lista())

print("INSERTO ELEMENTO: 6")
l.insertar(2,6)
print(l.retornar_lista())

"""
1)Modelar una panaderia (Clase y objetos)
2)Agregar a la panaderia una lista de productos (Listas enlazadas)
3)Agregar a la panaderia una cola de clientes (Colas y pilas)
4)Generar un iterador para la lista de productos y la cola de clientes (Iteradores)
5)Guardar la lista de productos en un archivo (Archivos)
6)Mover un directorio(Archivos (Ej. 8, Pract. 11))
Extra: importar uno o varios módulos
"""

class Panaderia:
    def __init__(self):
        pass
    

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
    
    def insertar_al_final(self,dato):
        """Inserta el dato al final de la lista"""    
        nodo=self._Nodo()
        nodo.dato=dato
        if self.prim is None:
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
        pass


class ColaClientes:
    def __init__(self) -> None:
        pass
    

def Iter():
    pass        

l=ListaProductosEnlazada()
print(f"¿Vacio? : {l.lista_vacia()}")
print(f"Largo : {l.largo()}")

print("INSERTO ELEMENTOS")
l.insertar_al_final({"Pan":125})
l.insertar_al_final({"Facturas":400})
l.insertar_al_final({"Sanguchitos":150})

print(f"¿Vacio? : {l.lista_vacia()}")
print(f"Largo : {l.largo()}")

print("Aca imprimo la lista")
print(l.retornar_lista())
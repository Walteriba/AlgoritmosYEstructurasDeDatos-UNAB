# -*- coding: utf-8 -*-

from time import time

def selectionSort(lista):
    global comparaciones
    n = len(lista)

    for i in xrange(n - 1):
        menor = i
        comparaciones += 1

        for j in xrange(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]


lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparaciones = 0

t0 = time()
selectionSort(lista)
t1 = time()

print "Lista ordenada:"
print lista, "\n"

print "Tiempo: {0:f} segundos".format(t1 - t0)
print "Comparaciones:", comparaciones

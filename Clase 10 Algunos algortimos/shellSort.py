# -*- coding: utf-8 -*-

from time import time

def shellSort(lista):
    global comparaciones
    n = len(lista)
    gap = n / 2

    while gap > 0:
        for i in xrange(gap, n):
            val = lista[i]
            j = i
            comparaciones += 1

            while j >= gap and lista[j-gap] > val:
                lista[j] = lista[j-gap]
                j -= gap

            lista[j] = val

        gap /= 2


lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparaciones = 0

t0 = time()
shellSort(lista)
t1 = time()

print "Lista ordenada:"
print lista, "\n"

print "Tiempo: {0:f} segundos".format(t1 - t0)
print "Comparaciones:", comparaciones
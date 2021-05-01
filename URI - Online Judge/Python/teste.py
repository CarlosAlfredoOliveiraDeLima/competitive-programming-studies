import sys

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(lista))
print(sys.getsizeof(lista))
print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))

print()

lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(type(lista))
print(sys.getsizeof(lista))
print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))

print()

lista = (v for v in range(10))

print(type(lista))
print(sys.getsizeof(lista))
print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))

print()

gerador = (letra for letra in 'Carlos Lima')
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

for letra in gerador:
    print(letra)

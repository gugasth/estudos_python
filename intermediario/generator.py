# anotações
# iterator é uma classe com __iter__ e __next__
# generator é uma função que pausa, ela usa iterator pra entregar 1 valor por vez

import sys # biblioteca que tem o sys.getsizeof(blabla)

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)
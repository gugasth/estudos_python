# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

#lista = []
#for numero in range(10):
#    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

# ou 
lista2 = [numero * 2 for numero in range(10)]
print(lista2)

# ou
lista3 = [numero * 2 for numero in range(10) if numero*2 > 10]
print(lista3)
# Empacotamento e desempacotamento de argumentos não nomeados


x, y, *resto = 1, 2, 3, 4
print(f'O x é: {x}, o y é: {y}, o resto é {resto}')


def soma (*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(f'A soma é: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')


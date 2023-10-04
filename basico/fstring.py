x = 'Uma variável qualquer'
y = f'Essa é uma string com uma variável: {x}'
print(y)


print(f'{x: >50}') # Alinhando a direita
print(f'{x: <50}') # Alinhando a esquerda
print(f'{x: ^50}') # Centralizando
print(f'{x:*^50}') # Centralizando e preenchendo com asteriscos

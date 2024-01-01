# crie uma função que multiplica todos os argumentos não nomeados recebidos
# retorne o total para uma variável e mostre o valor da variável

def multiplica(*args):
    total = 1
    for arg in args:
        total = arg * total 
    return total

resultado = multiplica(1, 2, 3, 4)
print(resultado)

# crie uma função que fala se um número é par um ímpar
# retorne se o númeor é par ou impar

def par_ou_impar(x):
    if (x % 2 == 0):
        print(f'O número {x} é par')
    else:
        print(f'O número {x} é ímpar')
        
par_ou_impar(3)
par_ou_impar(4)
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')
if (numero.isdigit()):
    numero = int(numero)
    if (numero % 2 == 0):
        print('O número é par')
    else:    
        print('O número é impar')
else:
    print('O número digitado não é inteiro')
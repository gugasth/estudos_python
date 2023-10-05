"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = ""
while (nome == ""): # enquanto não digitar fica esperando
    nome = input ('Digite o seu nome ')
    if (len(nome) > 0): # se o nome não for vazio
        if (len(nome) <= 4): # se for menor que 4
            print('Seu nome é curto') # é curto
        elif(len(nome) <= 6): # se for menor que 6
            print('Seu nome é normal') # é normal
        else: # senão
            print('O seu nome é muito grande') # é muito grande

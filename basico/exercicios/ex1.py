nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

if nome and idade:
    print('Seu nome é', nome)
    print('Seu nome invertido é', nome[::-1])
    espaco = (' ' in nome)
    if (espaco):
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')
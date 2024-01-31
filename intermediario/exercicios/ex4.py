# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def operacao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = operacao(soma, 5)
multiplica_por_dez = operacao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_dez(2))


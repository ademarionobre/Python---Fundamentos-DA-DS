# FUNÇÃO

# Um sequência de comandos que executa alguma tarefa e que tem um nome. A sua principal finalidade é nos ajudar a organizar
# programas em pedaços que correspondam a como imaginamos uma solução do problema.

# Exemplos
# print() imprime uma mensage no console
# input retornar um dado informado pelo usuario
# len recebe uma lista e retorna o tamanho dessa lista
# max retorna o maior valor de uma lista

# CRIAÇÃO DE FUNÇÃO
# Função inicial
# usando palavra reservada def (define)
def saudacao():
    print('Seja bem vindo(a)!')
    print('Aproveite!')

# chamando a funcao
saudacao()

# Função com parâmetros
def bemvindo(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Aproveite o conteúdo do curso de {curso}!')

bemvindo('Ademário', 'Python')

# Função com parâmetros default
def selecao(nome, cargo='Analista'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Prazer tê-lo(a) conosco como {cargo}')
selecao('Ademario')

# Funções com retorno
# def soma(num1, num2):
    #print('Soma = ', num1 + num2)

def soma(num1, num2):
    return num1 + num2 # a funcao para de executar após o return
resultado = soma(5, 6)

print('O resultado da soma é ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
resultado = calculadora(10, 20, '-')

print(resultado)
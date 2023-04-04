# Estrutura de repetição para techo de código
""""for variavel in range(10):
    print(variavel)""""

# executa uma repeticao de 0 a 9 e imprime.

# for com dois parametros
""""for var in range(1, 10):
    print(var)""""

"""# for com tres parametros. Inicio, Fim e pular 3 em 3.
for v in range(1, 12, 3):
    print(v)""""

# Exemplo de aplicaçãom médias de notas. Usanod variável acumuladora
soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a nota {i}: '))

    soma = soma + nota

print('A média é: ', soma/3)
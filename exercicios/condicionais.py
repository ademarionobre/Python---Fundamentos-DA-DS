# ESTRUTURAS CONDICIONAIS

# Exemplo 1
idade = 20

if idade >=18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

# Exmpelo 2
media = float(input('Informe a média do estudante: '))

if media >=7:
    print('Você foi aprovado!')
elif media >=5:
    print('Recuperação')
else:
    print('Você não foi aprovado.')

#Exemplo 3
media1 = 6
presenca = 100

if media1 >= 7 and presenca >= 70:
    print('Aprovado')
    print('Parabéns')
else:
    print('Reprovado')
    print('tente novamente')
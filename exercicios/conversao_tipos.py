# CONVERSÃO DE TIPOS
    #int()
    #str()
    #float()
    #bool()

idade = '40'
numero1 = '26'
numero2 = '30'

print(numero1 + numero2)

# convertendo
print(idade, type(idade))
idade_int = int(idade) # convertendo
print(idade_int, type(idade_int))

# padrão o input é string
altura = input('Informe sua altura: ')
print(altura, type(altura))
# conversão direta
altura = float(input('Informe sua altura: '))
print(altura, type(altura))

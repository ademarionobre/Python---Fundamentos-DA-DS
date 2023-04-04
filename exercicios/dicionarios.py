# DICIONÁRIOS
# Similar a listas. Estrutura define uma chave a um elemento.

# Criando dicionários. Utiliza {}
# dicionario = {}
# dicionario = dict()

dicionario = {'nome': 'Ademario', 'idade': 40, 'altura': 1.71}
print(dicionario)

print(dicionario['idade'])

# Adicionar elementos
dicionario['analista'] = True
print(dicionario)

dicionario['nome'] = 'Ademário' # substitui o valor no elemento
print(dicionario)

# Iterando sobre um dicionário
for var in dicionario:
    print(var) # pecorre e imprime as chaves

for chave in dicionario:
    print(chave, dicionario[chave]) # pecorre e imprime as chaves e valores

# Testando a existência de uma chave
print('peso' in dicionario)
print('altura' in dicionario)

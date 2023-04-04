# LISTAS: forma de esturutas que armazena várias variáveis
# uso de colchetes []

# Sem usar lista
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Usando lista
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = [] # lista vazia
lista = list() # lista vazia (função)
lista = [26, 'Ademário', 3.14, True] # diversos tipos de dados
lista_de_listas = [10, [1, 2, 3]] # lista dentro de outra lista

# Indexação e slices (fatiamento)
# Indexação - Acessando um elemento por meio de um indice
lista = [40, 'Ademário', 1.71, True] # 4 elementos inciando do indice 0 a 3
print(lista[0]) # primeiro elemento da lista
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) # ultimo elemento

# Slices (pedaços da lista)
lista1 = [10, 20, 30, 40 , 50, 60, 90]
print(lista1[0:3])
print(lista1[3:6])
print(lista1[3:])
print(lista1[2:6:2])# ultimo parametro pula de dois em dois

# Interações com FOR
#1. Utilizando os próprios elementos da lista
for elemento in lista1:
    print(elemento)

#2. Utilizando os índices
print('Comprimento da lista ', len(lista1))

for i in range(len(lista1)):
    print(i) #imprime os indices

for i in range(len(lista1)):
    print(lista1[i]) #imprime os elementos da lista em cada posição

# METODOS E FUNCOES DE LISTAS
# Métodos de listas

lista2 = [1, 3, 12, 8, 2]

# append - adicionando elementos no final
print('Antes do método append: ', lista2)

lista2.append(5)
print('Depois do append: ', lista2)

# insert - adiciona elemento na posição desejada

lista2.insert(2, 10) # adicionando elemento 10 no indice 2
print('Depois do insert: ', lista2)
lista2.insert(6, 10)

# extend - juntar duas listas

lista3 = [11, 15, 17]
lista2.extend(lista3)
print('Depois do extend: ', lista2)

# pop - remove elementos
# por padrão elimina o ultimo elemento
lista2.pop()
print('Lista após o pop: ',lista2)

lista2.pop(0)
print('Lista após o pop: ', lista2)

# remove - informa qual o elemento a ser removido. Remove o primeiro elemento encontrado.
lista2.remove(5)
print('Depois do remove: ', lista2)

# count
print('Quantidade de número 10 na lista: ', lista2.count(10))

# index - informa o indice de determinado elemento
print('Qual o índice do elemento 12?: ', lista2.index(12))

# sort - ordenar uma lista
lista2.sort() # ordena de forma crescente
print(lista2)
lista2.sort(reverse=True) # descrecente
print(lista2)

# FUNÇÕES PARA LISTAS
# len- saber quantos elementos na lista
print(len(lista2))

# sum
print(sum(lista2))

# max
print('Maior elemento da lista: ', max(lista2))

# min
print('Menor elemento da lista: ', min(lista2))



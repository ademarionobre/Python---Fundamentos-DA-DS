#Algumas funções podem nos ajudar a trabalhar com listas. Observe o código abaixo e o respectivo output desejado:

animais = ['gato', 'coelho', 'macaco', 'girafa']

#animais.função1('gato')
#print(animais)
#print(função2(animais))
#print(animais.função3('coelho'))

#Output desejado:

#['coelho', 'macaco', 'girafa']
#3
#0

"""Respectivamente, por quais funções devemos substituir função1, função2 e função3 no código acima, para obter o 
output desejado?"""

# saida
animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))
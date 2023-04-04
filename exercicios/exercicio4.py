"""
Além do laço de repetição while, muitas vezes utilizamos o operador for em Python para implementarmos laços de repetição.
Embora isso seja possível, o for é mais do que meramente um laço de repetição: este operador é utilizado para percorrer 
alguma estrutura iterável."""

#for _ in range(10):
#   print("Olá, mundo!")

"""Quando queremos utilizar o for explicitamente como um laço de repetição, é muito comum utilizarmos a estrutura acima,
com o auxílio do iterador range(). No entanto, o mesmo comportamento é possível se nos aproveitarmos do fato de que o for
percorre qualquer iterável. Sabendo disso, das alternativas a seguir, qual é a única que NÃO reproduz o mesmo resultado que
 o trecho acima?"""

#for _ in "lests code":
#    print("Olá mundo!")

#for _ in " "*10:
#    print("Olá, mundo!")

#for _ in range(10, 20, 1):
#    print("Olá mundo!")

for _ in [10]:
    print("Olá, mundo!")

#for _ in [10]*10:
#    print("Olá, mundo!")
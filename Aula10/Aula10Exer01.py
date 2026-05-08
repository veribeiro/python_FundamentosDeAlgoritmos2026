# Crie 3 listas:
# ▶ Inteiros: a primeira lista com 10 números inteiros gerados aleatoriamente
# ▶ Reais: a segunda lista com 5 números reais gerados aleatoriamente
# ▶ Strings: A terceira lista com 7 strings criadas por você.
# Então adicione as 3 listas a uma lista única, chamada completa.
# Apague todas as 3 listas originais.
# Acesse e mostre todos os elementos da lista completa.

from random import randint, random

inteiros=[]
reais=[]
strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for i in range(0,10):
    inte = randint(1, 10)
    inteiros.append(inte)

for l in range(0, 5):
    real = random()*5
    reais.append(real)

completa = [inteiros, reais, strings]

# inteiros.clear() -> Para remover a lista

print(f'Inteiros: {inteiros}')
print(f'Reais: {reais}')
print(f'Strings: {strings}')
print(f'Completa: {completa}')
# Faça um programa que cria uma matriz M 10 X 15, sendo que cada
# elemento é um inteiro gerado aleatoriamente.
# Então, exiba a matriz completa e, na sequência, somente os
# elementos da primeira coluna da matriz.

from random import randint
matriz = []

for i in range(10):
    linha = []
    for i in range(15):
        numero = randint(0, 9)
        linha.append(numero)
    matriz.append(linha)

print("Matriz completa:")
for l in range(10):
    for r in range(15):
        print(matriz[l][r], end=" ")
    print()

print("\nPrimeira coluna da Matriz:")
for p in range(0, 10):
    print(matriz[p][0])

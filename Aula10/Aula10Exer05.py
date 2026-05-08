# Faça um programa que cria um matriz A 10 X 5 com números
# inteiros aleatórios e, então, exiba a matriz transposta de
# A(At)

from random import randint

matriz = []

for i in range(10):
    linha = []
    for j in range(5):
        numero = randint(0, 9)
        linha.append(numero)
    matriz.append(linha)

print("Matriz original:")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna], end=" ")
    print()

At = []
for i in range(5):
    novaLinha = []
    for j in range(10):
        novaLinha.append(0)
    At.append(novaLinha) 

for i in range(10):
    for j in range(5):
        At[j][i]=matriz[i][j]

print("\nMatriz transposta")
for linha in range(len(At)):
    for coluna in range(len(At[linha])):
        print(At[linha][coluna], end=" ")
    print()
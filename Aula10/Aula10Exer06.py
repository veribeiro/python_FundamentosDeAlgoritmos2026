# Cria uma matriz m[12][12] com números inteiros aleatórios.
# Em seguida, calcule e mostre a soma ou a média considerando
# somente aqueles elementos que estão abaixo da diagonal
# principal da matriz, conforme ilustrado abaixo (área verde).
# A entrada do programa deve ser um único caractere maiúsculo
# ’S’ ou ’M’, indicando a operação (Soma ou Média) que deverá
# ser realizada com os elementos da matriz.

import random

# 1. Criar a matriz 12x12
N = 12
matriz = [[random.randint(0, 10) for _ in range(N)] for _ in range(N)]

# 2. Ler a operação
operacao = input("Digite S para Soma ou M para Média: ").upper()

# 3. Exibir a matriz com %3d
print("Matriz criada:")
for linha in matriz:
    for elemento in linha:
        print("%3d" % elemento, end=" ")
    print()

# 4. Calcular a Soma e contar os elementos (área verde)
soma = 0
contador = 0

for i in range(N):
    for j in range(N):
        # Condição para estar ACIMA da diagonal secundária
        if i + j > N - 1:
            soma += matriz[i][j]
            contador += 1

# 5. Mostrar o resultado conforme a operação
if operacao == 'S':
    print(f"\nSoma: {soma}")
elif operacao == 'M':
    # O exercício pede apenas números inteiros (// faz divisão inteira)
    media = soma // contador
    print(f"\nMédia: {media}")
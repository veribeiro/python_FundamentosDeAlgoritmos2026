# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo. Reserve 4 casas para imprimir cada dado da matriz.

n = int(input("Digite a ordem da matriz: "))

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        # Aplicando a lógica da potência: 2 elevado a (i + j)
        valor = 2 ** (i + j)
        linha.append(valor)
    matriz.append(linha)

# 3. Imprimir com a reserva de 4 casas (%4d)
for i in range(n):
    for j in range(n):
        # Usamos %4d para alinhar em 4 espaços
        # O if serve para não colocar espaço extra no final da linha (opcional)
        if j == n - 1:
            print("%4d" % matriz[i][j], end="")
        else:
            print("%4d" % matriz[i][j], end=" ")
    print()
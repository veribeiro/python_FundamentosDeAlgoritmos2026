# Faça um programa para receber uma matriz 3 X 3 (solicitar ao usuário)
# Apresentar a soma dos elementos da diagonal principal
lista1 = []
lista2 = []
lista3 = []

for i in range(0, 3):
    linha1 = int(input("Digite um número: "))
    lista1.append(linha1)

for l in range(0, 3):
    linha2 = int(input("Digite um número: "))
    lista2.append(linha2)

for t in range(0, 3):
    linha3 = int(input("Digite um número: "))
    lista3.append(linha3)

matriz = [lista1, lista2, lista3]

print("\nMatriz:")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna], end=" ")
    print()

oneDiagonal=matriz[0][0]
twoDiagonal=matriz[1][1]
treeDiagonal=matriz[2][2]

soma = oneDiagonal+twoDiagonal+treeDiagonal
print("Soma da diagonal: ", soma)
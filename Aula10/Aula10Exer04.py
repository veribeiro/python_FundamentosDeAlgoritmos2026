# Solicitar dados de uma matriz 4 X 4
# Montar uma lista de 4 elementos com a soma dos elementos
# ímpares de cada linha da matriz

lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(0, 4):
    linha1=int(input("Digite um número: "))
    lista1.append(linha1)

for l in range(0, 4):
    linha2=int(input("Digite um número: "))
    lista2.append(linha2)

for m in range(0, 4):
    linha3=int(input("Digite um número: "))
    lista3.append(linha3)

for n in range(0, 4):
    linha4=int(input("Digite um número: "))
    lista4.append(linha4)

matriz = [lista1, lista2, lista3, lista4]

print("\nMatriz:")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna], end=" ")
    print()

oneLinha = matriz[0]

resultadoSoma = []

for linha in range(len(matriz)):
    impares1 = []

    for y in matriz[linha]:
        if not y %2==0:
            impares1.append(y)

    soma = sum(impares1)
    resultadoSoma.append(soma)

print("Lista: ", resultadoSoma)
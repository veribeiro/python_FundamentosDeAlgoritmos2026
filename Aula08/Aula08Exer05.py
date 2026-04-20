# ▶ Imprime uma sequência de n números em ordem inversa à da leitura
# ▶ Utilize uma lista para isso.

lista = []

qtdeNum = int(input("Digite a qtde de números: "))
for i in range(qtdeNum):
    lista.append(int(input("Digite um número: ")))

print("Números: ", lista)

inverso = []

for i in range(len(lista)-1, -1, -1):
    inverso.append(lista[i])

print(inverso)
# ▶ Peça 10 números reais do usuário.
# ▶ Armazene-os em uma lista e diga qual o índice do maior e seu valor

lista = []
for i in range(0, 10):
    lista.append(int(input("Digite um número: ")))

x=len(lista)
print("Números: ", lista)

maior = lista[0]
for num in lista:
    if num>maior:
        maior = num

print("Maior número: ", maior)

for indice in range(len(lista)):
    if lista[indice] ==maior:
        print("Indice maior número: %d" %indice)
        break
else:
    print("Elemento não encontrado")

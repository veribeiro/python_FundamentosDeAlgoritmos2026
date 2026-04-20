# Faça um programa para criar uma lista de 10 elementos do usuário e aprsente:
# ▶ a soma dos elementos pares
# ▶ a soma dos elementos de índice par

lista = []
for i in range(0, 10):
    lista.append(int(input("Digite um número: ")))

print("Números: ", lista)

somarPares=0
somarImpares=0

for elementos in lista:
    if elementos%2==0:
        somarPares +=elementos

    elif not elementos%2==0:
        somarImpares += elementos

print("Soma elementos pares: ", somarPares)
print("Soma elementos ímpares: ", somarImpares)
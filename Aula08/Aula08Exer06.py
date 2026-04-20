# Faça um programa para criar uma lista de 10 elementos inteiros
# ▶ Mostre todos os elementos que forem maiores que a soma de dois de seus antecessores

lista =[]
for i in range(0, 10):
    lista.append(int(input("Digite um número: ")))

print("Números: ", lista)

for i in range(2, len(lista)):
    elemento = lista[i]
    antecessor_1 = lista[i-1]
    antecessor_2 = lista[i-2]

    if elemento>(antecessor_1+antecessor_2):
        print(elemento)
    

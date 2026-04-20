# As temperaturas de uma cidade foram armazenadas na lista
# temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4].
# Faça um programa que imprime a menor e a maior temperatura
# E imprima também a média das temperaturas

temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
soma=0
menor = temperaturas[0]


for i in temperaturas:
    if i<menor:
        menor=i


maior = temperaturas[0]
for num in temperaturas:
    if num>maior:
        maior=num

for m in temperaturas:
    soma +=m

print("Maior: ",maior)
print("Menor: ",menor)
print("Média: ",soma/len(temperaturas))
# Faça um programa que gere 100 números aleatórios
# Gere números no intervalo de 0 à 20
# Mostre quantas vezes cada número apareceu
# Dica:
# Utilize um dicionário para armazenar o número como chave
# e a quantidade de vezes em que ele aparece como valor

import random

# 1. Criar o dicionário vazio para armazenar as contagens
contagem = {}

# 2. Gerar 100 números aleatórios
for _ in range(100):
    numero = random.randint(0, 20)
    
    # Lógica do contador:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

# 3. Exibir os resultados formatados
print("Numero: Quantidade")
# Ordenamos as chaves para a exibição ficar organizada
for num in sorted(contagem.keys()):
    print(f"{num:2} : {contagem[num]}")
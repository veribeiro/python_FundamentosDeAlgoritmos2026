# Neste exercício, você simulará 1000 lançamentos de dois dados.
# Comece escrevendo uma função que simula o lançamento de um par de dados de seis lados cada.
# Sua função não deve aceitar nenhum parâmetro.
# Ela retornará a somatória obtida pelos dois dados.
# Escreva um programa principal que use sua função para simular 1000 lançamentos de dois dados.
# Como acontece em alguns programas, você deve contar o número
# de vezes que cada somatória acontece.
# Em seguida, a função principal deve exibir uma tabela que resume esses resultados.
# Mostre a frequência para cada resultado como uma porcentagem
# do número total de lançamentos.

import random

# 1. Função que simula o lançamento
def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

# 2. Programa Principal
lancamentos = {}

# Simula 1000 vezes
for _ in range(1000):
    soma = lancar_dados()
    
    # Se a soma já estiver no dicionário, aumenta 1. 
    # Se não, começa com 1.
    if soma in lancamentos:
        lancamentos[soma] += 1
    else:
        lancamentos[soma] = 1

# 3. Exibição dos resultados
print("Lançamentos:")
print(lancamentos)

print("\nEm 1000 lançamentos tivemos as seguintes porcentagens:")

# Para mostrar ordenado pela soma (de 2 a 12), usamos o sorted
for soma in sorted(lancamentos.keys()):
    quantidade = lancamentos[soma]
    porcentagem = (quantidade / 1000) * 100
    print(f"{soma:2} : {porcentagem:.1f}%")
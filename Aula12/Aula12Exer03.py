# Crie um arquivo: “numeros.txt” que contenha 100 números aleatórios;
# Escreva uma função que leia uma sequência numérica do arquivo
# “numeros.txt” e salva os números na lista num.
# Escreva outra função que recebe a lista num como parâmetro e
# retorna uma nova lista num_unicos, sem os elementos repetidos.
# Escreva uma terceira função que recebe a lista num_unicos e
# grava os números no arquivo “numeros_unicos.txt”.

import random

# 1. Função para criar o arquivo inicial com 100 números
def criar_arquivo_inicial():
    with open("numeros.txt", "w") as arquivo:
        for _ in range(100):
            # Gera entre 0 e 50 para garantir que existam repetidos para testar
            arquivo.write(f"{random.randint(0, 50)}\n")

# 2. Função para ler o arquivo e salvar na lista 'num'
def ler_sequencia():
    num = []
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            # strip remove o \n e int converte para número
            num.append(int(linha.strip()))
    return num

# 3. Função para remover repetidos
def remover_repetidos(lista_num):
    num_unicos = []
    for n in lista_num:
        if n not in num_unicos:
            num_unicos.append(n)
    return num_unicos

# 4. Função para gravar a lista final em um novo arquivo
def gravar_unicos(lista_unicos):
    with open("numeros_unicos.txt", "w") as arquivo:
        for n in lista_unicos:
            arquivo.write(f"{n}\n")

# --- Programa Principal ---
criar_arquivo_inicial()
lista_completa = ler_sequencia()
lista_sem_repetidos = remover_repetidos(lista_completa)
gravar_unicos(lista_sem_repetidos)

print(f"Total de números gerados: {len(lista_completa)}")
print(f"Total de números únicos: {len(lista_sem_repetidos)}")
print("Arquivos 'numeros.txt' e 'numeros_unicos.txt' gerados com sucesso!")
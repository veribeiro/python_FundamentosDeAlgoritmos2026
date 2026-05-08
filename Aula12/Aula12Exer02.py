# Crie um arquivo: “numeros.txt” que contenha 100 números aleatórios;
# Todos os números do arquivo estão na mesma e única linha,
# separados por espaço;
# Escreva uma função em Python para retornar a somatória de
# todos os números que estão armazenados no arquivo “numeros.txt”.

import random

# 1. Criando o arquivo conforme as regras (100 números na mesma linha)
def preparar_arquivo():
    with open("numeros.txt", "w") as arquivo:
        # Geramos 100 números e transformamos em texto
        numeros = [str(random.randint(0, 100)) for _ in range(100)]
        # Unimos todos com um espaço entre eles
        linha_unica = " ".join(numeros)
        arquivo.write(linha_unica)

# 2. Função para calcular a somatória
def somar_numeros_arquivo():
    with open("numeros.txt", "r") as arquivo:
        # Lê o conteúdo inteiro do arquivo
        conteudo = arquivo.read()
        
        # O .split() separa o texto pelos espaços e cria uma lista
        lista_de_strings = conteudo.split()
        
        # Convertemos cada item para inteiro e somamos tudo
        soma_total = sum(int(n) for n in lista_de_strings)
        
        return soma_total

# --- Execução ---
preparar_arquivo() # Apenas para garantir que o arquivo existe
resultado = somar_numeros_arquivo()
print(f"A soma de todos os números no arquivo é: {resultado}")
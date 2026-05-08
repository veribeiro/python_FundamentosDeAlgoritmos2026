# Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
# A primeira linha deve conter o maior número e a última linha o menor.
# Salve o resultado em outro arquivo (invertido.txt).

# 1. Abrir o arquivo original para leitura
with open("pares.txt", "r") as arquivo_origem:
    # Lemos as linhas, limpamos os espaços e convertemos para inteiro
    # Usamos uma lista para armazenar todos os números
    numeros = []
    for linha in arquivo_origem:
        if linha.strip(): # Verifica se a linha não está vazia
            numeros.append(int(linha.strip()))

# 2. Ordenar os números de forma decrescente
# O sorted(..., reverse=True) coloca o maior valor no índice [0]
lista_ordenada = sorted(numeros, reverse=True)

# 3. Criar e gravar o resultado no arquivo invertido.txt
with open("invertido.txt", "w") as arquivo_destino:
    for n in lista_ordenada:
        # Gravamos o número transformado em string com um pula-linha (\n)
        arquivo_destino.write(str(n) + "\n")

print("Arquivo 'invertido.txt' gerado com sucesso!")
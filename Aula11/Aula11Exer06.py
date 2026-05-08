# Um cartão de bingo consiste de 5 colunas de 5 números. As
# colunas são rotuladas com as letras B, I, N, G e O. Existem 15
# números que podem aparecer na coluna de cada letra. Em
# particular, os números que podem aparecer na coluna de B estão
# no intervalo de 1 a 15, os números que podem aparecer sob o I
# variam de 16 a 30 e assim por diante. Escreva uma função que
# cria um cartão de Bingo com números aleatórios e armazena tudo
# em um dicionário. As chaves serão as letras B, I, N, G e O.
# Os valores serão as listas de cinco números que aparecem em cada letra.

import random

def gerar_cartao_bingo():
    # 1. Definimos os intervalos de cada letra
    # B: 1-15, I: 16-30, N: 31-45, G: 46-60, O: 61-75
    letras = ['B', 'I', 'N', 'G', 'O']
    cartao = {}
    
    inicio = 1
    fim = 15
    
    for letra in letras:
        # Criamos uma lista de 5 números aleatórios para a letra atual
        # random.sample garante que os números não se repitam na mesma coluna
        numeros = random.sample(range(inicio, fim + 1), 5)
        
        # Guardamos no dicionário
        cartao[letra] = numeros
        
        # Atualizamos os limites para a próxima letra
        inicio += 15
        fim += 15
        
    return cartao

# Programa Principal
meu_cartao = gerar_cartao_bingo()

# Exibição formatada conforme a saída esperada
for letra, numeros in meu_cartao.items():
    print(f"{letra} : {numeros}")
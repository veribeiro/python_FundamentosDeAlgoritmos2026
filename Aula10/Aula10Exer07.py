# Faça um programa que preencha uma matriz 10 X 3 com as notas
# de 10 alunos com 3 provas (valores gerados de forma aleatória entre 0 e 10).
# O programa deverá mostrar:
# ▶ A matriz com todas as notas de cada aluno.
# ▶ Um relatório com o número do aluno (número da linha), a prova em
# que cada aluno obteve a menor nota (número da coluna) e o valor da menor nota.
# ▶ O relatório deverá mostrar também qual foi a menor nota obtida
# em cada prova e a quantidade de alunos que obtiveram essa menor
# nota na respectiva prova.

import random

# 1. Criar e preencher a matriz 10x3
matriz = [[random.randint(0, 10) for _ in range(3)] for _ in range(10)]

print("Matriz de Notas:")
for linha in matriz:
    for nota in linha:
        print(f"{nota:2}", end=" ")
    print()

print("\nRelatório do Aluno:")
# 2. Relatório individual por aluno
for i in range(10):
    menor_nota = min(matriz[i])
    # .index() encontra a primeira posição (coluna) da menor nota
    indice_prova = matriz[i].index(menor_nota)
    print(f"Aluno {i} : menor nota: {menor_nota:2} , idx: {indice_prova}")

print("\nRelatório Geral por Prova:")
for j in range(3): # Percorre as colunas (provas)
    # Criamos uma lista só com as notas da prova atual (coluna j)
    notas_prova = [matriz[i][j] for i in range(10)]
    
    menor_nota_prova = min(notas_prova)
    quantidade = notas_prova.count(menor_nota_prova)
    
    print(f"Menor nota na prova {j} - {menor_nota_prova} | alunos com essa nota: {quantidade}")
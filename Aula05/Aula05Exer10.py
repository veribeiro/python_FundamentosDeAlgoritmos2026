#  Elaborar um programa que leia um conjunto de valores reais,
# correspondentes a 80 notas dos alunos de uma turma, notas
# estas que variam de 0 a 10. Calcule e mostre:
# a) A quantidade de alunos aprovados (nota >= 6, 0)
# b) A média das notas da turma;
import random
aprovados=0
soma_nota=0
total_alunos=80

for i in range(total_alunos):
    nota =random.uniform(0,10)
    soma_nota+=nota
    if nota>=6:
        aprovados+=1
media=soma_nota/total_alunos

print("Quantidade de alunos aprovados: ",aprovados)
print("Quantidade de média de alunos: %.2f"%media)

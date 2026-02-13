#Exercício 4 :Faça um programa que pergunte quanto a pessoa ganha por hora e o número de horas trabalhas no mês. 
# Calcule e mostre o total do salário no referido mês, sabendo-se que são descontados 11%
# para o imposto de renda, 8% para o INSS e 5% para o sindicato.

valorHora = int(input("Digite o valor da hora de trabalho: "))
numHora = int(input("Digite o número de horas trabalhadas por mês: "))

salarioBruto = valorHora*numHora
IR = 0.11*salarioBruto
INSS = 0.08*salarioBruto
Sindicato = 0.05*salarioBruto
salarioLiquido = salarioBruto-(IR+INSS+Sindicato)
print("+ Salário Bruto: R$ %.2f" % salarioBruto, "\n - IR(11%): R$ ", IR,
      "\n - INSS(8%): R$ ", INSS, "\n - Sindicato: R$ %.2f"% Sindicato,
      "\n + Salário líquido: R$ %.2f" %salarioLiquido)

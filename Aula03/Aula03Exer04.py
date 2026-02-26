# Escreva um programa que pergunte o salário de um funcionário
#Calcule o valor do aumento de salário sabendo que:
#▶ Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
#▶ Para salários inferiores ou iguais a R$ 1250,00, aumento de 15%.
#Imprima o novo salário.
#Observação: Resolva usando apenas Estruturas de Decisão Completas.

salario = float(input("Qual é o seu salário "))
if salario > 1250:
    aumento = (salario*0.10)+salario
    print("Seu salário é: %.2f "% aumento)

else:
    aumento = (salario*0.15)+salario
    print("Seu salário é: %.2f"%aumento)

    

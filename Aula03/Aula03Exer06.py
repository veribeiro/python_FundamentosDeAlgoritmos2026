#Escreva um programa que deve dizer se um carro é:
# ▶ novo (se tem menos de 3 anos)
# ▶ velho (mais ou igual a 3 anos)
#A idade do carro deve ser informada pelo usuário
#Observação: Resolva usando apenas Estruturas de Decisão Completas.

idadeCarro = int(input("Qual é a idade do carro? "))

if idadeCarro>=3:
    print("Velho (tem mais ou igual a 3 anos)")

else:
    print("Novo (tem menos de 3 anos)")
# Tendo como dados de entrada a altura e o sexo de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas:
# ▶ para homens: (72,7 * h) - 58;
# ▶ para mulheres: (62,1 * h) - 44,7.

altura=(float(input("Digite sua altura: ")))
sexo= input("Digite o seu sexo -> Digite m para masculino e digite f para feminino: ")

if sexo=="f":
    pesoIdeal=(72.7 * altura) - 58
    print("Peso ideal: %.2f"% pesoIdeal)

elif sexo=="m":
    pesoIdeal=(62.1 * altura) - 44.7
    print("Peso ideal: %.2f"% pesoIdeal)

else: 
    print("Ocorreu um erro")
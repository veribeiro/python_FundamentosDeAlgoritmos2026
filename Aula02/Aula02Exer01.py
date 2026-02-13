#Exercício 1 : Faça um programa que leia a altura de uma pessoa e calcule o peso ideal,
#suponha que o peso ideal seja dado pela fórmula: (72.7Xaltura)-58

altura = float(input("Digite a sua altura: "))
pesoIdeal = (72.7*altura)-58

print("Peso ideal %.2f" % pesoIdeal)
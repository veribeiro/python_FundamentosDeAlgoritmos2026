# Escreva um programa que imprima a tabuada de um número
# digitado pelo usuário;

numeroEscolhido= int(input("Digite um número para escolher na tabuada: "))
limite = int(input("Digite o número limite para calcular a tabuada: "))
limite = limite+1

for i in range(0, limite):
    calcular=numeroEscolhido*i
    print(numeroEscolhido, " X ", i, " = ", calcular)
    i=i+1
    
    if limite==i:
        break


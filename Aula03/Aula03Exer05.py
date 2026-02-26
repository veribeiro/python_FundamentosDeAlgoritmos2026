# Escreva um programa que pergunte o ano atual e o ano de nascimento do usuário. Calcule a idade dele.
# Se a idade for maior ou igual a 18 anos, mostre uma mensagem dizendo que ele pode tirar CNH.
# Observação: Resolva usando apenas Estruturas de Decisão Simples.

anoAtual= int(input("Qual é o ano atual? "))
anoNascimento= int(input("Qual é o seu ano de nascimento? "))

calcularIdade= anoAtual-anoNascimento

if calcularIdade>=18:
    print("Você pode tirar sua CNH")

if calcularIdade<18:
    print("Você não pode tirar sua CNH")
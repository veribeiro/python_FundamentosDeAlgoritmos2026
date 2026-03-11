# Faça um programa que leia 6 números inteiro positivos do
# usuário exiba o maior o número lido;
numeros=[] #-> É a primeira vez que utilizo lista

for x in range (0, 6):
    num=int(input(f"Escolha um número (tentativa {x+1}/6): "))
    numeros.append(num)

    print(f"Você digitou: {numeros}")
    numeroMaior=max(numeros)

print("O número maior é: ", numeroMaior)
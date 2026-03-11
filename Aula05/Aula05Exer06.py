# Escreva um programa que leia números digitados pelo usuário
# ▶ O programa deve ler os números até que o 0 (zero) seja digitado.
# ▶ Quando o 0 for digitado, o programa deve exibir:
# ⋆ a quantidade de números que foram digitados;
# ⋆ a somatória destes números;
# ⋆ e a média aritmética.
numeros=[]

while True:
    num = int(input("Digite um número"))

    if num==0:
        break

    numeros.append(num)
        
quantidade = len(numeros)
somar = sum(numeros)
media = somar/quantidade if quantidade > 0 else 0

print("Quantidade de números digitados: ", quantidade)
print("Somatória dos números: ", somar)
print("Média aritmética: ", media)





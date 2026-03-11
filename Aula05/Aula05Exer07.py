# Faça um programa para calcular a somatória de 10 números
# ▶ Os número devem ser digitados pelo usuário
# ▶ Será necessário um contador para controlar o número de repetições
# ▶ e um acumulador para acumular a soma dos números entre cada repetição
acumular=0
contador=0

for x in range (0,10):
    numero=int(input("Digite um número: "))
    acumular+=numero
    contador+=1
    print("[",contador,"/10","]")

print("Somatória dos números digitados são: ", acumular)


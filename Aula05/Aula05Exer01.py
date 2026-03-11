# Faça um programa que imprima os números ímpares entre 0 e um
# número digitado pelo usuário;

numero = int(input("Digite um número: "))
i=0
print(i)

while i<=numero:
    if not i%2==0:
        print(i)
    i=i+1  

    
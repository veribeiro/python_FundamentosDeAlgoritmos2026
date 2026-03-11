# Faça um programa que imprima os números de 1 a 50 de 1 em 1 e
# de 52 a 100 de 2 em 2;
for x in range(1, 50):
    print(x)

print("\n")

for x in range(52, 100):
    if x%2==0:
        print(x)
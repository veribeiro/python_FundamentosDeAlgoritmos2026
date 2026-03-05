#Escreva um algoritmo que leia três valores inteiros e
#diferentes e mostre-os em ordem decrescente.

num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
num3=int(input("Digite um outro número: "))

if (num1>num2) and (num1>num3) and (num2>num3):
    print(num1 , ",", num2, ",", num3)

elif(num1>num2) and (num1>num3) and (num3>num2):
    print(num1 , ",", num3, ",", num2)

elif(num2>num1) and (num2>num3) and (num3>num1):
    print(num2 , ",", num3, ",", num1)

elif(num2>num1) and (num2>num3) and (num1>num3):
    print(num2 , ",", num1, ",", num3)

elif(num3>num1) and (num3>num2) and (num2>num1):
    print(num3 , ",", num2, ",", num1)

elif(num3>num1) and (num3>num2) and (num1>num2):
    print(num3 , ",", num1, ",", num2)

else:
    print("São iguais")
# Escreva um algoritmo que leia o código de um determinado
# produto e mostre a sua classificação. Utilize a seguinte

codigo = int(input("Escreva o código do produto: "))

if codigo==1:
    print("Alimento não perecível")

elif codigo==2 or codigo==3 or codigo==4:
    print("Alimento perecível")

elif codigo==5 or codigo==6:
    print("Vestuário")

elif codigo==7:
    print("Higiene pessoal")

elif codigo>=8 and codigo<=15:
    print("Limpeza e utensílios domésticos")

else:
    print("Inválido")
# Faça um algoritmo que leia o ano de nascimento de uma pessoa,
# calcule e mostre sua idade e, também, verifique e mostre se
# ela já tem idade para votar (16 anos ou mais) e para conseguir
# a Carteira de Habilitação (18 anos ou mais).

anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = int(input("Digite seu ano atual: "))

idade = anoAtual-anoNascimento

if idade>=18:
    print("Você já tem idade para votar e conseguir a Carteira de Habilitação")

elif idade>=16:
    print("Você já tem idade para votar, porém não pode conseguir a Carteira de Habilitação")

else:
    print("Você não tem idade para votar e não pode conseguir a Carteira de Habilitação")

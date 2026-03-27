# Foi feita uma pesquisa entre os habitantes de uma região.
# Foram coletados os dados de idade, sexo (M/F) e salário. Faça
# um programa que informe:
# a) a média de idade do grupo;
# b) a média de salários dos homens;
# c) quantidade de mulheres com salário abaixo de R$600,00.
#Encerre a entrada de dados quando for digitada uma idade
# negativa (os dados da idade negativa não podem entrar nos
# cálculos dos itens solicitados acima).
soma_idade=0
cont_pessoas=0
soma_salario_homens=0
cont_homens=0

cont_mulheres_salario_baixo=0

while True:
    idade=int(input("Digite a idade: "))

    if idade <0:
        break
    sexo=input("Digite o sexo (M/F): ")
    salario=int(input("Digite o salário: "))
    soma_idade+=idade
    cont_pessoas+=1


    if sexo=='M':
        soma_salario_homens+=salario 
        cont_homens+=1

    if sexo=='F' and salario<600:
        cont_mulheres_salario_baixo+=1

if cont_pessoas>0:
    media_idade=soma_idade/cont_pessoas
    print("Média de idade do grupo: %.2f"%media_idade)

    if cont_homens>0:
        media_salario_homens = soma_salario_homens/cont_homens
        print("Média de salários dos homens: %.2f"%media_salario_homens)
    else:
        print("Nenhum homem registrado")
    
    print("Quantidade de mulheres com salário abaixo de R$600,00: %.2f"%cont_mulheres_salario_baixo)

else:
    print("Não houve nenhum registro")



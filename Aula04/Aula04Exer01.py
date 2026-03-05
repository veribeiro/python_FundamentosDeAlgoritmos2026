#Construa um algoritmo que, tendo como dados de entrada o preço
#de um produto e seu código de origem, mostre o preço junto de
#sua procedência. Caso o código não seja nenhum dos
#especificados, o produto deve ser encarado como importado.
#Siga a tabela de códigos.

preco= float(input("Digite o preço: "))
codigo= float(input("Digite o código de origem: "))

if codigo==1:
    print("Procedência: Sul")
    print("Preço: %.2f" %preco)

elif codigo==2:
    print("Procedência: Norte")
    print("Preço: %.2f" %preco)


elif codigo==3:
    print("Procedência: Leste")
    print("Preço: %.2f" %preco)


elif codigo==4:
    print("Procedência: Oeste")
    print("Preço: %.2f" %preco)


elif codigo==5 or codigo==6:
    print("Procedência: Nordeste")
    print("Preço: %.2f" %preco)


elif codigo==7 or codigo==8 or codigo==9:
    print("Procedência: Sudeste")
    print("Preço: %.2f" %preco)

elif codigo>=10 and codigo<=20:
    print("Procedência: Centro-Oeste")
    print("Preço: %.2f" %preco)

elif codigo>=25 and codigo<=30:
    print("Procedência: Noroeste")
    print("Preço: %.2f" %preco)

else:
    print("O produto é importado")
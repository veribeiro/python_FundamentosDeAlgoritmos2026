#Exercício 2 :Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado 
#assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a
#pagar, sabendo que:
#* o carro custa R$ 60,00 por dia
#*  e R$ 0,15 por km rodado.

km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

totalPagar = (dias*60)+(km*0.15)

print("Total a pagar %.2f" % totalPagar)

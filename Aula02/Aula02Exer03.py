#Exercício 3 :Faça um programa que solicita do usuário uma quantidade de dias, horas, minutos e segundos. 
# Calcule e imprima o total convertido em somente segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

totalSeg= (dias*86400) + (horas*3600) + (minutos*60) + segundos
print("Tempo total foi de %d" %totalSeg, "segundos")
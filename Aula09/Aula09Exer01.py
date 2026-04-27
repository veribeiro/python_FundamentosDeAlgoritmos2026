#  Faça um programa que leia uma quantidade indeterminada de
# números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada
# de dados deverá terminar quando for lido um número negativo.

lista=[]

while True:
    numero=int(input("Digite um número: "))

    if numero<0:
        break

    lista.append(numero)

def intervalo1(num):
    contador1=0
    if num>=0 and num<=25:
        contador1+=1
        return contador1
    
def intervalo2(num):
    contador2=0
    if num>=26 and num<=50:
        contador2+=1
        return contador2

def intervalo3(num):
    contador3=0
    if num>=51 and num<=75:
        contador3+=1
        return contador3
    
def intervalo4(num):
    contador4=0
    if num>=76 and num<=100:
        contador4+=1
        return contador4


intervaloPrimeiro = filter(intervalo1, lista)
print("Resultado de números que estão no intervalo: [0-25]:")
print(len(list(intervaloPrimeiro)))
print("\n")

intervaloSegundo = filter(intervalo2, lista)
print("Resultado de números que estão no intervalo: [26-50]:")
print(len(list(intervaloSegundo)))
print("\n")

intervaloTerceiro = filter(intervalo3, lista)
print("Resultado de números que estão no intervalo: [51-75]:")
print(len(list(intervaloTerceiro)))
print("\n")

intervaloQuarto = filter(intervalo4, lista)
print("Resultado de números que estão no intervalo: [76-100]:")
print(len(list(intervaloQuarto)))
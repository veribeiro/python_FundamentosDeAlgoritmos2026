# Calcular a somatória de valores digitados pelo usuário:
# ▶ Continue somando até que o número 0 (zero) seja digitado;
# ▶ Quando o 0 for digitado o resultado da somatória é exibido;
acumulador=0

while True:
    num = int(input("Digite um número: "))
    acumulador+=num

    if num==0:
        print("A somatória de todos os números são: ",acumulador)
        break
    

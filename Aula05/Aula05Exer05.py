#  Faça um programa que solicita um número entre 0 e 10
# ▶ Mostre uma mensagem de erro caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
# ▶ Quando o valor for válido dê a mensagem “número aceito”.
# ▶ Dica: você pode utilizar operadores lógicos (and ou or) na
# condição do while também!
numeros=int(input("Digite um número entre 0 e 10: "))
i=0

while i<=numeros:
    if(numeros>=0 and numeros<=10):
        print("Número aceito")
        break
    
    else:
        print("Número inválido, digite novamente")
        numeros=int(input("Digite um número entre 0 e 10: "))
        
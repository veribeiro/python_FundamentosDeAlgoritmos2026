votos = [0] * 7
nomes = ["", "Windowns Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

print("Informe o voto de 1 a 6")

while True:
    voto = int(input("Informe o número do seu voto: "))

    if voto ==0:
        break

    elif 1 <= voto <= 6: #É como se fosse: voto >= 1 and voto <= 6
        votos[voto] +=1 #você transformou o dado (o número do voto) no próprio endereço (o índice) da lista.
        # Se o usuário digita 3: O Python vai direto na lista[3] e soma 1.
    else:
        print("Opção inválida")

totalVotos = sum(votos)

print(f"\n{'Sistema Operacional':<20} {'Votos':<10} {'%':<10}") # reserva um bloco de 20 ou 10 espaços na tela para o título.
print("-"*40)

mais_votado = 0
vencedor = ""

for i in range(1, 7):
    if totalVotos > 0:
        percentual = (votos[i]/totalVotos) *100
    else:
        percentual=0
    
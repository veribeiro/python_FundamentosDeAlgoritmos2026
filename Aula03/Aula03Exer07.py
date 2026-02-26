# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km
#Calcule o preço da passagem:
#▶ cobrando R$ 0,50 por km para viagens até 200 km
#▶ R$ 0,45 por km para viagens mais longas.
#Observação: Resolva usando apenas Estruturas de Decisão Completas.

distanciaKm = int(input("Qual é a distância que deseja percorrer em km "))

if distanciaKm<=200:
    total = distanciaKm*0.50
    print("Você irá pagar: R$ %.2f"% total)

else:
    total = distanciaKm*0.45
    print("Você irá pagar: R$ %.2f"% total)
# Escreva um programa que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos de
# combustível, em que são fornecidos a altura e o raio do cilindro. Sabendo que:
# ▶ O preço da lata de tinta é de acordo com a quantidade:
# ⋆ Na compra de 1 lata o valor unitário é de R$ 50,00
# ⋆ Na compra de 2 latas o valor unitário é de R$ 48,00
# ⋆ Na compra de 3 latas o valor unitário é de R$ 46,00
# ⋆ Na compra de mais que 3 latas o valor unitário é de R$ 45,00
# ▶ Uma lata de tinta tem 5 litros
# ▶ Um litro cobre 3mš
# ▶ A área do cilindro é a área da base somada com a área da lateral
# ▶ A área da base é π × r
# 2 (r = raio, π = 3.1415)
# ▶ A área da lateral é altura multiplicada pelo perímetro
# ▶ O perímetro é 2 × π × r

from math import ceil

altura = float(input("Altura: "))
raio = float(input("Raio: "))

areabase = 3.1415 * raio**2
arealateral = altura * (2*3.1415*raio)
areaCilindro = areabase + arealateral

arredondadoAreaCilindro = ceil(areaCilindro)
arredondadoAreaBase = ceil(areabase)

print("Área a ser pintada: %.2f"% areaCilindro)
print("Qtde de litros necessários: %.2f"% areabase)

qtdeLatasTinta = areabase / 5
arredondadoQtdedeLatasTinta = ceil(qtdeLatasTinta)

print("Qtde de latas de tinta: ", arredondadoQtdedeLatasTinta)

if arredondadoQtdedeLatasTinta == 1:
    print("Preço unitário da lata: R$ 50.00")
    custoTotal = 50*arredondadoQtdedeLatasTinta
    print("Custo total: R$ %.2f" %custoTotal)

elif arredondadoQtdedeLatasTinta == 2:
    print("Preço unitário da lata: R$ 48.00")
    custoTotal = 48*arredondadoQtdedeLatasTinta
    print("Custo total: R$ %.2f" %custoTotal)

elif arredondadoQtdedeLatasTinta == 3:
    print("Preço unitário da lata: R$ 46.00")
    custoTotal = 46*arredondadoQtdedeLatasTinta
    print("Custo total: R$ %.2f" %custoTotal)

elif arredondadoQtdedeLatasTinta > 3:
    print("Preço unitário da lata: R$ 45.00")
    custoTotal = 45*arredondadoQtdedeLatasTinta
    print("Custo total: R$ %.2f" %custoTotal)

else:
    print("Valor não aceito")

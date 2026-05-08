# Faça um programa que leia uma a um modelos de cinco carros (exemplos: FUSCA, GOL, VECTRA etc) e os guarde em uma mesma lista. Leia (um a um) uma outra lista  com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros.

# 1. Entrada de dados
carros = []
consumos = []

print("Digite os modelos dos 5 carros:")
for _ in range(5):
    carros.append(input().upper())

print("Digite o consumo (km/l) de cada um:")
for _ in range(5):
    consumos.append(float(input()))

# 2. Identificar o mais econômico
# O mais econômico é o que tem o MAIOR km/l
maior_consumo = max(consumos)
indice_economico = consumos.index(maior_consumo)
carro_economico = carros[indice_economico]

# 3. Exibir resultados e cálculos
print("\nResultado:")
# Exibe os nomes dos carros
for c in carros:
    print(c)

# Exibe os consumos originais
for con in consumos:
    print(int(con))

print(carro_economico)

# Cálculo para 1000 km
# Fórmula: 1000 / consumo
for con in consumos:
    litros_necessarios = 1000 / con
    print(int(litros_necessarios))
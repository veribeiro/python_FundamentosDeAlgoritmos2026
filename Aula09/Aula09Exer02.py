# 1. Inicializa o vetor com 7 posições (índices 0 a 6)
# O índice 0 será ignorado, usaremos de 1 a 6.
votos = [0] * 7
nomes = ["", "Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

print("Informe o voto (1 a 6) ou 0 para encerrar:")

# 2. Loop para leitura dos dados
while True:
    voto = int(input("Voto: "))
    
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto] += 1
    else:
        print("Opção inválida! Digite um número entre 1 e 6.")

# 3. Cálculo do total
total_votos = sum(votos)

# 4. Saída formatada
print(f"\n{'Sistema Operacional':<20} {'Votos':<10} {'%':<10}")
print("-" * 40)

mais_votado = 0
vencedor = ""

for i in range(1, 7):
    if total_votos > 0:
        percentual = (votos[i] / total_votos) * 100
    else:
        percentual = 0
        
    print(f"{nomes[i]:<20} {votos[i]:<10} {percentual:.0f}%")
    
    # Lógica para achar o vencedor
    if votos[i] > mais_votado:
        mais_votado = votos[i]
        vencedor = nomes[i]

print("-" * 40)
print(f"Total: {total_votos}")
print(f"\nO sistema mais votado foi o {vencedor}, com {mais_votado} votos, correspondendo a { (mais_votado/total_votos)*100 if total_votos > 0 else 0:.0f}% dos votos.")
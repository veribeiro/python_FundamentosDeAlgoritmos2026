N = []
qtadeNum = int(input())

for r in range(qtadeNum):
    N.append(int(input()))

menor=0
maior=0
soma=0

for i in N:
    if i<menor:
       menor=i
    
for l in N:
    if l>maior:
       maior = l
    
for m in N:
    soma += m
    
media = soma/len(N)

menor_depoisDaVirgula = f"{menor:.2f}"
maior_depoisDaVirgula = f"{maior:.2f}"
media_depoisDaVirgula = f"{media:.2f}"

lista=[menor_depoisDaVirgula, maior_depoisDaVirgula, media_depoisDaVirgula]
print(*lista)
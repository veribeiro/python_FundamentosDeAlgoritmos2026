lista = []

qtdeNum = int(input())

for i in range(qtdeNum):
   lista.append(int(input()))

inverso = []

for l in range(len(lista)-1, -1, -1):
   inverso.append(lista[l])

for inverso in inverso:
    print(inverso)
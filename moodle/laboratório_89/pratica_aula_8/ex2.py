lista = []
qtdeNum = int(input())

for i in range(qtdeNum):
    lista.append(int(input()))

for l in range(2, len(lista)):
    elemento = lista[l]
    anterior1 = lista[l-1]
    anterior2 = lista[l-2]

    if elemento>(anterior1+anterior2):
        print(elemento)
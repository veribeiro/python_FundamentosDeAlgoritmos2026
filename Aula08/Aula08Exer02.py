#  Mostre o menor valor dentro da lista T = [11, 7, 2, 4]

T=[11, 7, 2, 4]
x = len(T)
for elemento in T:
    if elemento<x:
        x=elemento
        print(x)
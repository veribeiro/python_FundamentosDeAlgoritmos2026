# Faça um programa que:
# ▶ Leia 5 valores do usuário e armazene-os em uma lista
# ▶ Imprima a lista completa
# ▶ Imprima o primeiro e o último elemento da lista

lista=[]
for i in range(0, 5):
    lista.append(int(input("Insira um número: ")))

print(lista)
print("Primeiro elemento: ",lista[0]," e último elemento: ", lista[4])

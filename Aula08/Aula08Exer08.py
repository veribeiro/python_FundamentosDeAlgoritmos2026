#  Neste exercício, você criará um programa que lê palavras do
# usuário até que o usuário entre com uma linha em branco.
# Após o usuário digitar uma linha em branco, seu programa deve
# exibir cada palavra digitada pelo usuário exatamente uma vez.
# As palavras devem ser exibidas na mesma ordem em que foram
# inseridas.

lista = []

while True:
    palavra = input("Digite uma palavra (Para parar apenas digite algo vazio): ")
    

    if palavra == '':
        break

    lista.append(palavra)

print("\nPalavras digitadas:")
for linha in lista:
    print(linha, end="\n")





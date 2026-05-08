lista=[]

while True:
    palavra = input()
    
    if palavra == '':
        break
    
    lista.append(palavra)
    
for linha in lista:
    print(linha)
#  Escreva uma função chamada procuraChave que encontre todas as
# chaves, em um dicionário, que estão associadas a um valor específico.
# A função receberá o dicionário e o valor a procurar como seus únicos parâmetros.
# A função retornará uma lista (possivelmente vazia) de chaves
# associadas ao valor fornecido.
# Faça um programa principal que mostra o funcionamento da função.
# Seu programa principal deve criar um dicionário e mostrar que
# a função procuraChave funciona corretamente quando retorna
# várias chaves, uma única chave ou nenhuma chave.

# 1. Definição da função
def procuraChave(dicionario, valor_procurado):
    chaves_encontradas = []
    
    # Percorre cada par do dicionário
    for chave, valor in dicionario.items():
        # Se o valor da chave atual for igual ao que buscamos
        if valor == valor_procurado:
            chaves_encontradas.append(chave)
            
    return chaves_encontradas

# 2. Programa Principal
meu_dict = {'alpha': 1, 'bravo': 2, 'charlie': 1, 'delta': 3, 'echo': 1}

print("Dicionario:")
print(meu_dict)

# Teste 1: Várias chaves (procurando valor 1)
resultado1 = procuraChave(meu_dict, 1)
print(f"\nProcurando chaves com valor 1\n{resultado1}")

# Teste 2: Uma única chave (procurando valor 3)
resultado2 = procuraChave(meu_dict, 3)
print(f"\nProcurando chaves com valor 3\n{resultado2}")

# Teste 3: Nenhuma chave (procurando valor 4)
resultado3 = procuraChave(meu_dict, 4)
print(f"\nProcurando chaves com valor 4\n{resultado3}")
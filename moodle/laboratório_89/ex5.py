# Implemente uma função chamada analise que recebe uma lista e retorne a media, mediana, o valor mínimo e o máximo respectivamente, independente do tamanho da lista.

def analise(lista):
    # 1. Média: soma de tudo dividido pela quantidade
    media = sum(lista) / len(lista)
    
    # 2. Valor Mínimo e Máximo: funções prontas do Python
    minimo = min(lista)
    maximo = max(lista)
    
    # 3. Mediana: o valor do meio
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    meio = tamanho // 2
    
    if tamanho % 2 == 0:
        # Se for par, a mediana é a média dos dois valores centrais
        mediana = (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        # Se for ímpar, é o valor exatamente no meio
        mediana = lista_ordenada[meio]
        
    return media, mediana, minimo, maximo

# Teste do exemplo:
print(analise([2, 5, 7, -2, 8]))
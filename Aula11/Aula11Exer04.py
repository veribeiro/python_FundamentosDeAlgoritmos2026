# Crie uma função que retorna o número de caracteres únicos em
# uma string criada pelo usuário.
# Por exemplo:
# “Hello, World!” tem 10 caracteres únicos
# enquanto zzz tem somente 1 caractere único.
# Use um dicionário para resolver este problema.

def contar_caracteres_unicos(frase):
    # Criamos um dicionário vazio
    dicionario_unicos = {}
    
    for caractere in frase:
        # Adicionamos o caractere como chave. 
        # O valor (1) não importa muito aqui, o foco é a chave existir.
        dicionario_unicos[caractere] = 1
            
    # O tamanho (len) do dicionário será o total de chaves únicas
    return len(dicionario_unicos)

# Programa Principal
texto1 = "Hello, World!"
texto2 = "zzz"

print(f"Número de caracteres únicos:")
print(f"{texto1}: {contar_caracteres_unicos(texto1)}")
print(f"{texto2}: {contar_caracteres_unicos(texto2)}")
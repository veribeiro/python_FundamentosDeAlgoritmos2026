# Duas palavras são anagramas se contiverem todas as mesmas
# letras, mas em uma ordem diferente.
# Por exemplo: estante e setenta são anagramas.
# Crie uma função que recebe duas strings do usuário e determina se elas são ou não anagramas.
# Utilize dicionário para resolver o problema.

def contar_letras(palavra):
    # Remove espaços e deixa tudo minúsculo para a comparação ser justa
    palavra = palavra.replace(" ", "").lower()
    contagem = {}
    
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

def verificar_anagrama(s1, s2):
    # Duas palavras de tamanhos diferentes (sem contar espaços) 
    # nunca serão anagramas
    if len(s1.replace(" ", "")) != len(s2.replace(" ", "")):
        return False
    
    return contar_letras(s1) == contar_letras(s2)

# Programa Principal
p1 = input("Digite uma palavra: ")
p2 = input("Digite outra palavra: ")

if verificar_anagrama(p1, p2):
    print("São anagramas")
else:
    print("Não são anagramas")
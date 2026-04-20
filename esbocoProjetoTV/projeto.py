#Lista de livros
livros = ['Quarta Asa', 'Trono de vidro', 'Acotar', 'Powerless', 'Orgulho e preconceito', 'Jogos vorazes', 'A noiva',
        'A empregada', 'Verity', 'Assistente do vilão', 'O príncipe cruel', 'Mentirosos', 'Divinos rivais', '1984',
        'A hora da estrela', 'O cortiço', 'A revolução dos bichos', 'Pequeno príncipe', 'Harry Potter', 'As crônicas de Nárnia', 
        'Percy Jackson']

#Menu
def menu_principal():
    while True:
        #Colocar os mais curtidos(lembrar de fazer depois)
        print("====Menu====")
        print("Buscar vídeo[aperte m]")
        print("Sair [aperte s]")
        print("\n")
        acaoUsuario = input("O que você deseja fazer? ")

        #Buscar vídeo
        if acaoUsuario == 'm':
            busca = str(input("Digite sua busca: "))
            if busca in livros:
                print("Encontrado!")
                busca_livro()
            else:
                print("Não encontrado!")
        elif acaoUsuario == 's':
            break

# Resultado depois da busca
def busca_livro():
    while True:
        print("\n====O que você deseja fazer com essa busca?====")
        #Opções para listar informações do vídeo, curtir ou descurtir, adcionar ou excluir vídeo dos favoritos
        print("Obter informações do vídeo [aperte p]")
        print("Sair [aperte s]")
        acaoUsuarioBusca= input("\nO que deseja fazer? ")

        if acaoUsuarioBusca == 'p':
            print("Informações") # (É necessário criar uma outra função apenas para informações)
        elif acaoUsuarioBusca == 's':
            break

# Informações iniciais para o usuário (Essa é a primeira coisa que o usuário visualiza)
print("====Seja bem-vindo!====")
print("Já possui uma conta ou deseja criar uma?")
possuiConta = str(input("Digite [s] se já possui conta ou digite [n] se não possue conta: "))

#Se o usuário possui a conta
if possuiConta == "s" or possuiConta=="S":
    print("\n")
    print("====Login usuário====")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    print("\n")
    menu_principal()

#Se o usuário não possui uma conta
elif possuiConta == "n" or possuiConta=="N":
    print("\n")
    print("====Cadastrar usuário====")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    idade = int(input("Digite sua idade: "))
    senha = input("Digite seu senha: ")

    if idade<18:
        print("Acesso negado - Menor de idade")
    elif idade>18:
        print("\n")
        print("Acesso permitido")
        print("Cadastro realizado com sucesso!")
        print("Faça login agora")

    
else:
    print("\n")
    print("Ocorreu um erro, o tipo de caractere que você digitou não faz parte do que foi solicitado")


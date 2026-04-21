
#Lista de livros
livros = ['Quarta Asa', 'Trono de vidro', 'Acotar', 'Powerless', 'Orgulho e preconceito', 'Harry Potter', 'O Príncipe Cruel',
        'A empregada', 'Verity', 'Assistente do vilão']

# Parte usuário função
#Menu
def menu_principal():
    while True:
        print("\n \n Navegação: Login >> Menu")
        #Colocar os mais curtidos(lembrar de fazer depois)
        print("==== MENU ====")
        print("Buscar vídeo [aperte m]")
        print("Sair [aperte s]")
        print("\n")
        acaoUsuario = input("O que você deseja fazer? ")

        #Buscar vídeo
        if acaoUsuario == 'm':
            busca = str(input("Digite sua busca: ")).strip()
            if busca in livros:
                print("Encontrado!")
                busca_livro(busca)
            else:
                print("Não encontrado!")
        elif acaoUsuario == 's':
            break


# Resultado depois da busca
def busca_livro(video_buscado):
    while True:
        print("------------------------------------------------------------------------------")
        print("\n \n Navegação: Login >> Menu >> Buscar vídeo")
        print("\n==== O QUE VOCÊ DESEJA FAZER COM ESSA BUSCA? ====")
        #Opções para listar informações do vídeo, curtir ou descurtir, adcionar ou excluir vídeo dos favoritos
        print("1 - Obter informações do vídeo")
        print("2 - Curtir vídeo ")
        print("3 - Descurtir vídeo ")
        print("4 - Adicionar o vídeo em favoritos")
        print("5 - Excluir o vídeo em favoritos")
        print("Sair [digite s]")
        acaoUsuarioBusca= input("\nO que deseja fazer? ")

        # Para info do livro
        if acaoUsuarioBusca == '1':
            info_livro(video_buscado)
        
        # Para adcionar aos favoritos
        elif acaoUsuarioBusca == '4':
            print("Adcionar favorito")

        elif acaoUsuarioBusca == 's' or acaoUsuarioBusca == 'S':
            break

def info_livro(nome_video):
    while True:
        print("------------------------------------------------------------------------------")
        print("\n \n Navegação: Login >> Menu >> Buscar vídeo >> Informações do vídeo")
        print(f"\n==== OBTER INFORMAÇÕES DO VÍDEO {nome_video} ===")
        print("Continuar para visualizar as informações do vídeo [digite c]")
        print("Sair [digite s]")
        print("\n")
        acaoUsuarioInfo = input("O que você deseja fazer? ")
        if acaoUsuarioInfo=='c': #É necessário você tranformar isso em DOCUMENTO ou DICIONÁRIO
            print("Visualizando Sinopse, Duração e Gênero do vídeo:\n")
            if nome_video == 'Quarta Asa':
                print("--> Sinopse: Em Quarta Asa, best-seller #1 do The New York Times, uma jovem precisa sobreviver " \
                "ao treinamento em uma escola de elite para poderosos cavaleiros de dragões, onde a única regra é se formar... ou morrer tentando. \n \nViolet Sorrengail, uma jovem de vinte anos, " \
                "estava destinada a entrar na Divisão dos Escribas, levando uma vida relativamente tranquila entre os livros e as aulas de História. No entanto, a general comandante das forças de Navarre - " \
                "também conhecida como sua mãe, durona como as garras de um dragão, ordena que Violet se junte às centenas de candidatos que buscam se tornar a elite de seu país: cavaleiros de dragões. \n \n" \
                "* Obs: Sinopse feita pela editora 'Planeta Minotauro'")
                print("--> Duração: 2h 50m")
                print("--> Gênero: Ficção, fantasia")
            elif nome_video == 'Trono de vidro':
                print("--> Sinopse: LETAL. LEAL. LENDÁRIA. \n \n" \
                    "Celaena Sardothien fará de tudo para conquistar a liberdade. Entretanto, o castelo de vidro esconde muitos segredos e abriga um mal do qual ela deseja escapar. Tornar-se a Campeã do Rei pode ser a chave da libertação de Celaena, mas a que custo? \n \n" \
                    "*Obs: Sinopse feita pela editora 'Galera'")
                print("--> Duração: 2h 30m")
                print("--> Gênero: Ação e Aventura, Fantasia Épica")
            elif nome_video == 'Acotar':
                print("--> Sinopse: UMA CAÇADORA DETERMINADA. UM FEÉRICO AMALDIÇOADO. E UM CORAÇÃO MORTAL QUE PODE SER A SALVAÇÃO DE UM REINO MÁGICO. \n \n " \
                "* Obs: Sinopse feita pela editora 'Galera'")
                print("--> Duração: 2h 50m")
                print("--> Gênero: Fantasia romântica, fantasia adulta")
            elif nome_video == 'Powerless':
                print("--> Sinopse: Kai é um príncipe poderoso, treinado para matar. Paedyn é uma garota comum que sobrevive fingindo ter poderes. \n \n " \
                "Quando os caminhos dos dois se encontram por acaso. eles não imaginam que serão oponentes em uma competição mágica brutal. Nem que se verão envolvidos em um romance proibido e perigoso tão impossível quanto inevitável. \n \n" \
                "* Obs: Sinopse feita pela editora 'Rocco'")
                print("--> Duração: 2h 30m")
                print("--> Gênero: Fantasia")
            elif nome_video == 'Orgulho e preconceito':
                print("--> Sinopse: Orgulho e Preconceito é um dos mais aclamados romances da escritora inglesa Jane Austen. Publicado em 1813, revela como era a sociedade da época, quando os relacionamentos se desenrolavam de maneira mais lenta e romântica, no ritmo das cartas levadas por mensageiros a cavalo. \n \n " \
                "Nesse mundo, o sonho da Sra. Bennet era casar bem suas cinco filhas: Jane, Elizabeth, Mary, Kitty e Lydia. Entre as irmãs, destaca-se Elizabeth, a Lizzy, que se depara com um turbilhão de sentimentos diante do orgulho e preconceito que mascaram a realidade. Trata-se de um clássico que, mesmo após duzentos anos desde a sua primeira publicação, " \
                "continua a encantar milhões de leitores ao redor do mundo. \n \n " \
                "*Obs: Sinopse feita pela editora 'Camelot'")
                print("--> Duração: 1h 40m")
                print("--> Gênero: Drama, Comédia, Romance")
        
        elif acaoUsuarioInfo == 's':
            break


# Parte adm função
def menu_principal_adm():
    while True:
        print("\n \n Navegação: Login do administrador >> Menu")
        print("==== MENU ====")
        print("1-Cadastrar livro:")
        print("2-Excluir livro:")
        print("4-Sair")
        print("\n")
        opcaoAdm = input("O que você deseja fazer? ")

        if opcaoAdm == "1":
            print("\n--Cadastrar livro--")
            nome=input("Digite o nome do livro: ")
            livros.append(nome)
            print("Livro cadastrado com sucesso!")
        
        elif opcaoAdm == "2":
            print("\--Excluir livro--")
            nome=input("Nome do livro que deseja deletar: ")
            print("livro excluido com sucesso!")
        
        elif opcaoAdm == "4":
            break

# Informações iniciais para o usuário (Essa é a primeira coisa que o usuário visualiza)
print("====Seja bem-vindo!====")
print("Já possui uma conta ou deseja criar uma?")
print("//Digite [a] para entrar em conta corporativa// -> Acesso apenas para funcionários")
possuiConta = str(input("Digite [s] se já possui conta usuário ou digite [n] se não possue conta usuário: "))

#Se o usuário possui a conta
if possuiConta == "s" or possuiConta=="S":
    print("\n")
    print("====Login usuário====")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    print("------------------------------------------------------------------------------")
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
    print("------------------------------------------------------------------------------")

    if idade<18:
        print("Acesso negado - Menor de idade")
            
    elif idade>18:
        print("\n")
        print("Acesso permitido")
        print("Cadastro realizado com sucesso!")
        print("Faça login agora")

# Parte apenas para funcionários
elif possuiConta == "a" or possuiConta=="A":
    print("\n")
    print("====Seja bem vindo, funcionário!====")
    print("Deseja logar sua conta como administrador?")
    logarConta = str(input("Digite [n] se não deseja ou digite [s] para logar conta: "))
    
    if logarConta == "n" or logarConta =="N":
        print("\n")
        print("Sem problema, basta seguir o login padrão e escolher a opção de usuário comum.")

    # login do adm
    elif logarConta == "s" or logarConta =="S":
        print("\n")
        print("--login administrador--")
        adm = input("Digite seu nome completo: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        print("\n")
        print("Acesso com sucesso. Bem-vindo,administrador!")
        menu_principal_adm()
    else:
        print("\n")
        print("Ocorreu um erro, o tipo de caractere que você digitou não faz parte do que foi solicitado")

    
else:
    print("\n")
    print("Ocorreu um erro, o tipo de caractere que você digitou não faz parte do que foi solicitado")


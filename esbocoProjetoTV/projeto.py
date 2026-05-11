listaUsuarios = [] #Vai armazenar a lista de usuários depois. Essa lista está na função cadastrar_usuario()
import os

def inicializar_catalogo():
    # Verifica se o arquivo não existe ou está vazio
    if not os.path.exists('videos.txt') or os.path.getsize('videos.txt') == 0:
        videos_iniciais = [
            "QUARTA ASA\tEm Quarta Asa, best-seller #1 do The New York Times,  uma jovem precisa sobreviver ao treinamento\\nem uma escola de elite para poderosos cavaleiros de dragões, onde a única regra é se formar... ou morrer tentando.\\nViolet Sorrengail, uma jovem de vinte anos, estava destinada a entrar na Divisão dos Escribas,\\nlevando uma vida relativamente tranquila entre os livros e as aulas de História. No entanto, a general comandante das forças de Navarre -\\ntambém conhecida como sua mãe, durona como as garras de um dragão, ordena que Violet\\nse junte às centenas de candidatos que buscam se tornar a elite de seu país: cavaleiros de dragões.\\n* Obs: Sinopse feita pela editora 'Planeta Minotauro'\t2h 50m\tFicção, fantasia\tRebecca Yarros\n",
            "TRONO DE VIDRO\t'LETAL. LEAL. LENDÁRIA.\\nCelaena Sardothien fará de tudo para conquistar a liberdade.\\nEntretanto, o castelo de vidro esconde muitos segredos e abriga um mal do qual ela deseja escapar.\\nTornar-se a Campeã do Rei pode ser a chave da libertação de Celaena, mas a que custo?'\\n* Obs: Sinopse feita pela editora 'Galera'\t2h 30m\tAção e Aventura, Fantasia Épica\tSarah J. Maas\n"
            "ACOTAR\t'UMA CAÇADORA DETERMINADA. UM FEÉRICO AMALDIÇOADO. E UM CORAÇÃO MORTAL QUE PODE SER A SALVAÇÃO DE UM REINO MÁGICO.'\\n* Obs: Sinopse feita pela editora 'Galera'\t2h 50m\tFantasia romântica, fantasia adulta\tSarah J. Maas\n"
            "POWERLESS\t'Kai é um príncipe poderoso, treinado para matar. Paedyn é uma garota comum que sobrevive fingindo ter poderes.\\nQuando os caminhos dos dois se encontram por acaso. eles não imaginam que serão oponentes em uma competição mágica brutal.\\nNem que se verão envolvidos em um romance proibido e perigoso tão impossível quanto inevitável.'\\n* Obs: Sinopse feita pela editora 'Rocco'\t2h 30m\tFantasia\tLauren Roberts\n"
            "ORGULHO E PRECONCEITO\t'Orgulho e Preconceito é um dos mais aclamados romances da escritora inglesa Jane Austen.\\nPublicado em 1813, revela como era a sociedade da época,\\nquando os relacionamentos se desenrolavam de maneira mais lenta e romântica,\\nno ritmo das cartas levadas por mensageiros a cavalo.\\nNesse mundo, o sonho da Sra. Bennet era casar bem suas cinco filhas: Jane, Elizabeth, Mary, Kitty e Lydia.\\nEntre as irmãs, destaca-se Elizabeth, a Lizzy, que se depara com um turbilhão de sentimentos\\ndiante do orgulho e preconceito que mascaram a realidade.\\nTrata-se de um clássico que, mesmo após duzentos anos desde a sua primeira publicação,\\ncontinua a encantar milhões de leitores ao redor do mundo.'\\n* Obs: Sinopse feita pela editora 'Camelot'\t1h 40m\tDrama, Comédia, Romance\tJane Austen\n"
            "HARRY POTTER\t'HARRY POTTER nunca tinha ouvido falar em Hogwarts até o momento em que as CARTAS começam a aparecer\\n no capacho do número 4 da rua dos Alfeneiros.\\nEndereçadas com TINTA VERDE em pergaminho amarelado com um LACRE PÚRPURA, elas são rapidamente confiscadas por seus tios TERRÍVEIS.\\nE então, no décimo primeiro aniversário de Harry, um homem GIGANTESCO com olhos luzindo\\ncomo besouros negros chamado RÚBEO HAGRID entra intempestivamente com uma notícia ASSOMBROSA:\\nHarry Potter é um bruxo e tem uma vaga na ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS.\\nUma aventura inacreditável está para começar!'\\n* Obs: Sinopse feita pela editora 'ROCCO'\t2h 00m\tFantasia, Ficção\tJ.K. Rowling\n"
            "O PRINCIPE CRUEL\t'Da autora de best-sellers nº 1 do The New York Times , Holly Black, O prínicipe cruel\\né o primeiro livro da envolvente série O Povo do Ar sobre uma garota mortal que se vê presa\\nem uma teia de intrigas de fadas reais.\\nJude tinha apenas sete anos quando seus pais foram brutalmente assasinados\\ne ela e as irmãs levadas para viver no traiçoeiro Reino das Fadas.\\nDez anos depois, tudo o que Jude quer é se encaixar, mesmo sendo uma garota mortal.\\nMas todos os feéricos parecem desprezar os humanos... Especialmente o príncipe Cardan,\\no mais jovem e mais perverso dos filhos do Grande Rei de Elfhame.\\nPara conquistar o tão desejado lugar na Corte, Jude precisa desafiar o príncipe\\n- e enfrentar as consequências do ato.'\\n* Obs: Sinopse feita pela editora 'Galera'\t1h 30m\tFantasia\tHolly Black\n"
            "A EMPREGADA\t'147 SEMANAS NA LISTA DE MAIS VENDIDOS DO THE NEW YORK TIMES\\nUma história que vai surpreender até os leitores de suspense mais calejados.\\nTodos os dias, Millie limpa a casa de Nina e Andrew Winchester de cima a baixo. Pega a filha deles na escola.\\nPrepara refeições deliciosas para a família toda antes de poder se recolher e enfim comer\\no próprio jantar, sozinha em seu quarto minúsculo e claustrofóbico no sótão.\\nAfinal, com seu passado problemático, ela tem mais é que agradecer por ter conseguido esse emprego.\\nLogo os Winchesters vão descobrir que não fazem a menor ideia de quem Millie é de verdade. Nem do que ela é capaz de fazer.'\\n* Obs: Sinopse feita pela editora 'Arqueiro'\t1h 50m\tMistério\tFreida McFadden\n"
            "VERITY\t'Distintamente sinistro, com um verdadeiro toque de Colleen Hoover. Por anos esperei, um thriller como esse.\\n— Tarryn Fisher, coautora da série Nunca Jamais\\nInstigante e surpreendente. Impossível largar.\\n— Claire Contreras, autora de Kaleidoscope Hearts\\nVasculho várias caixas e encontro manuscritos em diversos estágios do processo de escrita.\\nTodos são versões dos seis livros da série que ela já escreveu.\\nNão há nada que indique o que estava planejando escrever em seguida.\\nEstou na sexta caixa, esquadrinhando todo o seu conteúdo, até que encontro algo com um título diferente. Chama-se Que assim seja.\\nFolheio as primeiras páginas torcendo para ser um rascunho do sétimo livro da série.\\nMas quase imediatamente vejo que não é. É algo mais... pessoal. Volto à primeira página do primeiro capítulo e começo a ler.\\nÀs vezes penso na noite em que conheci Jeremy e me pergunto: se não tivéssemos cruzado nossos olhares,\\nminha vida teria terminado do mesmo jeito?'\\n* Obs: Sinopse feita pela editora 'Galera Record'\t1h 50m\tMistério\tColleen Hoover\n"
            "ASSISTENTE DO VILÃO\t'PROCURA-SE ASSISTENTE:\\nVilão notório do alto escalão busca assistente leal e equilibrado\\npara funções de escritório não especificadas, apoio à equipe para caos e terror aleatórios e outras Coisas Sombrias em Geral.\\nDiscrição é essencial. Excelentes benefícios.\\nReferir-se ao chefe apenas como uma 'pessoa' parecia insuficiente.\\nEm muitos aspectos, ele era extraordinário, mas ser responsável por todas as suas vontades\\ne necessidades acabara por torná-lo mais humano aos olhos dela.\\nO véu misterioso que o cobria quando Evie começara o trabalho tinha desaparecido, e uma imagem bem mais clara estava formada em sua mente.\\nMesmo assim, ela ainda tinha muito a aprender.\\nComo, por exemplo, que tipo de escuridão espreitava dentro dele para que houvesse três cabeças penduradas naquele bendito teto.\\nSOS!\\n* Obs: Sinopse feita pela editora 'Globo'\t2h 30m\tFantasia, Mistério\tHannah Nicole Maehrer\n"
        ]
        
        with open('videos.txt', 'w', encoding='utf-8') as f:
            f.writelines(videos_iniciais)
        print("📥 Catálogo inicial de vídeos carregado com sucesso!")

inicializar_catalogo()

# Parte usuário funções
# Funcão para cadastrar usuário, armazenar variáveis em dicionário e criar um arquivo .txt
def cadastrar_usuario():
    with open('cadastroUsuarios.txt', 'a') as cadastroUsu: #Vai criar o documento cadastroUsuarios.txt
        while True:
            print("\n")
            print("====Cadastrar usuário====")
            nome = input("Digite seu nome (Ou digite [s] para sair): ")

            if nome.lower()=='s':
                break
            email = input("Digite seu email: ")
            idade = int(input("Digite sua idade: "))
            senha = input("Digite seu senha: ")


            if idade<18:
                print("Acesso negado - Menor de idade")

            if idade >=18:
                novoUsuario = {
                "nome": nome,
                "email": email,
                "idade": idade,
                "senha": senha,
                "curtidas": []
            }
            cadastroUsu.write(f'{nome}\t{email}\t{idade}\t{senha}\n')
            
            with open('cadastroUsuarios.txt') as cadastroUsu:
                for linha in cadastroUsu:
                    # Foi necessário criar essa condição pois estava com erro de valores que não estavam conseguindo ser verificados por causa das caracteres
                    if not linha.strip():
                        continue
                    dividido = linha.strip().split('\t')
                    if len(dividido) != 4: #Se a quantidade de itens for diferente de 4, vai pular a linha
                        continue
                    nome, email, idade, senha = dividido
            
                listaUsuarios.append(novoUsuario)
                print("Cadastro realizado com sucesso!")
                print("\n")
                print("Acesso permitido")
                print("Faça login agora")


def login_usuario(emailRecebido, senhaRecebido):
    with open('cadastroUsuarios.txt') as cadastro:
            
                for linha in cadastro: # É o mesmo loop da função cadastrar_usuario()
                    if not linha.strip():
                        continue
                    dividido = linha.strip().split('\t')
                    if len(dividido) != 4:
                        continue
                    nomeSalvo, emailSalvo, idadeSalvo, senhaSalvo = dividido

                    if emailSalvo==emailRecebido and senhaSalvo==senhaRecebido:
                    
                        # É necessário pegar o dicionário novamente para ter depois conseguir ter informações de curtidas
                        usuarioLogin = {
                            "nome": nomeSalvo,
                            "email": emailSalvo,
                            "idade": idadeSalvo,
                            "senha": senhaSalvo,
                            "curtidas": []
                        }

                        print(f'-- Seja bem-vindo {nomeSalvo}!')
                        return usuarioLogin

    return None

#Menu
def menu_principal():
    while True:
        print("\n \n Navegação: Login >> Menu")
        #Colocar os mais curtidos(lembrar de fazer depois)
        print("==== MENU ====")
        print("1 - Buscar vídeo")
        print("2 - Visualizar os mais curtidos")
        print("3 - Visualizar todo o catalógo de vídeos")
        print("4 - Visualizar meu histórico de curtidas")
        print("5 - Gerenciar favoritos")
        print("Sair [aperte s]")
        print("\n")
        acaoUsuario = input("O que você deseja fazer? ")

        #Buscar vídeo
        if acaoUsuario == '1':
            pesquisa()

        elif acaoUsuario == '2':
            top_cinco()

        elif acaoUsuario == '3':
            print("Navegação: Login >> Menu >> Visualizar todo o catalógo de vídeos")
            print("===VISUALIZAR TODO O CATALÓGO DE VÍDEOS===")
            mostrar_catalogo()

        elif acaoUsuario == '4':
            print("------------------------------------------------------------------------------")
            print("\n \n Navegação: Login >> Menu >> Visualizar histórico de curtidas")
            print("=== VISUALIZAR HISTÓRICO DE CURTIDAS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:
                visualizar_curtidos(usuario_logado)
        elif acaoUsuario == '5':
            gerenciar_favoritos()
        elif acaoUsuario == 's':
            break

def pesquisa():
    livros_armazenados = []
    try:
        with open('videos.txt', encoding='utf-8') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes)>=1:
                    livros_armazenados.append(partes[0].lower())
    except FileNotFoundError:
        print("O arquivo não foi encontrado")

            #Mostrar opções
    if livros_armazenados:
        print("=== Todos os vídeos disponíveis ===")
        for i, nome in enumerate(livros_armazenados, 1):
            print(f"{i} - {nome}")
        print("-----------------------------------------")

            #Pedir para o usuário buscar vídeo
        busca = input("\nDigite o nome ou o número do vídeo acima: ").strip().lower()
            #Verificar se o usuário digitou o nome ou número
        videoEncontrado = None

            #Se digitou o número
        if busca.isdigit(): #is digit() é uma função de string usada para verificar se todos os caracteres em uma string são dígitos numéricos (0-9).
            indice = int(busca)-1
            if 0<=indice<len(livros_armazenados):
                videoEncontrado = livros_armazenados[indice]
            
            #Verificar se o texto existe
        if not videoEncontrado:
            for livro in livros_armazenados:
                if busca == livro.lower():
                    videoEncontrado = livro
                    break
        if videoEncontrado:
            print("Encontrado!")
            busca_livro(videoEncontrado)
        else:
            print("Não encontrado!")
    else:
        print("Não há vídeos cadastrados")

def mostrar_catalogo():
    try:
        with open('videos.txt', encoding='utf-8') as lista:
            for i, linha in enumerate(lista, 1):
                #Contador para numerar os títulos
                partes = linha.strip().split('\t')

                if len(partes)>=1:
                    titulo = partes[0]
                    print(f"{i} - {titulo}")
            if i==0:
                print("Catalógo vazio")
    except FileNotFoundError:
        print("Arquivo não encontrado")

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

        elif acaoUsuarioBusca == '2':
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:  # garante que não é None
                curtir_livro(usuario_logado, video_buscado)

        elif acaoUsuarioBusca == '3':
            usuario_logado = login_usuario(email, senha)
            if usuario_logado: 
                descurtir_livro('curtidaLivros.txt', f'{usuario_logado["email"]}\t{video_buscado}')
        
        # Para adcionar aos favoritos
        elif acaoUsuarioBusca == '4':
            print("\n \n Navegação: Login >> Menu >> Buscar vídeo >> Informações do vídeo >> Adicionar vídeo em favoritos")
            print(f"\n==== ADICIONAR EM FAVORITOS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado: 
                adicionar_favoritos(usuario_logado["email"], video_buscado)

        elif acaoUsuarioBusca == '5':
            print("\n \n Navegação: Login >> Menu >> Buscar vídeo >> Informações do vídeo >> Excluir vídeo em favoritos")
            print(f"\n==== EXCLUIR EM FAVORITOS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado: 
                excluir_favorito(usuario_logado["email"], video_buscado)

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
        if acaoUsuarioInfo=='c' or acaoUsuarioInfo=="C": #É necessário você tranformar isso em DOCUMENTO ou DICIONÁRIO
            print("Visualizando Sinopse, Autor, Duração e Gênero do vídeo:\n")
            try:
                with open('videos.txt', encoding='utf-8') as lista:
                    for linha in lista:
                        partes = linha.strip().split('\t')

                        if len(partes)==5:
                            titulo, sinopse, duracao, genero, autor = partes

                            if titulo.lower() == nome_video:
                                formatarSinopse = sinopse.replace("\\n", "\n")
                                print("\n"+"="*10)
                                print(f"TÍTULO: {titulo.upper()}")
                                print("-"*10)
                                print(f"SINOPSE: {formatarSinopse}")
                                print(f"DURAÇÃO: {duracao}")
                                print(f"GÊNERO: {genero}")
                                print(f"AUTOR: {autor}")
                                print("="*10)
                                break
            except FileNotFoundError:
                print("O arquivo não existe")

        elif acaoUsuarioInfo=='s' or acaoUsuarioInfo=='S':
            break

def curtir_livro(usuario_logado, nome_do_livro):
    email = usuario_logado["email"]

    with open('curtidaLivros.txt', 'a') as curtidasLivros:
    # Adiciona o livro à lista de curtidas do usuário
        if nome_do_livro not in usuario_logado["curtidas"]:
            usuario_logado["curtidas"].append(nome_do_livro)
            print("Livro curtido com sucesso")
        else:
            print("Livro já curtido")

        #Para saber o total de curtidas, basta medir o tamanho da lista:
        total = len(usuario_logado["curtidas"])
        print(f"Você tem {total} livros curtidos.")

        # Para não repetir os dados
        existe = False

        with open("curtidaLivros.txt") as curtidasLivrosVerificar:
            for linha in curtidasLivrosVerificar:
                emailsalvo, livrosalvo = linha.strip().split('\t')
                if emailsalvo == email and livrosalvo == nome_do_livro:
                    existe=True
                    break

        if not existe:
            with open("curtidaLivros.txt","a") as curtidasLivrosVerificar:
                curtidasLivrosVerificar.write(f'{email}\t{nome_do_livro}\n')

def descurtir_livro(nome_arquivo, remover):
    removido = False

    try:
        with open(nome_arquivo) as descurtirLivros:
            linhas = descurtirLivros.readlines()

        with open(nome_arquivo, 'w') as descurtirLivros:
            for linha in linhas:
                # Se a linha não for o que queria ser apagao, precisa reescrever
                if linha.strip() != remover:
                    descurtirLivros.write(linha)
                else:
                    removido = True
    
        if not removido:
            print("Esse livro não está na sua lista de curtidos")
        elif removido:
            print("Livro descurtido com sucesso!")
    except FileNotFoundError:
        print("Não há arquivo (você ainda não curtiu nenhum vídeo)")

def visualizar_curtidos(usuario_logado):
    email = usuario_logado["email"]
    contador = 1
    ha_curtidas = False

    try:
        with open('curtidaLivros.txt') as curtidas:
            for linha in curtidas:
                limpaLinha = linha.strip()
                if not limpaLinha:
                    continue

                emailsalvo, livro = limpaLinha.split('\t')

                if emailsalvo==email:
                    print(f"{contador}.{livro}")
                    contador +=1
                    ha_curtidas = True
    
        if not ha_curtidas:
            print("Você ainda não curtiu nenhum livro!")
    except FileNotFoundError:
        print("Você ainda não curtiu nenhum livro")

def gerenciar_favoritos():
    while True:
        print("\n \n Navegação: Login >> Menu >> Gerenciar favoritos")
        print("=== GERENCIAR FAVORITOS ===")
        print("1 - Criar lista de reprodução de vídeos favoritos")
        print("2 - Editar lista de reprodução criados")
        print("3 - Visualizar lista de reprodução já criados")
        print("4 - Excluir lista de reprodução de vídeos favoritos")
        print("Sair [aperte s]")
        print("\n")
        acaoUsuarioFavoritos = input("O que você deseja fazer? ")

        if acaoUsuarioFavoritos == '1':
            print("\n \n Navegação: Login >> Menu >> Gerenciar favoritos >> Criar lista de reprodução de vídeos favoritos")
            print("=== CRIAR LISTA DE VÍDEOS FAVORITOS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:  # garante que não é None
                criar_lista(usuario_logado["email"])

        elif acaoUsuarioFavoritos == '2':
            print("\n \n Navegação: Login >> Menu >> Gerenciar favoritos >> Editar lista de reprodução criados")
            print("=== EDITAR LISTA DE VÍDEOS FAVORITOS ===")
            print("* Você só pode editar os nomes de suas listas")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:  # garante que não é None
                editar_lista_nome(usuario_logado["email"])

        elif acaoUsuarioFavoritos == '3':
            print("\n \n Navegação: Login >> Menu >> Gerenciar favoritos >> Visualizar lista de reprodução já criados")
            print("=== VISUALIZAR LISTAS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:  # garante que não é None
                visualizar_lista(usuario_logado["email"])

        elif acaoUsuarioFavoritos == '4':
            print("\n \n Navegação: Login >> Menu >> Gerenciar favoritos >> Excluir lista de reprodução de vídeos favoritos")
            print("=== EXCLUIR LISTAS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:  # garante que não é None
                remover_lista(usuario_logado["email"])

        elif acaoUsuarioFavoritos == 's' or 'S':
            break

#Para criar lista de favoritos que o usuário quer (apenas criar o nome da lista)
def criar_lista(email_usuario):
    nomeLista = input("Digite o nome da nova lista que deseja criar: ").strip()

    with open('nomeLista.txt', 'a') as lista:
        lista.write(f"{email_usuario}\t{nomeLista}\n")

    print(f"Lista '{nomeLista}' criada com sucesso!")

def editar_lista_nome(email_usuario):
    listas_criadas=[]
    try:
        with open('nomeLista.txt') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes) == 2 and partes[0] == email_usuario:
                    listas_criadas.append(partes[1])
    except FileNotFoundError:
        print("Não há listas!")
        return
    
    if not listas_criadas:
        print("Lista não encontrada")
        return
    
    print("---TODAS AS SUAS LISTAS---")
    for i, nome in enumerate(listas_criadas, 1):
        print(f"{i} - {nome}")

    opcaoUsuarioEditar = int(input("\nSelecione o número da lista que deseja editar para renomear: "))
    nomeAntigoLista = listas_criadas[opcaoUsuarioEditar-1]
    nomeNovoLista = input(f"Digite o nome novo para a lista: '{nomeAntigoLista}': ")

    # A parte abaixo vai atualizar o nomeLista.txt, o arquivo que só tem o nome da lista e o email do usuário
    linhas_mudar = []
    with open('nomeLista.txt') as lista:
        for linha in lista:
            if linha.strip() == f"{email_usuario}\t{nomeAntigoLista}":
                linhas_mudar.append(f"{email_usuario}\t{nomeNovoLista}\n")
            else:
                linhas_mudar.append(linha)

    with open('nomeLista.txt', 'w') as linha:
        linha.writelines(linhas_mudar)

    # A parte abaixo vai atualizar o detalheFavoritos.txt, o arquivo tem o email usuário, nome lista e nome dos vídeos adicionados
    linhas_detalhe_arquivo = []
    try:
        with open('detalheFavoritos.txt') as listaf:
            for linha in listaf:
                partes = linha.strip().split('\t')
                if len(partes) == 3:
                    email, lista, video = partes
                    if email == email_usuario and lista == nomeAntigoLista:
                        linhas_detalhe_arquivo.append(f"{email}\t{nomeNovoLista}\t{video}\n")
                    else:
                        linhas_detalhe_arquivo.append(linha)

        with open('detalheFavoritos.txt', 'w') as lista:
            lista.writelines(linhas_detalhe_arquivo)

    except FileNotFoundError:
        print("Não há vídeos")
        pass

    print(f"Nome lista alterada com sucesso! A lista: '{nomeAntigoLista}' agora se chama: '{nomeNovoLista}'!")


def visualizar_lista(email_usuario):
    listasUsuario = []
    try:
        with open('nomeLista.txt') as lista:
            for linha in lista:
                email, nomeLista = linha.strip().split('\t')
                if email == email_usuario:
                    listasUsuario.append(nomeLista)

        if not listasUsuario:
            print("Você não tem nenhuma lista criada!")
    
        print("--> Listas disponíveis: ")
        for i, lista in enumerate(listasUsuario, 1):
            print(f"{i} - {lista}")

        if lista:
            visualizar_detalhe_favoritos()
        else:
            print("Não há lista")
        
    except FileNotFoundError:
        print("Não há arquivo (você ainda não criou nenhuma lista)")

# Assim que o usuário fizer a busca do vídeo, ele pode adicionar aos favoritos de qualquer 'pasta' que criou
def adicionar_favoritos(email_usuario, nome_video):
    listasUsuario = []
    with open('nomeLista.txt') as lista:
        for linha in lista:
            email, nomeLista = linha.strip().split('\t')
            if email == email_usuario:
                listasUsuario.append(nomeLista)

    if not listasUsuario:
        print("Você não tem nenhuma lista criada!")
    
    print("--> Listas disponíveis: ")
    for i, lista in enumerate(listasUsuario, 1):
        print(f"{i} - {lista}")

    try:
        opcaoUsuarioLista = int(input(f"\nDigite o número da lista que deseja adicionar o vídeo '{nome_video}': "))
        if opcaoUsuarioLista == lista:
            listaEscolha = listasUsuario[opcaoUsuarioLista-1]

            with open('detalheFavoritos.txt', 'a') as favoritos:
                favoritos.write(f"{email_usuario}\t{listaEscolha}\t{nome_video}\n")

            print(f"O vídeo '{nome_video}' foi adicionado a lista '{listaEscolha}' com sucesso!")
        else:
            print("Você não possui listas!")
    except ValueError:
        print("Você digitou algo inválido")

def visualizar_detalhe_favoritos():
    while True:
        print("\n=== Obter detalhes dos favoritos ===")
        print("1 - Obter detalhes dos favoritos que foram criados")
        print("Sair [aperte s]")
        opcaoUsuarioDetalheFavoritos = input("O que você deseja fazer?: ")
        if opcaoUsuarioDetalheFavoritos == 's' or opcaoUsuarioDetalheFavoritos == "S":
            break
        elif opcaoUsuarioDetalheFavoritos == '1':
            print("\n \n Navegação: Login >> Menu >> Gerenciar favoritos >> Visualizar lista reprodução já criados >> Obter detalhes dos favoritos que foram criados")
            print("=== VISUALIZAR DETALHES FAVORITOS SALVOS ===")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:  # garante que não é None
                visualizar_e_selecionarFavoritos(usuario_logado["email"])
        else:
            print("Ocorreu um erro, o tipo de caractere que você digitou não faz parte do que foi solicitado")

def visualizar_e_selecionarFavoritos(email_usuario):
    listasUsuario = []
    with open('nomeLista.txt') as lista:
        for linha in lista:
            email, nomeLista = linha.strip().split('\t')
            if email == email_usuario:
                listasUsuario.append(nomeLista)

    if not listasUsuario:
        print("Você não tem nenhuma lista criada!")
    
    print("--> Listas disponíveis: ")
    for i, lista in enumerate(listasUsuario, 1):
        print(f"{i} - {lista}")

    try:
        opcaoUsuarioLista = int(input("\nSelecione a lista que deseja visualizar: "))
    
        if opcaoUsuarioLista >= 1: #Precisa ser maior ou igual a 1 que o usuário digitou
            if opcaoUsuarioLista <= len(listasUsuario): #Verifica se o número não é grande demais

                indice = opcaoUsuarioLista-1
                listaEscolha = listasUsuario[indice]
                print(f"Você escolheu a lista: {listaEscolha}")

                encontrarItens = False
            
                try: # o try é usado em chances que podem dar erro e o programa fechar sozinho, mas se der for usado irá aparecer uma mensagem no except e não fecha o programa. É como se fosse um if
                    with open('detalheFavoritos.txt') as favoritos:
                        for linha in favoritos:
                            parte_favoritos = linha.strip().split('\t')

                            if len(parte_favoritos) == 3:
                                email_pasta_fav, lista_pasta_fav, item_pasta_fav = parte_favoritos

                                if email_pasta_fav == email_usuario and lista_pasta_fav == listaEscolha:
                                    print(item_pasta_fav)
                                    encontrarItens = True

                    if not encontrarItens:
                        print("Lista vazia")
                except FileNotFoundError:
                    print("Você ainda não adicionou nenhum item na lista de favoritos")
            else:
                print("Número alto demais")
        else:
            print("Número baixo demais")
    except ValueError:
        print("Você digitou algo inválido!")


def excluir_favorito(email_usuario, video_selecionado):
    listaEncontrar = []

    try:
        with open('detalheFavoritos.txt') as favoritos:
            for linha in favoritos:
                partes = linha.strip().split('\t')
                if len(partes) == 3:
                    email, lista, video = partes

                    if email == email_usuario and video == video_selecionado:
                        listaEncontrar.append(lista)
    except FileNotFoundError:
        print("Não encontrado")
        return

    if not listaEncontrar:
        print(f"{video_selecionado} não foi encontrado")
        return
    
    print(f"O vídeo {video_selecionado} foi encontrado nas listas: ")
    for i, lista in enumerate(listaEncontrar, 1):
        print(f"{i} - {lista}")

    opcaoExcluir = int(input("Digite o número da lista que deseja excluir: "))
    listaEscolha = listaEncontrar[opcaoExcluir-1]

    #Agora vai reescrever o arquivo, mas sem a linha que precisa exluir
    manter = []
    excluir = False

    with open('detalheFavoritos.txt') as excluirFavoritos:
        linhas = excluirFavoritos.readlines()

    for linha in linhas:
        partes = linha.strip().split('\t')
        if len(partes) == 3:
            #Exclui as 3 linhas que baterem exatamente
            email, lista, video = partes
            if email == email_usuario and lista == listaEscolha and video == video_selecionado:
                excluir = True
                continue

            manter.append(linha)
    if excluir:
        with open('detalheFavoritos.txt', 'w') as escrita:
            escrita.writelines(manter)
        print(f"\n{video_selecionado} foi removido da lista: {listaEscolha}")

def remover_lista(email_usuario):
    todas_listas = []
    try:
        with open('nomeLista.txt') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes) == 2 and partes[0] == email_usuario:
                    todas_listas.append(partes[1])
    except FileNotFoundError:
        print("Não há listas para excluir")
        return
    
    if not todas_listas:
        print("Nenhuma lista foi encontrada")
        return
    
    print("\nQual das listas abaixo você deseja excluir permanentemente?")
    for i, nome in enumerate(todas_listas, 1):
        print(f"{i} - {nome}")

    try:
        opcaoUsuarioExcluir = int(input("\nDigite o número da lista que deseja excluir: "))
        nome_deletar = todas_listas[opcaoUsuarioExcluir-1]
    except (ValueError, IndexError):
            print("Opção inválida")
            return

    confirmar = input(f"Você tem certeza que deseja excluir a lista: '{nome_deletar}'? e TODOS os vídeos dela? [digite s]-> para excluir [digite n]->Para não excluir: ")
    if confirmar.lower() != 's':
            print("Deletar foi cancelado")
            return
        
    #Remover do 'nomeListas.txt'
    linhas_restantes = []
    with open('nomeLista.txt') as lista:
        for linha in lista:
            if linha.strip() != f"{email_usuario}\t{nome_deletar}":
                linhas_restantes.append(linha)

    with open('nomeLista.txt', 'w') as lista:
        lista.writelines(linhas_restantes)

    #Remover do 'detalheFavoritos.txt'
    linhas_restantes_detalhe = []
    try:
        with open('detalheFavoritos.txt') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes) == 3:
                    email, lista, video = partes
                    if email==email_usuario and lista == nome_deletar:
                        continue

                linhas_restantes_detalhe.append(linha)
        with open('detalheFavoritos.txt', 'w') as lista:
            lista.writelines(linhas_restantes_detalhe)
    except FileNotFoundError:
        print("Não há listas")
        pass

    print(f"\nA lista '{nome_deletar}' e todos os vídeos dentro dela foram excluídos com sucesso!")

# Parte adm função
def menu_principal_adm():
    while True:
        print("\n \n Navegação: Login do administrador >> Menu")
        print("==== MENU ====")
        print("---Livro---")
        print("1- Cadastrar vídeo")
        print("2- Excluir vídeo")
        print("---Usuário---")
        print("3- Consultar usuário")
        print("4- Consultar estatísticas")
        print("5- Sair")
        print("\n")
        opcaoAdm = input("O que você deseja fazer? ")

        if opcaoAdm == "1":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Cadastrar vídeo")
            cadastrar_video()
        
        elif opcaoAdm == "2":
            print("\n Navegação: Login do administrador >> Menu >> Excluir vídeo")
            excluir_video()

        elif opcaoAdm == "3":
            consultar_usuarios()

        elif opcaoAdm == "4":
            consulta_estatistica()

        elif opcaoAdm == "5":
            break

def cadastrar_video():
    print("\n Navegação: Login do administrador >> Menu >> Consultar vídeos")
    print("--- CADASTRAR NOVO VÍDEO ---")
    print("Obs: utilize '\\n' para pular linha na sinopse")
    titulo = input("Título: ").strip()
    sinopse = input("Sinopse: ").strip()
    duracao = input("Duração do vídeo: ").strip()
    genero = input("Gênero: ").strip()
    autor = input("Autor: ").strip()

    with open('videos.txt', 'a', encoding='utf-8') as lista:
        lista.write(f"{titulo}\t{sinopse}\t{duracao}\t{genero}\t{autor}\n")
    print(f"\nVídeo '{titulo}' cadastrado com sucesso!")

def excluir_video():
    todosVideos = []
    try:
        with open('videos.txt', encoding='utf-8') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes)>=1:
                    todosVideos.append(partes[0])
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return
    if not todosVideos:
        print("Não há vídeos para excluir")
        return
    
    print("--- EXCLUSÃO DE VÍDEO ---")
    for i,titulo in enumerate(todosVideos, 1):
        print(f"{i} - {titulo}")

    try:
        escolhaAdmExcluir = int(input("Digite o número do vídeo que deseja excluir: "))
        videoApagar = todosVideos[escolhaAdmExcluir-1]
    except (ValueError, IndexError):
        print("É inválido")
        return
    
    confirmarEscolha = input(f"Essa ação irá REMOVER o vídeo: '{videoApagar}' do sistema. Você deseja mesmo excluir? [digite s]-> para excluir [digite n]->Para não excluir: ")
    if confirmarEscolha.lower() != 's':
        print("A ação remover foi cancelada!")
        return
    # Remover vídeo do arquivo 'videos.txt'
    armazenar_video = []
    with open('videos.txt', encoding='utf-8') as lista:
        for linha in lista:
            if not linha.strip().startswith(videoApagar + "\t"):
                armazenar_video.append(linha)

    with open('videos.txt', 'w', encoding='utf-8') as lista:
        lista.writelines(armazenar_video)

    # Remover o vídeo do arquivo 'detalheFavoritos'
    armazenar_favoritos = []
    try:
        with open('detalheFavoritos.txt', encoding='utf-8') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes) ==3 and partes[2] != videoApagar:
                    armazenar_favoritos.append(linha)
                elif len(partes) !=3:
                    armazenar_favoritos.append(linha)
        with open('detalheFavoritos.txt', 'w', encoding='utf-8') as lista:
            lista.writelines(armazenar_favoritos)
    except FileNotFoundError:
        print("Não há favoritos!")
        pass

    print(f"O vídeo: '{videoApagar}' foi excluído do sistema!")

def consultar_usuarios():
    while True: 
        print("\n Navegação: Login do administrador >> Menu >> Consultar usuário")
        print("--Consultar usuário--")
        print("1- Consultar um usuário especifíco")
        print("2- Consultar lista de todos os usuários")
        print("3- Sair")
        try:
            opcaoConsultarUsu = int(input("O que você deseja fazer?: "))

            if opcaoConsultarUsu == 3:
                break
            elif opcaoConsultarUsu == 2:
                todos_usuarios()
            elif opcaoConsultarUsu == 1:
                especifico_usuario()

        except ValueError:
            print("Opção inválida")

def todos_usuarios():
    print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Lista de todos os usuários")
    print("--Lista de todos os usuários--")
    try:
        with open('cadastroUsuarios.txt') as usuarios:
            listaTodosUsuarios = [linha.split() for linha in usuarios]
            print(listaTodosUsuarios)
    except FileNotFoundError:
        print("Não há arquivo (ainda não há nenhum usuário cadastrado)")

def especifico_usuario():
    print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Lista de um usuário específico")
    try:
        with open('cadastroUsuarios.txt') as usuarios:
            listaTodosUsuarios = [linha.split() for linha in usuarios]
        while True:
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Procurar usuário em específico")
            print("--Procurar usuário em específico--")
            print("1- Pesquisar por nome do usuário")
            print("2- Pesquisar por email do usuário")
            print("3- Sair")

            try:
                opcaoConsultarEspecifico = int(input("O que você deseja fazer: "))

                if opcaoConsultarEspecifico == 1:
                    buscaNome = input("Digite sua busca: ").strip()
                    for usuario in listaTodosUsuarios:
                        nome = usuario[0]

                        if nome == buscaNome:
                            print(f"O usuário: '{buscaNome}' foi encontrado na lista --> {usuario}")
                            break
            
                    else:
                        print("Usuário não encontrado!")

                elif opcaoConsultarEspecifico == 2:
                    buscaEmail = input("Digite sua busca: ").strip()
                    for usuario in listaTodosUsuarios:
                        email = usuario[1]

                        if email == buscaEmail:
                            print(f"O email: '{buscaEmail}' foi encontrado na lista --> {usuario}")
                            break

                    else:
                        print("Email não encontrado!")

                elif opcaoConsultarEspecifico == 3:
                    break
            except ValueError:
                print("Opção inválida")
    except FileNotFoundError:
        print("Não há arquivo (ainda não há nenhum usuário cadastrado)")

def consulta_estatistica():

    while True:
        print("-"*20)
        print("\n\n\n\n\n\n\n Navegação: Login do administrador >> Menu >> Consultar estatísticas")
        print("\n\n--Estatísticas--")
        print("1-Total de usuários")
        print("2-Total de livros")
        print("3-Curtidas de um livro específico")
        print("4-Livros populares")
        print("5-Informações dos livros")
        print("6-Top 5 livros mais curtidos")
        print("7-Sair")
    
        opcao=input("\nEscolha a sua opção administrador:")
    
    # Código para mostrar total de usuários
        if opcao == "1":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Consultar estatísticas >> Total de usuários")
            total_usuarios()
        
        elif opcao == "2":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Consultar estatísticas >> Total de livros")
            total_livros()
        
        elif opcao == "3":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Consultar estatísticas >> Curtidas de um livro específico")
            print("\n --- Visualizar curtidas de um livro específico: ---")
            ver_curtidas()
        
        elif opcao == "4":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Consultar estatísticas >> Livros populares")
            print("\n--- Visualizar livros populares: ---")
            visualizar_populares()
        
        elif opcao == "5":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Consultar estatísticas >> Informações dos livros")
            pesquisaAdm()

        elif opcao == "6":
            print("\n Navegação: Login do administrador >> Menu >> Consultar usuário >> Consultar estatísticas >> Top 5 livros mais curtidos")
            print("\n--- Visualizar top 5 livros mais curtidos: ---")
            top_cinco()
        
        elif opcao == "7":
            print("Saindo do sistema de estatísticas...")
            break

def total_usuarios():
    print("\n--- TOTAL USUÁRIOS ---")
    try:
        with open('cadastroUsuarios.txt') as lista:
            # lista.readlines() cria uma lista com todas as linhas
            totalUsu= len(lista.readlines())
            print(f"Total de usuários cadastrados no sistema: {totalUsu}")
    except FileNotFoundError:
        print("Não há arquivo de usuários")

def total_livros():
    print("\n---TOTAL LIVROS ---")
    try:
        with open('videos.txt', encoding='utf-8') as lista:
            # lista.readlines() cria uma lista com todas as linhas
            totalLivro= len(lista.readlines())
            print(f"Total de livros cadastrados no sistema: {totalLivro}")
    except FileNotFoundError:
        print("Não há arquivo de livros registrados")

def ver_curtidas():
    todos_livros = []
    try:
        with open('videos.txt', encoding='utf-8') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes)>=1:
                    todos_livros.append(partes[0])
    except FileNotFoundError:
        print("Vídeos não encontrados")
        return
    
    if not todos_livros:
        print("Não há livros cadastrados")
        return
    print("\n--- QUAL LIVRO DESEJA VER CURTIDAS ---")
    for i, titulo in enumerate(todos_livros, 1):
        print(f"{i} - {titulo}")
    
    escolhaAdmLivro = input("Digite o nome ou o número do vídeo: ").strip().lower()
    livroSelecionado = None

    if escolhaAdmLivro.isdigit():
        indice = int(escolhaAdmLivro)-1
        if 0 <= indice <len(todos_livros):
            livroSelecionado = todos_livros[indice]
    
    if not livroSelecionado:
        for livro in todos_livros:
            if escolhaAdmLivro == livro.lower():
                livroSelecionado = livro
                break
    
    if livroSelecionado:
        contador = 0
        try:
            with open('curtidaLivros.txt') as lista:
                for linha in lista:
                    partes = linha.strip().split('\t')
                    if len(partes)==2:
                        nomeLivroArquivo = partes[1].strip()
                        if nomeLivroArquivo.lower()==livroSelecionado.lower():
                            contador+=1
            print("\n"+'='*10)
            print(f"Livro selecionado: '{livroSelecionado.upper()}'")
            print(f"Total de curtidas: {contador}")
            print("="*10)
        except FileNotFoundError:
            print(f"\nO livro selecionado: '{livroSelecionado.upper()}' não possui curtidas")
    else:
        print("Opção inválida")

def visualizar_populares():
    contagem_todos_curtidos = {}
    try:
        with open('curtidaLivros.txt') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes) ==2:
                    # Pegar o nome do vídeo
                    video = partes[1]

                    if video in contagem_todos_curtidos:
                        contagem_todos_curtidos[video] +=1
                    else:
                        contagem_todos_curtidos[video]=1
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return
    if not contagem_todos_curtidos:
        print("Não há favoritos no sistema")

    #Ordenar votos
    ranking = sorted(contagem_todos_curtidos.items(), key=lambda item: item[1], reverse=True)
    print("\nOs 3 vídeos mais populares!!")
    print("="*10)
    for i, (video, favoritos) in enumerate(ranking[:3],1):
        if i==1:
            medalha = "🥇 "
        elif i==2:
            medalha = "🥈 "
        elif i==3:
            medalha = "🥉 "
        print(f"{medalha}{i}° Lugar: {video}")
    print("="*10)

def pesquisaAdm():
    livros_armazenados = []
    try:
        with open('videos.txt', encoding='utf-8') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes)>=1:
                    livros_armazenados.append(partes[0].lower())
    except FileNotFoundError:
        print("O arquivo não foi encontrado")

            #Mostrar opções
    if livros_armazenados:
        print("=== Todos os vídeos disponíveis ===")
        for i, nome in enumerate(livros_armazenados, 1):
            print(f"{i} - {nome}")
        print("-----------------------------------------")

            #Pedir para o usuário buscar vídeo
        busca = input("\nDigite o nome ou o número do vídeo acima: ").strip().lower()
            #Verificar se o usuário digitou o nome ou número
        videoEncontrado = None

            #Se digitou o número
        if busca.isdigit(): #is digit() é uma função de string usada para verificar se todos os caracteres em uma string são dígitos numéricos (0-9).
            indice = int(busca)-1
            if 0<=indice<len(livros_armazenados):
                videoEncontrado = livros_armazenados[indice]
            
            #Verificar se o texto existe
        if not videoEncontrado:
            for livro in livros_armazenados:
                if busca == livro.lower():
                    videoEncontrado = livro
                    break
        if videoEncontrado:
            print("Encontrado!")
            info_livroAdm(videoEncontrado)
        else:
            print("Não encontrado!")
    else:
        print("Não há vídeos cadastrados")


def info_livroAdm(nome_video):
    while True:
        print("------------------------------------------------------------------------------")
        print(f"\n==== OBTER INFORMAÇÕES DO VÍDEO {nome_video} ===")
        print("Continuar para visualizar as informações do vídeo [digite c]")
        print("Sair [digite s]")
        print("\n")
        acaoUsuarioInfo = input("O que você deseja fazer? ")
        if acaoUsuarioInfo=='c' or acaoUsuarioInfo=="C": #É necessário você tranformar isso em DOCUMENTO ou DICIONÁRIO
            print("Visualizando Sinopse, Autor, Duração e Gênero do vídeo:\n")
            try:
                with open('videos.txt', encoding='utf-8') as lista:
                    for linha in lista:
                        partes = linha.strip().split('\t')

                        if len(partes)==5:
                            titulo, sinopse, duracao, genero, autor = partes

                            if titulo.lower() == nome_video:
                                formatarSinopse = sinopse.replace("\\n", "\n")
                                print("\n"+"="*10)
                                print(f"TÍTULO: {titulo.upper()}")
                                print("-"*10)
                                print(f"SINOPSE: {formatarSinopse}")
                                print(f"DURAÇÃO: {duracao}")
                                print(f"GÊNERO: {genero}")
                                print(f"AUTOR: {autor}")
                                print("="*10)
                                break
            except FileNotFoundError:
                print("O arquivo não existe")

        elif acaoUsuarioInfo=='s' or acaoUsuarioInfo=='S':
            break

def top_cinco():
    contagem_todos_curtidos = {}
    try:
        with open('curtidaLivros.txt') as lista:
            for linha in lista:
                partes = linha.strip().split('\t')
                if len(partes) ==2:
                    # Pegar o nome do vídeo
                    video = partes[1]

                    if video in contagem_todos_curtidos:
                        contagem_todos_curtidos[video] +=1
                    else:
                        contagem_todos_curtidos[video]=1
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return
    if not contagem_todos_curtidos:
        print("Não há favoritos no sistema")

    #Ordenar votos
    ranking = sorted(contagem_todos_curtidos.items(), key=lambda item: item[1], reverse=True)
    print("\nOs 5 vídeos mais votados!!")
    print("="*10)
    for i, (video, favoritos) in enumerate(ranking[:5],1):
        if i==1:
            medalha = "🥇 "
        elif i==2:
            medalha = "🥈 "
        elif i==3:
            medalha = "🥉 "
        else:
            medalha = ""
        print(f"{medalha}{i}° Lugar: {video}")
        print(f"  Total de {favoritos} favoritados no sistema")
    print("="*10)

def logo():
    logo = r'''
    _____  _____ ___    _______      __
    |  ___| ____|_ _|   |_   _\ \   / /
    | |_  |  _|  | |      | |  \ \ / / 
    |  _| | |___ | |      | |   \ V /  
    |_|   |_____|___|     |_|    \_/
    '''
    
    print(logo)

# Informações iniciais para o usuário (Essa é a primeira coisa que o usuário visualiza)
print("====Seja bem-vindo!====")
logo()
print("Já possui uma conta ou deseja criar uma?")
print("//Digite [a] para entrar em conta corporativa// -> Acesso apenas para funcionários")
possuiConta = str(input("Digite [s] se já possui conta usuário ou digite [n] se não possue conta usuário: "))

#Se o usuário possui a conta
if possuiConta == "s" or possuiConta=="S":
    print("\n")
    print("====Login usuário====")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    if login_usuario(email, senha):
        menu_principal()
    else:
        print("Usuário não encontrado")
    print("------------------------------------------------------------------------------")
    print("\n")

#Se o usuário não possui uma conta
elif possuiConta == "n" or possuiConta=="N":
    cadastrar_usuario()
    print("------------------------------------------------------------------------------")


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
        if adm=='adm' and email=='adm' and senha=='adm':
            print("Acesso com sucesso. Bem-vindo,administrador!")
            menu_principal_adm()
        else:
            print("Login inválido")
    else:
        print("\n")
        print("Ocorreu um erro, o tipo de caractere que você digitou não faz parte do que foi solicitado")

    
else:
    print("\n")
    print("Ocorreu um erro, o tipo de caractere que você digitou não faz parte do que foi solicitado")

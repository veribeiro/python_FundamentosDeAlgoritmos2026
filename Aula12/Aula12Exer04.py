# Crie uma agenda de telefones que salva os dados de maneira permanente.
# A agenda deve funcionar em loop infinito, até que o usuário
# decida sair. Os dados armazenados são: nome, sobrenome, telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1 - Novo contato (create)
# ▶ 2 - Procura (pelo nome) (read)
# ▶ 3 - Atualiza contato (update)
# ▶ 4 - Apaga contato (delete)
# ▶ 0 - Sair

import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO_AGENDA = "agenda.txt"

def carregar_contatos():
    """Lê o arquivo e transforma em um dicionário."""
    contatos = {}
    if os.path.exists(ARQUIVO_AGENDA):
        with open(ARQUIVO_AGENDA, "r") as f:
            for linha in f:
                # Divide a linha pelos separadores ';'
                nome, sobrenome, tel, email = linha.strip().split(";")
                contatos[nome.lower()] = {
                    "nome": nome, "sobrenome": sobrenome, 
                    "telefone": tel, "email": email
                }
    return contatos

def salvar_contatos(contatos):
    """Pega o dicionário e grava no arquivo texto."""
    with open(ARQUIVO_AGENDA, "w") as f:
        for c in contatos.values():
            f.write(f"{c['nome']};{c['sobrenome']};{c['telefone']};{c['email']}\n")

# --- Programa Principal ---
contatos = carregar_contatos()

while True:
    print("\n--- AGENDA TELEFÔNICA ---")
    print("1 - Novo contato (Create)")
    print("2 - Procura (Read)")
    print("3 - Atualiza contato (Update)")
    print("4 - Apaga contato (Delete)")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        tel = input("Telefone: ")
        email = input("E-mail: ")
        # Salva no dicionário usando o nome em minúsculo como chave
        contatos[nome.lower()] = {
            "nome": nome, "sobrenome": sobrenome, "telefone": tel, "email": email
        }
        salvar_contatos(contatos)
        print("Contato salvo!")

    elif opcao == "2":
        busca = input("Digite o nome para procurar: ").lower()
        if busca in contatos:
            c = contatos[busca]
            print(f"\nEncontrado: {c['nome']} {c['sobrenome']} | Tel: {c['telefone']} | E-mail: {c['email']}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        busca = input("Nome do contato para atualizar: ").lower()
        if busca in contatos:
            print("Deixe em branco para manter o valor atual.")
            tel = input(f"Novo Telefone ({contatos[busca]['telefone']}): ") or contatos[busca]['telefone']
            email = input(f"Novo E-mail ({contatos[busca]['email']}): ") or contatos[busca]['email']
            
            contatos[busca]['telefone'] = tel
            contatos[busca]['email'] = email
            salvar_contatos(contatos)
            print("Dados atualizados!")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        busca = input("Nome do contato para apagar: ").lower()
        if busca in contatos:
            del contatos[busca]
            salvar_contatos(contatos)
            print("Contato removido com sucesso.")
        else:
            print("Contato não existe.")

    elif opcao == "0":
        print("Saindo e salvando dados...")
        break
    else:
        print("Opção inválida!")
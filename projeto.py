usuarios = {}
jogos = {}
 
def criar_usuario(nome):

    #Cria um novo usuário se ele ainda não existir.

    if nome in usuarios:
        print("Usuário já existe!")

    else:
        while True:
            email = input("Digite seu e-mail: ")
            if email in usuarios: 
                print("Email já em uso! Tente novamente.")
            else:
                break
            
        senha = input("Digite sua senha: ")

        usuarios[nome] = {
            "email": email,
            "senha": senha,
            "jogos": {},
            "preferencias": [],
            "saldo": 0.0,
            "itens": {},
            "mensagens": [],
            "pontuacoes": {},
            "conquistas": {} 
        }

        print("\nUsuario criado com sucesso!")

def compra_item(nome):

    while True:
        game = input("\nQual o nome do jogo que deseja comprar algo nele?\n")
        if game not in jogos:
            print("Este jogo não existe no catalogo")
            print("\nDigite o que gostaria de fazer agora:")
            print("\n1 - Tentar achar outro jogo")
            print("2- Retornar ao menu anterior")

            opcao = input()

            if opcao == "2":
                break

        if game not in usuarios[nome]["jogos"]:
            print("\nVocê não possui este jogo na conta.")
            continue

        # Verifica se o jogo possui uma loja de itens

        if "loja" not in jogos[game] or not jogos[game]["loja"]:
            print("\nEste jogo não possui itens à venda.")
            continue

        print("\nItens disponíveis para compra:")
        for item, preco in jogos[game]["loja"].items():
            print("- " + item + ": R$" + str(preco))

        item_desejado = input("\nDigite o nome do item que deseja comprar: ")

        # Verifica se o item está disponível

        if item_desejado not in jogos[game]["loja"]:
            print("\nItem não encontrado na loja do jogo.")
            continue

        preco_item = jogos[game]["loja"][item_desejado]

        # Verifica se o usuário tem saldo suficiente

        if usuarios[nome]["saldo"] < preco_item:
            print("\nSaldo insuficiente para comprar " + item_desejado + ".")
            break

        # Realiza a compra

        usuarios[nome]["saldo"] -= preco_item
        if item_desejado not in usuarios[nome]["itens"]:
            usuarios[nome]["itens"][item_desejado] = 0
        usuarios[nome]["itens"][item_desejado] += 1

        print("\nCompra realizada com sucesso! " + item_desejado + " foi adicionado ao seu inventário.")

def adicionar_saldo(nome):

    #Adiciona saldo à conta do usuário.
    
    saldo_adicionado = float(input("\nQuanto deseja adicionar de saldo à conta de "+nome+"?\n"))

    if saldo_adicionado < 0:
        print("\nO valor deve ser positivo!")
        return

    # Soma o saldo atual com o novo

    usuarios[nome]["saldo"] += saldo_adicionado

    print(f"\nSaldo adicionado com sucesso! Saldo atual: R${usuarios[nome]['saldo']:.2f}")

def postar_no_forum(nome_jogo, usuario, mensagem):

    if nome_jogo not in jogos:
        print("\nJogo "+nome_jogo+" não encontrado!")
        return

    jogos[nome_jogo]["forum"].append(usuario + ": " + mensagem) 
    print("\nMensagem postada no fórum de "+nome_jogo+"!")

def ver_forum(nome_jogo):

    if nome_jogo not in jogos:
        print("\nJogo não encontrado!\n")
        return

    print("\n--- Fórum do jogo "+nome_jogo+" ---")

    if not jogos[nome_jogo]["forum"]:
        print("Nenhuma mensagem no fórum ainda.")
    else:
        for post in jogos[nome_jogo]["forum"]:
            print(post)

def enviar_mensagem(remetente, destinatario, mensagem):

    if destinatario not in usuarios:
        print("\nUsuário não encontrado!")
        return
    
    usuarios[destinatario]["mensagens"].append(f"{remetente}: {mensagem}")
    print("\nMensagem enviada para "+destinatario+"!")

def ver_mensagens(nome):

    if not usuarios[nome]["mensagens"]:
        print("\nNenhuma mensagem recebida.")
    else:
        print("\n--- Mensagens Privadas ---")
        for msg in usuarios[nome]["mensagens"]:
            print(msg)

def chatsforuns(nome, nome_jogo):

    print("\nO que deseja fazer?\n")
    print("1 - Comentar em um forum")
    print("2 - visualizar um forum")
    print("3 - Enviar uma mensagem para um usuario")
    print("4 - Ver mensagem de um usuario")
    print("5 - Retornar ao menu anterior\n")


    opcao = input()

    if opcao == "1":
        mensagem = input("Qual mensagem deseja enviar?")
        postar_no_forum(nome_jogo, nome, mensagem)

    elif opcao == "2":
        ver_forum(nome_jogo)
    
    elif opcao == "3":
        mensagem = input("Digite a mensagem que você quer enviar: ")
        destinatario = input("\nPara quem quer enviar? ")
        enviar_mensagem(nome,destinatario, mensagem )

    elif opcao == "4":
        ver_mensagens(nome)


    else:
        return

def atualizar_jogo_usuario(nome, nome_jogo):
        
    if nome not in usuarios:
        print("\nUsuário "+nome+" não encontrado!")
        return

    if nome_jogo not in usuarios[nome]["jogos"]:
        print("\nVocê não possui "+nome_jogo+" na biblioteca!")
        return

    versao_atual = usuarios[nome]["jogos"][nome_jogo]
    versao_nova = jogos[nome_jogo]["versao"]

    if versao_atual == versao_nova:
        print("\nSeu jogo já está atualizado para a versão "+versao_nova+"!")

    else:
        usuarios[nome]["jogos"][nome_jogo] = versao_nova
        print("\n"+nome_jogo+" atualizado para a versão "+versao_nova+"!")

def abrir_suporte(nome):

    #O usuário pode abrir uma solicitação de suporte.

    problema = input("\nDescreva seu problema: ")

    if "suporte" not in usuarios[nome]:
        usuarios[nome]["suporte"] = []  # Cria a lista se ainda não existir
    
    usuarios[nome]["suporte"].append({"descricao": problema, "status": "Aberto"})
    print("\nSolicitação enviada com sucesso!")


def ver_suporte(nome):

    #O usuário pode ver suas solicitações de suporte.

    if "suporte" not in usuarios[nome] or not usuarios[nome]["suporte"]:
        print("\nNenhuma solicitação aberta.")
        return
    
    print("\nSuas solicitações de suporte:")

    for i, suporte in enumerate(usuarios[nome]["suporte"]):
        print(f"{i+1}. {suporte['descricao']} - {suporte['status']}")


def resolver_suporte(nome):

    """O usuário pode marcar um suporte como resolvido."""
    ver_suporte(nome)
    
    escolha = input("\nDigite o número da solicitação resolvida (ou pressione Enter para voltar): ")
    
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(usuarios[nome]["suporte"]):
            usuarios[nome]["suporte"][indice]["status"] = "Resolvido"
            print("\nSolicitação marcada como resolvida!")
        else:
            print("\nNúmero inválido!")


def suporte(nome):

    #Menu de suporte ao usuário.

    while True:
        print("\nSuporte ao Usuário")
        print("1 - Abrir uma solicitação")
        print("2 - Ver minhas solicitações")
        print("3 - Marcar como resolvido")
        print("4 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            abrir_suporte(nome)
        elif opcao == "2":
            ver_suporte(nome)
        elif opcao == "3":
            resolver_suporte(nome)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

def controle_pais(responsavel, nome):

    #Define restrições de controle parental para um usuário após verificar as senhas.
    
    if nome not in usuarios:
        print("\nUsuário não encontrado!")
        return
    
    if responsavel not in usuarios:
        print("\nA conta do responsável não foi encontrada!")
        return
    
    # Verificar senha do responsável

    senha_responsavel = input(f"\n{responsavel}, digite sua senha para confirmar a alteração: ")
    if senha_responsavel != usuarios[responsavel]["senha"]:
        print("\nSenha incorreta! Ação cancelada.")
        return

    # Verificar senha do usuário
    senha_usuario = input(f"Digite a senha da conta \n{nome}, dpara confirmar a alteração: ")
    if senha_usuario != usuarios[nome]["senha"]:
        print("\nSenha incorreta! Ação cancelada.")
        return
    
    # Se ambas as senhas estiverem corretas, definir as restrições
    usuarios[nome]["responsavel"] = responsavel
    print(f"\nResponsável '{responsavel}' vinculado à conta de {nome}.")

    restricoes = {}
    restricoes["bloquear_compras"] = input("Bloquear compras? (s/n): ").lower() == "s"
    restricoes["bloquear_jogos"] = input("Deseja restringir jogos específicos? (s/n): ").lower() == "s"

    if restricoes["bloquear_jogos"]:
        restricoes["jogos_bloqueados"] = input("Digite os nomes dos jogos bloqueados separados por vírgula: ").split(",")

    usuarios[nome]["restricoes"] = restricoes
    print("\nConfigurações de controle parental salvas com sucesso!")

def gerenciar_perfil(nome):

    #Gerencia o perfil de um usuário existente.
    if nome not in usuarios:
        print("Usuário não encontrado!")
        return

    while True:
        senha = input("Digite a senha do usuário para acessar o perfil: ")

        if senha == usuarios[nome]["senha"]:
            print("Acesso permitido!\n")
            break
        else:
            print("\nSenha incorreta, o que deseja fazer agora?\n")
            print("1 - Tentar novamente")
            print("2 - Voltar ao menu anterior\n")
            
            opcao = input("Escolha uma opção: ")

            if opcao == "2":
                print("Voltando ao menu principal...")
                return 

    while True:
        print("\nGerenciamento de Perfil - " + nome+ "\n")
        print("1 - Mudar a senha do perfil")
        print("2 - Adicionar um jogo à conta")
        print("3 - Remover um jogo da conta")
        print("4 - Atualizar preferências da conta")
        print("5 - Visualizar informações da conta")
        print("6 - Comprar item")
        print("7 - Adicionar saldo a conta")
        print("8 - Chats/fóruns")
        print("9 - Atualizar jogo (usuario)")
        print("10 - Suporte tecnico")
        print("11 - Controle de pais")
        print("12 - Voltar ao menu principal")

        valor = input("\nEscolha uma opção: ")

        if valor == "1":
            nova_senha = input("Digite a nova senha: ")
            usuarios[nome]["senha"] = nova_senha
            print("Senha alterada com sucesso!")

        elif valor == "2":
            nome_jogo = input("Digite o nome do jogo para adicionar: ")
            if nome_jogo in usuarios[nome]["jogos"]:
                print("O jogo já está na conta do usuário!")
            elif nome_jogo not in jogos:
                  print("\nJogo não encontrado na plataforma.")
                  print("Adicione-o antes na plataforma e depois repita o processo de adicionar a conta")
            else:
                usuarios[nome]["jogos"][nome_jogo] = jogos[nome_jogo]["versao"]
                print(f"Jogo {nome_jogo} (versão {jogos[nome_jogo]['versao']}) adicionado à conta!")


        elif valor == 3: 
             nome_jogo = input("Digite o nome do jogo para adicionar: ")
             if nome_jogo in usuarios[nome]["jogos"]:
                usuarios[nome]["jogos"].remove(nome_jogo)
                print("O jogo já foi removido na conta do usuário!")
             elif nome_jogo not in jogos:
                  print("\nJogo não encontrado na plataforma.")

        elif valor == "4":
            preferencia = input("Digite o nome da preferência: ")
            usuarios[nome]["preferencias"] = preferencia
            print("Preferência atualizada com sucesso!")

        elif valor == "5":
            print(usuarios[nome])

        elif valor == "6":
            compra_item(nome)

        elif valor == "7":
            adicionar_saldo(nome)

        elif valor == "8":
            nome_jogo = input("Em qual jogo voce quer acessar este recurso?")
            chatsforuns(nome, nome_jogo)

        elif valor == "9":
            nome_jogo = input("Qual jogo deseja atualizar")
            atualizar_jogo_usuario(nome, nome_jogo)

        elif valor == "10":
            suporte(nome)

        elif valor == "11":
            filh = input("Qual o nome do seu filho(a)?")
            controle_pais(nome, filh)

        elif valor == "12":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Escolha novamente.")

 
def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    if usuarios:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print("- " + usuario)
    else:
        print("Nenhum usuário cadastrado.")

def adicionar_itens_loja():
    """Adiciona itens à loja de um jogo."""
    
    nome_jogo = input("\nDigite o nome do jogo\n")

    if nome_jogo not in jogos:
         print("Jogo não encontrado!")
         print("Retornando ao menu anterior!")
         return

    if "loja" not in jogos[nome_jogo]:
        jogos[nome_jogo]["loja"] = {}
    
    item = input("\n1 - Nome do item a adicionar: ")

    
        
    preco = float(input("Qual será o preço do item: "))
    jogos[nome_jogo]["loja"][item] = preco
    print("\nItem " +item+ " adicionado por R$ " + str(preco))

def adicionar_conquistas():
    """Adiciona uma conquista a um jogo."""
    nome_jogo = input("\nDigite o nome do jogo onde deseja adicionar a conquista: ")

    if nome_jogo not in jogos:
        print("\nJogo não encontrado na plataforma.")
        return

    conquista = input("\nDigite o nome da conquista a ser adicionada ao jogo "+nome_jogo+": ")
    
    if conquista in jogos[nome_jogo]["conquistas"]:
        print("\nEssa conquista já existe no jogo.")
    else:
        jogos[nome_jogo]["conquistas"].append(conquista)
        print("\nConquista '"+conquista+"' adicionada ao jogo '"+nome_jogo+"' com sucesso!")

def adicionar_pontuacao(nome):
    """Adiciona pontuação a um jogador em um jogo específico."""
    if nome not in usuarios:
        print("\nUsuário não encontrado!")
        return
    
    nome_jogo = input("\nDigite o nome do jogo onde "+nome+" ganhou pontuação: ")

    if nome_jogo not in usuarios[nome]["jogos"]:
        print("\nO usuário não possui esse jogo!")
        return
    
    pontos = int(input("\nDigite a pontuação ganha no jogo "+nome_jogo+": "))
    
    if nome_jogo not in usuarios[nome]["pontuacoes"]:
        usuarios[nome]["pontuacoes"][nome_jogo] = 0
    
    usuarios[nome]["pontuacoes"][nome_jogo] += pontos
    print("\nPontuação adicionada! Nova pontuação no jogo '"+nome_jogo+"':", usuarios[nome]["pontuacoes"][nome_jogo])

def atualizar_jogo(nome_jogo):

    if nome_jogo not in jogos:
        print("\nJogo "+nome_jogo+" não encontrado!")
        return

    nova_versao = input("Digite a nova versão do jogo (ex: 1.1, 2.0): ")
    descricao_patch = input("Digite a descrição da atualização: ")

    # Atualiza o jogo para a nova versão
    jogos[nome_jogo]["versao"] = nova_versao
    jogos[nome_jogo]["patches"].append(f"Versão {nova_versao}: {descricao_patch}")

    print("\nJogo "+nome_jogo+" atualizado para a versão "+nova_versao+"!")

        
def gerenciar_jogo():

    """Gerencia a biblioteca de jogos, permitindo adicionar ou remover jogos."""
    while True:
        print("\nGerenciamento de Jogos:\n")
        print("1 - Adicionar um jogo à plataforma")
        print("2 - Remover um jogo da plataforma")
        print("3 - Adicionar itens ao jogo")
        print("4 - Adicionar conquistas aos jogos")
        print("5 - Desbloquear conquista para jogador")
        print("6 - Atualizar jogo (desenvolvedor)")
        print("7 - Voltar ao menu principal\n")

        opcao = input()

        if opcao == "1":
            nome_jogo = input("Digite o nome do jogo: ")

            if nome_jogo in jogos:
                print("Jogo já existe na plataforma!")
            else:
                online = input("O jogo é online? (s/n): ").strip().lower()
                if online == "s":
                    while True:
                            max_ligas = int(input("Quantas ligas esse jogo terá? (mínimo 1): "))
                            if max_ligas >= 1:
                                break
                            else:
                                print("O número mínimo de ligas deve ser 1.")
                                print("Por favor, insira um número válido.")
                    
                    jogos[nome_jogo] = {
                        "online": True,
                        "max_ligas": max_ligas,
                        "jogadores": {},
                        "forum": [],
                        "versao": "1.0", 
                        "patches": [],
                        "conquistas": []
                    }

                    print("Jogo online adicionado com " + str(max_ligas) + " ligas!")
                    print("O sistema de ligas pode ser pareado com diferença de uma liga acima ou abaixo")
                    print("caso seja a primeira liga, será a parti dela, caso seja a ultima,  a ")
                    print("pontuação é ilimitada")

                else:
                    jogos[nome_jogo] = {
                        "online": False,
                        "jogadores": {},
                        "versao": "1.0", 
                        "patches": [],
                        "conquistas": []
                    }
                    print("Jogo offline adicionado!")

        elif opcao == "2":
            nome_jogo = input("Digite o nome do jogo a ser removido: ")

            if nome_jogo in jogos:
                del jogos[nome_jogo]
                print("Jogo removido com sucesso!")
            else:
                print("O jogo não existe na biblioteca!")

        elif opcao == "3":
            adicionar_itens_loja()

        elif opcao =="4":
            game = input("Qual jogo vocẽ quer adicionar uma nova conquista?")
            adicionar_conquistas()
        
        elif opcao == "5":
            nome = input("Qual o nome do jogador?")
            adicionar_pontuacao(nome)
        
        elif opcao =="6":
            nome_jogo = input("Digite o nome do jogo que deseja atualizar")
            atualizar_jogo(nome_jogo)

        elif opcao == "7":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida! Escolha novamente.")

def listar_jogadores():

    #Lista todos os jogadores com suas conquistas e pontuações.
    if not usuarios:
        print("\nNenhum jogador cadastrado.")
        return

    print("\nLista de jogadores e seus status:")

    for nome, dados in usuarios.items():
        print("\nUsuário: "+nome)
        print("Saldo: R$"+str(dados["saldo"]))
        
        if dados["pontuacoes"]:
            print("Pontuações:")
            for jogo, pontos in dados["pontuacoes"].items():
                print("   ➜ "+jogo+": "+str(pontos)+" pontos")

        if dados["conquistas"]:
            print("Conquistas:")
            for jogo, conquistas in dados["conquistas"].items():
                print("   ➜ "+jogo+": "+", ".join(conquistas))

        print("\n" + "-"*40)

def listar_jogos():

    #Lista todos os jogos disponíveis na biblioteca.

    if jogos:
        print("Jogos disponíveis:")
        for jogo in jogos:
            print("- " + jogo)
    else:
        print("Nenhum jogo disponível.")

def principal():
    # Função principal que gerencia o menu da plataforma.

    while True:
        print("\nMenu Principal:\n")
        print("1 - Criar usuário")
        print("2 - Perfis de usuários")
        print("3 - Menu de jogos da plataforma")
        print("4 - Listar jogos")
        print("5 - Listar usuários")
        print("6 - Sair")
        
        escolha = input("\nEscolha uma opção: ")  # Lê a opção do usuário
        
        if escolha == "1":
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)

        elif escolha == "2":
            usuarinome = input("Qual usuário você quer gerenciar? ")
            gerenciar_perfil(usuarinome)

        elif escolha == "3":
            gerenciar_jogo()

        elif escolha == "4":
            listar_jogos()

        elif escolha == "5":
            listar_usuarios()

        elif escolha == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Escolha novamente.")
principal()
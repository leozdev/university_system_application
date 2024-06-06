import os
from src.auxiliar import existe_arquivo, confirmar

def entrar_dados():
    """
    Solicita ao usuário que insira os dados de uma disciplina.

    Retorna:
        tuple: Tupla contendo as seguintes informações da disciplina:
            - nome (str): Nome da disciplina.
            - ementa (str): Ementa da disciplina.
            - bibliografia (str): Bibliografia da disciplina.
            - n_creditos (str): Número de créditos da disciplina.
            - carga_horaria (str): Carga horária da disciplina.
    """ 
    nome = input("Digite o nome da disciplina: ").title()
    ementa = input("Digite a ementa da disciplina: ").capitalize()
    bibliografia = input("Digite a bibliografia da disciplina: ").capitalize()
    n_creditos = input("Digite o número de créditos da disciplina: ")
    carga_horaria = input("Digite a carga horária da disciplina (00h): ")

    return nome, ementa, bibliografia, n_creditos, carga_horaria

def incluir_dados(db_disciplinas, sigla, nome, ementa, bibliografia, n_creditos, carga_horaria):
    """
    Inclui os dados de uma disciplina no banco de dados.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        sigla (str): Sigla da disciplina.
        nome (str): Nome da disciplina.
        ementa (str): Ementa da disciplina.
        bibliografia (str): Bibliografia da disciplina.
        n_creditos (str): Número de créditos da disciplina.
        carga_horaria (str): Carga horária da disciplina.
    """ 
    db_disciplinas[sigla] = {
        'nome': nome,
        'ementa': ementa,
        'bibliografia': bibliografia,
        'n_creditos': n_creditos,
        'carga_horaria': carga_horaria
    }

def inserir_disciplina(db_disciplinas, sigla):
    """
    Insere uma nova disciplina no banco de dados.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        sigla (str): Sigla da disciplina.

    Retorna:
        bool: True se a disciplina foi inserida com sucesso, False se a disciplina já está cadastrada.
    """ 
    if sigla not in db_disciplinas:
        incluir_dados(db_disciplinas, sigla, *entrar_dados())
        return True  # Dados inseridos com sucesso!
    return False  # Disciplina já cadastrada!

def listar_todas_disciplinas(db_disciplinas):
    """
    Lista todas as disciplinas cadastradas no banco de dados.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
    
    Retorna:
        bool: True se existe algum dado no banco de dados, False caso contrário.
    """ 
    if len(db_disciplinas) < 1:
        return False
    
    print("Disciplinas:\n")
    for sigla in db_disciplinas: 
        print(f"\t{'-' * 30}")
        print("\tSigla da Disciplina:", sigla)
        listar_atributos_disciplina(db_disciplinas, sigla)
    return True

def listar_atributos_disciplina(db_disciplinas, sigla):
    """
    Lista os atributos de uma disciplina específica.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        sigla (str): Sigla da disciplina.

    Retorna:
        bool: True se a disciplina foi encontrada e listada, False caso contrário.
    """ 
    if sigla in db_disciplinas:
        atributos = db_disciplinas[sigla]
        print("\n\tNome:", atributos['nome'])
        print("\tEmenta:", atributos['ementa'])
        print("\tBibliografia:", atributos['bibliografia'])
        print("\tNúmero de Créditos:", atributos['n_creditos'])
        print("\tCarga Horária:", atributos['carga_horaria'])
        return True  # Tudo ocorreu bem!
    return False  # Sigla da Disciplina não encontrada!

def alterar_dados_disciplina(db_disciplinas, sigla):
    """
    Altera os dados de uma disciplina já cadastrada.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        sigla (str): Sigla da disciplina.

    Retorna:
        int: 1 se os dados foram alterados com sucesso, -1 se a alteração foi cancelada, 0 se a sigla não foi encontrada.
    """ 
    if sigla in db_disciplinas:
        dados = entrar_dados()
        if confirmar('alterar'):
            incluir_dados(db_disciplinas, sigla, *dados)
            return 1  # Dados alterados com sucesso!
        return -1  # Alteração cancelada com sucesso!
    return 0  # Sigla não encontrada!

def remover_disciplina(db_disciplinas, sigla):
    """
    Remove uma disciplina do banco de dados.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        sigla (str): Sigla da disciplina.

    Retorna:
        int: 1 se a disciplina foi removida com sucesso, -1 se a remoção foi cancelada, 0 se a disciplina não foi encontrada.
    """ 
    if sigla in db_disciplinas:
        if confirmar('excluir'):
            del db_disciplinas[sigla]
            return 1  # Dados apagados com sucesso!
        return -1  # Exclusão cancelada!
    return 0  # Disciplina não cadastrada!

def gravar_dados(db_disciplinas, path):
    """
    Grava os dados das disciplinas em um arquivo.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        path (str): Caminho do arquivo onde os dados serão salvos.
    """ 
    arq = open(path, "w", encoding="utf-8")
    for sigla, atributos in db_disciplinas.items():
        linha = (f"{sigla};"
                 f"{atributos['nome']};"
                 f"{atributos['ementa']};"
                 f"{atributos['bibliografia']};"
                 f"{atributos['n_creditos']};"
                 f"{atributos['carga_horaria']}\n")
        arq.write(linha)
    arq.close()

def carregar_dados(db_disciplinas, path):
    """
    Carrega os dados das disciplinas de um arquivo.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        path (str): Caminho do arquivo de onde os dados serão carregados.
    """ 
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")
        for linha in arq:
            sigla, nome, ementa, bibliografia, n_creditos, carga_horaria  = linha.strip().split(";")
            incluir_dados(db_disciplinas, sigla, nome, ementa, bibliografia, n_creditos, carga_horaria)
        arq.close()

def submenu_disciplinas():
    """
    Exibe o submenu de gerenciamento de disciplinas e solicita ao usuário que selecione uma opção.

    Retorna:
        int: A opção selecionada pelo usuário.
    """ 
    while True:
        input("\nPressione [enter] para continuar...")
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu de Gerenciamento de Disciplinas ---")
        print("1 - Listar Todas Disciplinas")
        print("2 - Listar uma Disciplina Específica")
        print("3 - Incluir Disciplina")
        print("4 - Alterar Dados de uma Disciplina")
        print("5 - Excluir uma Disciplina")
        print("6 - Voltar")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 6:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def executa(db_disciplinas, path):
    """
    Executa o submenu de disciplinas e a função correspondente com base na opção selecionada pelo usuário.

    Parâmetros:
        db_disciplinas (dict): Banco de dados das disciplinas.
        path (str): Caminho do arquivo onde os dados serão salvos/carregados.
    """ 
    opt_submenu = 1
    while opt_submenu != 6:
        opt_submenu = submenu_disciplinas()
        
        if opt_submenu == 1:
            print("Listando todas as disciplinas cadastradas...\n")
            if not listar_todas_disciplinas(db_disciplinas):
                print("Erro: Nenhuma disciplina cadastrada.")

        elif opt_submenu == 2:
            print("Listando uma determinada disciplina cadastrada...\n")
            sigla = input("Digite a sigla da disciplina que deseja listar: ").upper()

            if not listar_atributos_disciplina(db_disciplinas, sigla):
                print("Erro: Não foi possível localizar os dados da sigla da disciplina.")

        elif opt_submenu == 3:
            print("Inserindo uma nova disciplina...\n")
            sigla = input("Digite a sigla da disciplina que deseja inserir: ").upper()

            if inserir_disciplina(db_disciplinas, sigla):
                print("Sucesso: Disciplina cadastrada com sucesso.")
            else:
                print("Erro: Já existe um cadastro com essa sigla de disciplina.")

        elif opt_submenu == 4:
            print("Alterando os dados de uma disciplina cadastrada...\n")
            sigla = input("Digite a sigla da disciplina que deseja alterar: ").upper()

            retorno = alterar_dados_disciplina(db_disciplinas, sigla)
            if retorno == 1:
                print("Sucesso: Dados da disciplina alterados com sucesso.")
            elif retorno == -1:
                print("Aviso: Alteração cancelada pelo usuário.")
            else:
                print("Erro: Não foi possível localizar os dados da sigla da disciplina.")

        elif opt_submenu == 5:
            print("Removendo uma disciplina cadastrada...\n")
            sigla = input("Digite a sigla da disciplina que deseja remover: ").upper()

            retorno = remover_disciplina(db_disciplinas, sigla)
            if retorno == 1:
                print("Sucesso: Disciplina removida com sucesso.")
            elif retorno == -1:
                print("Aviso: Remoção cancelada pelo usuário.")
            else:
                print("Erro: Não foi possível localizar os dados da sigla da disciplina.")

        # Salva os dados após cada operação e encerra o submenu 
        gravar_dados(db_disciplinas, path)
    print("Voltando ao menu principal...")
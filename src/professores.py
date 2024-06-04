import os
from src.auxiliar import existe_arquivo, confirmar

def entrar_dados():
    """
    Solicita ao usuário que insira os dados de um professor.

    Os dados incluem nome, data de nascimento, sexo, área de pesquisa, titulação, graduação, e-mails e telefones.

    Retorna:
        list: Uma lista contendo os dados do professor [nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones].
    """
    nome = input("Digite o Nome completo: ").title()
    data_nasc = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
    sexo = input("Digite o Sexo (F/M): ").title()
    area = input("Digite a Área de Pesquisa: ").title()
    titulacao = input("Digite a Titulação: ").title()
    graduacao = input("Digite a Graduação: ").title()
    emails = input("Digite os E-mails (separados por vírgula-espaço): ").split(", ")
    telefones = input("Digite os Telefones (separados por vírgula-espaço): ").split(", ")
    
    return [nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones]

def incluir_dados(db_professores, registro, dados):  
    """
    Inclui os dados de um professor no banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        registro (str): O registro funcional do professor.
        dados (list): A lista de dados do professor.
    """  
    nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = dados

    db_professores[registro] = {
        "nome": nome,
        "data-nascimento": data_nasc,
        "sexo": sexo,
        "area-de-pesquisa": area,
        "titulacao": titulacao,
        "graduacao": graduacao,
        "emails": emails,
        "telefones": telefones
    }
    
def inserir_professor(db_professores, registro):
    """
    Insere um novo professor no banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        registro (str): O registro funcional do professor.
    
    Retorna:
        bool: True se o professor foi inserido com sucesso, False se o registro já existe.
    """
    if registro not in db_professores:
        dados = entrar_dados()
        incluir_dados(db_professores, registro, dados)
        return True # Registro foi cadastrado
    return False # Registro já está cadastrado

def listar_todos_professores(db_professores):
    """
    Lista todos os professores cadastrados no banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
    """
    for registro in db_professores:
        print("-" * 30)
        print("Registro Funcional:", registro)
        listar_atributos_professor(db_professores, registro)

def listar_atributos_professor(db_professores, registro):
    """
    Lista os atributos de um professor específico.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        registro (str): O registro funcional do professor.
    
    Retorna:
        bool: True se o registro foi encontrado, False caso contrário.
    """
    if registro in db_professores:
        atributos = db_professores[registro]
        print("\nNome:", atributos['nome'])
        print("Data de Nascimento:", atributos['data-nascimento'])
        print("Sexo:", atributos['sexo'])
        print("Área de Pesquisa:", atributos['area-de-pesquisa'])
        print("Titulação:", atributos['titulacao'])
        print("Graduação:", atributos['graduacao'])
        print("E-mails:", ", ".join(atributos['emails']))
        print("Telefones:", ", ".join(atributos['telefones']))
        return True # Tudo ocorreu bem
    return False # Registro não encontrado

def alterar_dados_professor(db_professores, registro):
    """
    Altera os dados de um professor existente no banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        registro (str): O registro funcional do professor.
    
    Retorna:
        int: 1 se os dados foram alterados com sucesso, -1 se a alteração foi cancelada, 0 se o registro não foi encontrado.
    """
    if registro in db_professores:
        if confirmar('alterar'):
            incluir_dados(db_professores, registro)
            return 1 # Alterado
        return -1 # Alteração Cancelada
    return 0 # Registro não encontrado

def remover_professor(db_professores, registro):
    """
    Remove um professor do banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        registro (str): O registro funcional do professor.
    
    Retorna:
        int: 1 se o professor foi removido com sucesso, -1 se a remoção foi cancelada, 0 se o registro não foi encontrado.
    """
    if registro in db_professores:
        if confirmar('remover'):
            del db_professores[registro]
            return 1 # Excluído
        return -1 # Exclusão Cancelada
    return 0 # Registro não encontrado

def gravar_dados(db_professores, path):
    """
    Grava os dados dos professores em um arquivo.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        path (str): O caminho do arquivo onde os dados serão salvos.
    """
    with open(path, "w", encoding="utf-8") as arq:
        for registro, atributos in db_professores.items():
            linha = (f"{registro};"
                     f"{atributos['nome']};"
                     f"{atributos['data-nascimento']};"
                     f"{atributos['sexo']};"
                     f"{atributos['area-de-pesquisa']};"
                     f"{atributos['titulacao']};"
                     f"{atributos['graduacao']};"
                     f"{','.join(atributos['emails'])};"
                     f"{','.join(atributos['telefones'])}\n")
            arq.write(linha)

def carregar_dados(db_professores, path):
    """
    Carrega os dados dos professores a partir de um arquivo.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        path (str): O caminho do arquivo de onde os dados serão carregados.
    """
    if existe_arquivo(path):
        with open(path, "r", encoding="utf-8") as arq:
            for linha in arq:
                registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = linha.strip().split(";")
                dados = [nome, data_nasc, sexo, area, titulacao, graduacao, emails.split(","), telefones.split(",")]
                incluir_dados(db_professores, registro, dados)

def submenu_professores():
    """
    Exibe o submenu de gerenciamento de professores e solicita ao usuário que selecione uma opção.

    Retorna:
        int: A opção selecionada pelo usuário.
    """
    while True:
        input("\nPressione [enter] para continuar...")
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu de Gerenciamento de Professores ---")
        print("1 - Listar Todos os Cadastros")
        print("2 - Listar um Cadastro Específico")
        print("3 - Incluir Cadastro")
        print("4 - Alterar um Cadastro Existente")
        print("5 - Excluir um Cadastro")
        print("6 - Voltar")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 6:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def executa(db_professores, path):
    """
    Executa o submenu de professores e a função correspondente com base na opção selecionada pelo usuário.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        path (str): O caminho do arquivo onde os dados dos professores serão salvos.
    """ 
    opt_submenu = 1
    while opt_submenu != 6:
        opt_submenu = submenu_professores()

        if opt_submenu == 1:
            print("Todos os professores cadastrados:\n")
            listar_todos_professores(db_professores)

        elif opt_submenu == 2:
            registro = input("Digite o Registro Funcional que deseja listar os dados: ")
            if not listar_atributos_professor(db_professores, registro):
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")

        elif opt_submenu == 3:
            registro = input("Digite o Registro Funcional: ")
            if inserir_professor(db_professores, registro):
                print("Professor cadastrado com sucesso.")
            else:
                print("Erro: Já existe um cadastrado com esse registro funcional no banco de dados.")
        
        elif opt_submenu == 4:
            registro = input("Digite o Registro Funcional que deseja alterar os dados: ")
            retorno = alterar_dados_professor(db_professores, registro)
            if retorno == 1:
                print("Dados do professor alterado com sucesso.")
            elif retorno == -1:
                print("Alteração cancelada!")
            else:
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")

        elif opt_submenu == 5:
            registro = input("Digite o Registro Funcional que deseja remover os dados: ")
            retorno = remover_professor(db_professores, registro)
            if retorno == 1:
                print("Professor removido com sucesso.")
            elif retorno == -1:
                print("Remoção cancelada!")
            else:
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")
        
        # Salva os dados após cada operação e encerra o submenu 
        gravar_dados(db_professores, path)
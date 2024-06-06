import os
from src.auxiliar import existe_arquivo, confirmar

def entrar_dados():
    """
    Solicita ao usuário que insira os dados de um professor.

    Retorna:
        tuple: Tupla contendo as seguintes informações do professor:
            - nome (str): Nome completo do professor.
            - data_nasc (str): Data de nascimento do professor (DD/MM/AAAA).
            - sexo (str): Sexo do professor (F/M).
            - area (str): Área de pesquisa do professor.
            - titulacao (str): Titulação do professor.
            - graduacao (str): Graduação do professor.
            - emails (list): Lista de e-mails do professor.
            - telefones (list): Lista de telefones do professor.
    """
    nome = input("Digite o Nome completo: ").title()
    data_nasc = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
    sexo = input("Digite o Sexo (F/M): ").title()
    area = input("Digite a Área de Pesquisa: ").title()
    titulacao = input("Digite a Titulação: ").title()
    graduacao = input("Digite a Graduação: ").title()
    emails = input("Digite os E-mails (separados por vírgula-espaço): ").split(", ")
    telefones = input("Digite os Telefones (separados por vírgula-espaço): ").split(", ")
    
    return nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones

def incluir_dados(db_professores, registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones):  
    """
    Inclui os dados de um professor no banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        registro (str): O registro funcional do professor.
        nome (str): Nome completo do professor.
        data_nasc (str): Data de nascimento do professor (DD/MM/AAAA).
        sexo (str): Sexo do professor (F/M).
        area (str): Área de pesquisa do professor.
        titulacao (str): Titulação do professor.
        graduacao (str): Graduação do professor.
        emails (list): Lista de e-mails do professor.
        telefones (list): Lista de telefones do professor.
    """  
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
        incluir_dados(db_professores, registro, *entrar_dados())
        return True # Registro foi cadastrado
    return False # Registro já está cadastrado

def listar_todos_professores(db_professores):
    """
    Lista todos os professores cadastrados no banco de dados.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.

    Retorna:
        bool: True se existe algum dado no banco de dados, False caso contrário.
    """
    if len(db_professores) < 1:
        return False
    
    print("Professores:\n")
    for registro in db_professores:
        print(f"\t{'-' * 30}")
        print(f"\tRegistro Funcional: {registro}")
        listar_atributos_professor(db_professores, registro)
    return True

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
        print(f"\n\tNome: {atributos['nome']}")
        print(f"\tData de Nascimento: {atributos['data-nascimento']}")
        print(f"\tSexo: {atributos['sexo']}")
        print(f"\tÁrea de Pesquisa: {atributos['area-de-pesquisa']}")
        print(f"\tTitulação: {atributos['titulacao']}")
        print(f"\tGraduação: {atributos['graduacao']}")
        print(f"\tE-mails: {', '.join(atributos['emails'])}")
        print(f"\tTelefones: {', '.join(atributos['telefones'])}")
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
        dados = entrar_dados()
        if confirmar('alterar'):
            incluir_dados(db_professores, registro, *dados)
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
    arq = open(path, "w", encoding="utf-8")
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
    arq.close()

def carregar_dados(db_professores, path):
    """
    Carrega os dados dos professores de um arquivo.

    Parâmetros:
        db_professores (dict): O banco de dados de professores.
        path (str): O caminho do arquivo de onde os dados serão carregados.
    """
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")
        for linha in arq:
            registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = linha.strip().split(";")

            incluir_dados(db_professores, registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails.split(","), telefones.split(","))
        arq.close()
        
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
            print("Listando todos os professores cadastrados...\n")
            if not listar_todos_professores(db_professores):
                print("Erro: Nenhum professor cadastrado.")

        elif opt_submenu == 2:
            print("Listando os dados de um determinado professor cadastrado...\n")
            registro = input("Digite o Registro Funcional que deseja listar os dados: ")
            
            if not listar_atributos_professor(db_professores, registro):
                print("Erro: Não foi possível localizar os dados do registro funcional.")

        elif opt_submenu == 3:
            print("Inserindo um novo professor...\n")
            registro = input("Digite o Registro Funcional: ")

            if inserir_professor(db_professores, registro):
                print("Sucesso: Professor cadastrado com sucesso.")
            else:
                print("Erro: Já existe um cadastro com esse registro funcional.")

        elif opt_submenu == 4:
            print("Alterando os dados de um professor cadastrado...\n")
            registro = input("Digite o Registro Funcional que deseja alterar os dados: ")

            retorno = alterar_dados_professor(db_professores, registro)
            if retorno == 1:
                print("Sucesso: Dados do professor alterados com sucesso.")
            elif retorno == -1:
                print("Aviso: Alteração cancelada pelo usuário.")
            else:
                print("Erro: Não foi possível localizar os dados do registro funcional.")

        elif opt_submenu == 5:
            print("Removendo um professor cadastrado...\n")
            registro = input("Digite o Registro Funcional que deseja remover os dados: ")

            retorno = remover_professor(db_professores, registro)
            if retorno == 1:
                print("Sucesso: Professor removido com sucesso.")
            elif retorno == -1:
                print("Aviso: Remoção cancelada pelo usuário.")
            else:
                print("Erro: Não foi possível localizar os dados do registro funcional.")

        # Salva os dados após cada operação e encerra o submenu 
        gravar_dados(db_professores, path)
    print("Voltando ao menu principal...")
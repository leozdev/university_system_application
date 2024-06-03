import os
from src.auxiliar import existe_arquivo, confirmar

# Futuramente incluir uma função que checa se não tem campos em brancos!
def entrar_dados():
    """
    DOCSTRING
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
    DOCSTRING
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
    DOCSTRING
    """ 
    if registro not in db_professores:
        dados = entrar_dados()
        incluir_dados(db_professores, registro, dados)
        return True # Registro foi cadastrado
    return False # Registro já está cadastrado

def listar_todos_professores(db_professores):
    """
    DOCSTRING
    """ 
    for registro in db_professores:
        print("-" * 30)
        print("Registro Funcional:", registro)
        listar_atributos_professor(db_professores, registro)

def listar_atributos_professor(db_professores, registro):
    """
    DOCSTRING
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
    DOCSTRING
    """ 
    if registro in db_professores:
        if confirmar('alterar'):
            incluir_dados(db_professores, registro)
            return 1 # Alterado
        return -1 # Alteração Cancelada
    return 0 # Registro não encontrado

def remover_professor(db_professores, registro):
    """
    DOCSTRING
    """ 
    if registro in db_professores:
        if confirmar('remover'):
            del db_professores[registro]
            return 1 # Excluído
        return -1 # Exclusão Cancelada
    return 0 # Registro não encontrado

def gravar_dados(db_professores, path):
    """
    DOCSTRING
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
    DOCSTRING
    """ 
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")

        for linha in arq:
            registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = linha.strip().split(";")
            
            dados = [nome, data_nasc, sexo, area, titulacao, graduacao, emails.split(","), telefones.split(",")]
            incluir_dados(db_professores, registro, dados)
        arq.close()

def submenu_professores():
    """
    DOCSTRING
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
    DOCSTRING
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
        
        # Retornando ao menu principal 
        gravar_dados(db_professores, path)
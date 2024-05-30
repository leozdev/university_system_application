import os
from src.auxiliar import existe_arquivo, confirmar

def entrar_dados():
    """
    DOCSTRING
    """ 
    nome = input("Digite o nome da disciplina: ").title()
    ementa = input("Digite a ementa da disciplina: ").capitalize()
    bibliografia = input("Digite a bibliografia da disciplina: ").capitalize()
    n_creditos = input("Digite o número de creditos da disciplina: ")
    carga_horaria = input("Digite a carga horária da disciplina (00h): ")

    return [nome, ementa, bibliografia, n_creditos, carga_horaria]

def incluir_dados(db_disciplinas, sigla, dados):
    """
    DOCSTRING
    """ 
    nome, ementa, bibliografia, n_creditos, carga_horaria = dados

    db_disciplinas[sigla] = {
    'nome': nome,
    'ementa': ementa, 
    'bibliografia': bibliografia,
    'n_creditos': n_creditos,
    'carga_horaria': carga_horaria
    }
    
def inserir_disciplina(db_disciplinas, sigla):
    """
    DOCSTRING
    """ 
    if sigla not in db_disciplinas:
        dados = entrar_dados()
        incluir_dados(db_disciplinas, sigla, dados)
        return True # Dados inseridos com sucesso!
    return False # Disciplina já cadastrada!

def listar_todas_disciplinas(db_disciplinas):
    """
    DOCSTRING
    """ 
    for sigla in db_disciplinas: 
        print("-" * 30)
        print("Sigla da Disciplina:", sigla)
        listar_atributos_disciplina(db_disciplinas, sigla)

def listar_atributos_disciplina(db_disciplinas, sigla):
    """
    DOCSTRING
    """ 
    if sigla in db_disciplinas:
        atributos = db_disciplinas[sigla]
        print("\nNome:", atributos['nome'])
        print("Ementa:", atributos['ementa'])
        print("Bibliografia:", atributos['bibliografia'])
        print("Número de Créditos:", atributos['n_creditos'])
        print("Carga Horária:", atributos['carga_horaria'])
        return True # Tudo ocorreu bem!
    return False # Sigla da Disciplina não encontrada!

def alterar_dados_disciplina(db_disciplinas, sigla):
    """
    DOCSTRING
    """ 
    if sigla in db_disciplinas:
        if confirmar('alterar'):
            incluir_dados(db_disciplinas, sigla)
            return 1 # Dados alterados com sucesso!
        return -1 # Alteração cancelada com sucesso!
    return 0 # Sigla não encontrada!

def remover_disciplina(db_disciplinas, sigla):
    """
    DOCSTRING
    """ 
    if sigla in db_disciplinas:
        if confirmar('excluir'):
            del db_disciplinas[sigla]
            return 1 # Dados apagados com sucesso!
        return -1 # Exclusão cancelada!
    return 0 # Disciplina não cadastrada!

def gravar_dados(db_disciplinas, path):
    """
    DOCSTRING
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
    DOCSTRING
    """ 
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")
        for linha in arq:
            dados = linha.strip().split(";")
            incluir_dados(db_disciplinas, dados[0], dados[1:])

def submenu_disciplinas():
    """
    DOCSTRING
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
    DOCSTRING
    """ 
    opt_submenu = 1
    while opt_submenu != 6:
        opt_submenu = submenu_disciplinas()
        
        if opt_submenu == 1:
            print("Todas disciplinas cadastradas:\n")
            listar_todas_disciplinas(db_disciplinas)

        elif opt_submenu == 2:
            sigla = input("Digite a sigla da disciplina que deseja listar: ")

            if not listar_atributos_disciplina(db_disciplinas, sigla):
                print("Erro: Essa sigla da disciplina não consta no banco de dados de disciplinas.")

        elif opt_submenu == 3:
            sigla = input("Digite a sigla da disciplina que deseja inserir: ")

            if inserir_disciplina(db_disciplinas, sigla):
                print("Disciplina cadastrada com sucesso.")
            else:
                print("Erro: Já existe um cadastrado dessa sigla da disciplina no banco de dados.")

        # Pensar em alguma solução melhor que essa (Se tiver como...)
        elif opt_submenu == 4:
            sigla = input("Digite a sigla da disciplina que deseja alterar: ")

            retorno = alterar_dados_disciplina(db_disciplinas, sigla)
            if retorno == 1:
                print("Dados da disciplina alterado com sucesso.")
            elif retorno == -1:
                print("Alteração cancelada!")
            else:
                print("Erro: Essa sigla da disciplina não consta no banco de dados de disciplinas.")

        elif opt_submenu == 5:
            sigla = input("Digite a sigla da disciplina que deseja remover: ")

            retorno = remover_disciplina(db_disciplinas, sigla)
            if retorno == 1:
                print("Disciplina removida com sucesso.")
            elif retorno == -1:
                print("Remoção cancelada!")
            else:
                print("Erro: Essa sigla da disciplina não consta no banco de dados de disciplinas.")
        
        # Retornando ao menu principal 
        gravar_dados(db_disciplinas, path)
            
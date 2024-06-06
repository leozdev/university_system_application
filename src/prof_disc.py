import os
from src.auxiliar import existe_arquivo, confirmar
# TERROR DE TODOS

def entrada_registro():
    """
    Solicita e retorna o registro funcional do professor.

    Parametros:
    db_professores (dict): Dicionário contendo o banco de dados de professores.

    Retorna:
    str or None: O registro funcional do professor, se encontrado no banco de dados, senão retorna None.
    """
    registro = input("Digite o Registro Funcional: ")
    return registro

def entrada_chaves():
    """
    Solicita e retorna as chaves (sigla, ano, semestre) da disciplina.

    Parametros:
    db_disciplinas (dict): Dicionário contendo o banco de dados de disciplinas.

    Retorna:
    tuple: Uma tupla contendo a sigla, o ano e o semestre da disciplina, se encontrada no banco de dados, senão retorna uma tupla de valores nulos.
    """
    sigla = input("Digite a Sigla da Disciplina: ")
    ano = input("Digite o Ano: ")
    semestre = input("Digite o Semestre: ")
    return sigla, ano, semestre 

def entrada_atributos():
    dias_da_semana = input("Digite os Dias da Semana (separados por vírgula): ").split(", ")
    horarios_inicio = input("Digite os Horários do curso (separados por vírgula): ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")

    return [dias_da_semana, horarios_inicio, nome_do_curso]

def incluir_dados(db_prof_disc, registro, sigla_disciplina, ano, semestre, atributos):
    """
    Inclui os dados da disciplina no banco de dados de professores-disciplinas.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    registro (str): O registro funcional do professor.
    sigla_disciplina (str): A sigla da disciplina.
    ano (str): O ano da disciplina.
    semestre (str): O semestre da disciplina.
    """
    dias_da_semana, horarios_inicio, nome_do_curso = atributos 

    db_prof_disc[registro][(sigla_disciplina, ano, semestre)] = {
    "dias_da_semana": dias_da_semana,
    "horarios_inicio": horarios_inicio,
    "curso": nome_do_curso
    }

def inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas):
    """
    Insere um novo registro no banco de dados de professores-disciplinas.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    db_professores (dict): Dicionário contendo o banco de dados de professores.
    db_disciplinas (dict): Dicionário contendo o banco de dados de disciplinas.

    Retorna:
    int: 1 se o registro foi inserido com sucesso, -1 se o registro funcional não existe no banco de dados de professores, -2 se a sigla da disciplina não existe no banco de dados de disciplinas, 0 se o registro já existe no banco de dados de professores-disciplinas.
    """
    registro = entrada_registro()
    if not registro:
        return -1 # Registro não existente no db_professores
    
    db_prof_disc[registro] = {}

    sigla, ano, semestre = entrada_chaves()
    if not (sigla and ano and semestre):
        return -2 # Sigla não existente no db_disciplinas
    
    if (sigla, ano, semestre) not in db_prof_disc[registro]:
        incluir_dados(db_prof_disc, registro, sigla, ano, semestre, entrada_atributos())
        return 1 # Cadastrado com sucesso no db_prof_disc
    return 0 # Cadastro já existe no prof_disc
   
def listar_todas_aulas(db_prof_disc):
    """
    Lista todas as aulas cadastradas por professor.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    """
    print("Todas as aulas cadastradas por professor:\n")
    for registro in db_prof_disc:
        print(f"{'-' * 30}")
        print(f"Registro Funcional do Professor: {registro}")
        listar_atributos_aula(db_prof_disc, registro)

def listar_atributos_aula(db_prof_disc, registro):
    """
    Lista os atributos de uma aula específica.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    registro (str): O registro funcional do professor.

    Retorna:
    bool: True se o registro foi encontrado e os atributos listados, False caso contrário.
    """
    if registro in db_prof_disc:
        for (sigla_disciplina, ano, semestre), atributos in db_prof_disc[registro].items():
            print(f"\nSigla da disciplina: {sigla_disciplina}")
            print(f"Ano: {ano}")
            print(f"Semestre: {semestre}")
            print(f"Dias da Semana: {', '.join(atributos['dias_da_semana'])}")
            print(f"Horários de início: {', '.join(atributos['horarios_inicio'])}")
            print(f"Curso: {atributos['curso']}")
        return True # Tudo ocorreu bem
    return False # Registro não encontrado no db_prof_disc
    
###############################################################################
def existe_dados(db_prof_disc, db_professores, db_disciplinas):

    registro = entrada_registro(db_professores)
    if registro:
        sigla, ano, semestre = entrada_chaves(db_disciplinas)
        if sigla and ano and semestre:
            if (sigla, ano, semestre) in db_prof_disc[registro]:
                return registro, (sigla, ano, semestre)
###############################################################################

################
def alterar_cadastro(db_prof_disc):
    """
    Permite ao usuário alterar os dados de uma aula existente.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.

    Retorna:
    int: 1 se os dados foram alterados com sucesso, 0 se a alteração foi cancelada, -1 se o registro funcional não existe, -2 se as chaves da disciplina não existem.
    """
    registro = entrada_registro()
    if registro:
        conjunto_chaves = entrada_chaves()
        
        if conjunto_chaves in db_prof_disc[registro]:
            print("\nAtualize os dados:\n")

            if confirmar('alterar'):
                incluir_dados(db_prof_disc, registro, *conjunto_chaves, novo_cadastro=False)
                return 1 # Alterado com sucesso!
            return 0 # Alteração cancelada!
        return -2 # Conjuntos chaves não existe
    return -1 # Registro não existe

def remover_prof_disc(db_prof_disc):
    """
    Permite ao usuário remover uma aula existente.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.

    Retorna:
    int: 1 se a aula foi removida com sucesso, 0 se a remoção foi cancelada, -1 se o registro funcional não existe, -2 se as chaves da disciplina não existem.
    """
    registro = entrada_registro()
    if registro:
        conjunto_chaves = entrada_chaves()
        
        if conjunto_chaves in db_prof_disc[registro]:

            if confirmar('excluir'):
                if len(db_prof_disc[registro]) > 1:
                    del db_prof_disc[registro][conjunto_chaves]
                else:
                    del db_prof_disc[registro]
                return 1 # Excluido com sucesso!
            return 0 # Exclusão Cancelada
        return -2 # Conjuntos chaves não existe
    return -1 # Registro não existe
    
def gravar_dados(db_prof_disc, path):
    """
    Grava os dados do banco de dados de professores-disciplinas em um arquivo.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    path (str): O caminho do arquivo onde os dados serão gravados.
    """
    arq =  open(path, "w", encoding="utf-8")

    for registro in db_prof_disc:
        for conjunto_chaves, atributos in db_prof_disc[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves

            linha = (f"{registro};"
                     f"{sigla_disciplina};"
                     f"{ano};{semestre};"
                     f"{','.join(atributos['dias_da_semana'])};"
                     f"{','.join(atributos['horarios_inicio'])};"
                     f"{atributos['curso']}\n")
            arq.write(linha)

    arq.close()

def carregar_dados(db_prof_disc, path):
    """
    Carrega os dados do arquivo para o banco de dados de professores-disciplinas.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    path (str): O caminho do arquivo de onde os dados serão carregados.
    """
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")

        for linha in arq:
            registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, nome_do_curso = linha.strip().split(";")

            if registro not in db_prof_disc:
                db_prof_disc[registro] = {}

            db_prof_disc[registro][(sigla_disciplina, ano, semestre)] = {
            "dias_da_semana": dias_da_semana.split(','),
            "horarios_inicio": horarios_inicio.split(','),
            "curso": nome_do_curso
            }

        arq.close()

def submenu_prof_disc():
    """
    Exibe o menu de gerenciamento de professores-disciplinas e solicita uma opção do usuário.

    Retorna:
    int: A opção selecionada pelo usuário.
    """
    while True:
        input("\nPressione [enter] para continuar...")
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu de Gerenciamento de Professores-Disciplinas ---")
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

def executa(db_prof_disc, db_professores, db_disciplinas, path):
    """
    Executa o menu de gerenciamento de professores-disciplinas.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    db_professores (dict): Dicionário contendo o banco de dados de professores.
    db_disciplinas (dict): Dicionário contendo o banco de dados de disciplinas.
    path (str): O caminho do arquivo onde os dados serão gravados.
    """
    while True:
        opt = submenu_prof_disc()

        if opt == 1:
            listar_todas_aulas(db_prof_disc)
#######################
        elif opt == 2:
            registro = input("Digite o Registro Funcional: ")
            if not listar_atributos_aula(db_prof_disc, registro):
                print("Erro: Essa aula ainda não foi cadastrada no banco de dados professores-disciplinas.")

        elif opt == 3:
            retorno = inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas)

            if retorno == 0:
                print("Erro: Já existe um cadastrado dessa aula no banco de dados.")
            elif retorno == -1:
                print("Erro: Esse registro funcional ainda não foi cadastrado no banco de dados de professores.")
            elif retorno == -2:
                print("Erro: Essa sigla da disciplina não consta no banco de dados de disciplinas.")
            else:
                print("Aula cadastrada com sucesso.")

        elif opt == 4:
            retorno = alterar_cadastro(db_prof_disc)

            if retorno == 0:
                print("Alteração cancelada!")
            elif retorno == -1:
                print("Erro: Esse registro funcional ainda não foi cadastrado no banco de dados de professores.")
            elif retorno == -2:
                print("Erro: Essa aula ainda não foi cadastrada no banco de dados professores-disciplinas.")
            else:
                print("Dados da aula alterado com sucesso.")

        elif opt == 5:
            retorno = remover_prof_disc(db_prof_disc)

            if retorno == 0:
                print("Remoção cancelada!")
            elif retorno == -1:
                print("Erro: Esse registro funcional ainda não foi cadastrado no banco de dados de professores.")
            elif retorno == -2:
                print("Erro: Essa aula ainda não foi cadastrada no banco de dados professores-disciplinas.")
            else:
                print("Aula removida com sucesso!")
                
        elif opt == 6:
            gravar_dados(db_prof_disc, path)
            return

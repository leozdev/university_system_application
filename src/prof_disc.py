import os
from src.auxiliar import existe_arquivo, confirmar

def entrar_chaves():
    """
    Solicita ao usuário que insira o registro funcional, a sigla da disciplina, o ano e o semestre.

    Retorna:
        tuple: Contendo o registro funcional (str), a sigla da disciplina (str), o ano (str) e o semestre (str).
    """
    registro = input("Digite o Registro Funcional: ")
    sigla = input("Digite a sigla da disciplina: ")
    ano = input("Digite o Ano: ")
    semestre = input("Digite o Semestre: ")
    return registro, sigla, ano, semestre

def entrar_atributos():
    """
    Solicita ao usuário que insira os dias da semana, os horários de início e o nome do curso.

    Retorna:
        tuple: Contendo os dias da semana (list), os horários de início (list) e o nome do curso (str).
    """
    dias_da_semana = input("Digite os Dias da Semana (separados por vírgula): ").split(", ")
    horarios_inicio = input("Digite os Horários do curso (separados por vírgula): ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")
    return dias_da_semana, horarios_inicio, nome_do_curso

def incluir_dados(db_prof_disc, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, nome_do_curso):
    """
    Inclui dados de um professor-disciplina no banco de dados.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        registro (str): O registro funcional do professor.
        sigla_disciplina (str): A sigla da disciplina.
        ano (str): O ano da disciplina.
        semestre (str): O semestre da disciplina.
        dias_da_semana (list): Lista de dias da semana.
        horarios_inicio (list): Lista de horários de início.
        nome_do_curso (str): Nome do curso.
    """
    db_prof_disc[(registro, sigla_disciplina, ano, semestre)] = {
        "dias_da_semana": dias_da_semana,
        "horarios_inicio": horarios_inicio,
        "curso": nome_do_curso
    }

def verificar_dados(db_professores, db_disciplinas, registro, sigla):
    """
    Verifica se o registro funcional e a sigla da disciplina existem nos bancos de dados de professores e disciplinas.

    Parametros:
        db_professores (dict): Dicionário contendo o banco de dados de professores.
        db_disciplinas (dict): Dicionário contendo o banco de dados de disciplinas.
        registro (str): O registro funcional do professor.
        sigla (str): A sigla da disciplina.

    Retorna:
        bool: True se ambos o registro e a sigla existirem, False caso contrário.
    """
    if registro in db_professores and sigla in db_disciplinas:
        return True
    return False

def inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas, registro, sigla, ano, semestre):
    """
    Insere umm novo professor-disciplina no db_prof_disc.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        db_professores (dict): Dicionário contendo o banco de dados de professores.
        db_disciplinas (dict): Dicionário contendo o banco de dados de disciplinas.
        registro (str): O registro funcional do professor.
        sigla (str): A sigla da disciplina.
        ano (str): O ano da disciplina.
        semestre (str): O semestre da disciplina.

    Retorna:
        int: 1 se cadastrado com sucesso, -1 se o cadastro já existe, 0 se o registro ou a sigla não existem.
    """
    if verificar_dados(db_professores, db_disciplinas, registro, sigla):
        if (registro, sigla, ano, semestre) not in db_prof_disc:
            incluir_dados(db_prof_disc, registro, sigla, ano, semestre, *entrar_atributos())
            return 1  # Cadastrado com sucesso no db_prof_disc
        return -1  # Cadastro já existe no prof_disc
    return 0  # Registro funcional e/ou sigla da disciplina inexistente no db_professores/db_disciplinas.
   
def listar_todos_prof_disc(db_prof_disc):
    """
    Lista todos os dados dos professores-disciplinas cadastrados.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.

    Retorna:
        bool: True se existe algum dado no banco de dados, False caso contrário.
    """
    if len(db_prof_disc) < 1:
        return False
    
    print("Professores-disciplinas:\n")
    for (registro, sigla, ano, semestre) in db_prof_disc:
        print(f"\t{'-' * 30}")
        listar_atributos_prof_disc(db_prof_disc, registro, sigla, ano, semestre)
    return True

def listar_atributos_prof_disc(db_prof_disc, registro, sigla, ano, semestre):
    """
    Lista os atributos de um professor-disciplina específico.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        registro (str): O registro funcional do professor.
        sigla (str): A sigla da disciplina.
        ano (str): O ano da disciplina.
        semestre (str): O semestre da disciplina.

    Retorna:
        bool: True se o conjunto de chaves foi encontrado e os atributos listados, False caso contrário.
    """
    if (registro, sigla, ano, semestre) in db_prof_disc:
        atributos = db_prof_disc[(registro, sigla, ano, semestre)]
        print(f"\tRegistro Funcional do Professor: {registro}")
        print(f"\tSigla da disciplina: {sigla}")
        print(f"\tAno: {ano}")
        print(f"\tSemestre: {semestre}")
        print(f"\tDias da Semana: {', '.join(atributos['dias_da_semana'])}")
        print(f"\tHorários de início: {', '.join(atributos['horarios_inicio'])}")
        print(f"\tCurso: {atributos['curso']}")
        return True 
    return False 
    
def alterar_cadastro(db_prof_disc, registro, sigla, ano, semestre):
    """
    Altera os dados de um professor-disciplina cadastrado.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        registro (str): O registro funcional do professor.
        sigla (str): A sigla da disciplina.
        ano (str): O ano da disciplina.
        semestre (str): O semestre da disciplina.

    Retorna:
        int: 1 se alterado com sucesso, -1 se a alteração foi cancelada, 0 se os dados não foram encontrados.
    """
    if (registro, sigla, ano, semestre) in db_prof_disc:
        atributos = entrar_atributos()
        if confirmar('alterar'):
            incluir_dados(db_prof_disc, registro, sigla, ano, semestre, *atributos)
            return 1  # Alterado com sucesso!
        return -1  # Alteração cancelada!
    return 0  # Dados não encontrados (Registro ou (sigla, ano, semestre)) no db_prof_disc

def remover_prof_disc(db_prof_disc, registro, sigla, ano, semestre):
    """
    Remove os dados de um professor-disciplina cadastrado.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        registro (str): O registro funcional do professor.
        sigla (str): A sigla da disciplina.
        ano (str): O ano da disciplina.
        semestre (str): O semestre da disciplina.

    Retorna:
        int: 1 se removido com sucesso, -1 se a remoção foi cancelada, 0 se os dados não foram encontrados.
    """
    if (registro, sigla, ano, semestre) in db_prof_disc:
        if confirmar('excluir'):
            del db_prof_disc[(registro, sigla, ano, semestre)]
            return 1  # Removido com sucesso!
        return -1  # Remoção cancelada
    return 0  # Dados não encontrados (Registro ou (sigla, ano, semestre)) no db_prof_disc

def gravar_dados(db_prof_disc, path):
    """
    Grava os dados do db_prof_disc em um arquivo.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        path (str): O caminho do arquivo onde os dados serão gravados.
    """
    arq = open(path, "w", encoding="utf-8")
    for conjunto_chaves in db_prof_disc:
        registro, sigla_disciplina, ano, semestre = conjunto_chaves
        atributos = db_prof_disc[conjunto_chaves]

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
    Carrega os dados do arquivo para o dicionario db_prf_disc.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        path (str): O caminho do arquivo de onde os dados serão carregados.
    """
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")
        for linha in arq:
            registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, nome_do_curso = linha.strip().split(";")
            incluir_dados(db_prof_disc, registro, sigla_disciplina, ano, semestre, dias_da_semana.split(','), horarios_inicio.split(','), nome_do_curso)
        arq.close()

def submenu_prof_disc():
    """
    Exibe o menu de gerenciamento de professores-disciplinas e solicita ao usuário que selecione uma opção.

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
    Executa o submenu de professores-disciplinas e a função correspondente com base na opção selecionada pelo usuário.

    Parametros:
        db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
        db_professores (dict): Dicionário contendo o banco de dados de professores.
        db_disciplinas (dict): Dicionário contendo o banco de dados de disciplinas.
        path (str): O caminho do arquivo onde os dados serão gravados.
    
    """
    opt_submenu = 1
    while opt_submenu != 6:
        opt_submenu = submenu_prof_disc()

        if opt_submenu == 1:
            print("Listando todas os professores-disciplinas cadastradas...\n")
            if not listar_todos_prof_disc(db_prof_disc):
                print("Erro: Nenhum professor-disciplina cadastrado.")
            
        elif opt_submenu == 2:
            print("Listando os dados de um determinado professor-disciplina cadastrada...\n")
            if not listar_atributos_prof_disc(db_prof_disc, *entrar_chaves()):
                print("Erro: Não foi possível localizar os dados desse professor-disciplina.")

        elif opt_submenu == 3:
            print("Inserindo umm novo professor-disciplina...\n")
            registro, sigla, ano, semestre = entrar_chaves()
            retorno = inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas, registro, sigla, ano, semestre)

            if retorno == 0:
                print("Erro: Registro funcional ou sigla da disciplina inexistente.")
            elif retorno == -1:
                print("Erro: Já existe um cadastro para este professor-disciplina.")
            else:
                print("Sucesso: Professor-disciplina cadastrado com sucesso.")

        elif opt_submenu == 4:
            print("Alterando os dados de um professor-disciplina cadastrado...\n")
            registro, sigla, ano, semestre = entrar_chaves()
            retorno = alterar_cadastro(db_prof_disc, registro, sigla, ano, semestre)

            if retorno == 0:
                print("Erro: Não foi possível localizar os dados deste professor-disciplina.")
            elif retorno == -1:
                print("Aviso: Alteração cancelada pelo usuário.")
            else:
                print("Sucesso: Dados do professor-disciplina alterados com sucesso.")

        elif opt_submenu == 5:
            print("Excluindo um professor-disciplina cadastrada...\n")
            registro, sigla, ano, semestre = entrar_chaves()
            retorno = remover_prof_disc(db_prof_disc, registro, sigla, ano, semestre)

            if retorno == 0:
                print("Erro: Não foi possível localizar os dados deste professor-disciplina.")
            elif retorno == -1:
                print("Aviso: Remoção cancelada pelo usuário.")
            else:
                print("Sucesso: Professor-disciplina removido com sucesso.")
    
    # Opção 6 -> Salva os dados  e encerra o submenu
    gravar_dados(db_prof_disc, path)
    print("Voltando ao menu principal...")

import os
from src.auxiliar import existe_arquivo, confirmar

def entrar_chaves():
    registro = input("Digite o Registro Funcional: ")
    sigla = input("Digite a sigla da disciplina: ")
    ano = input("Digite o Ano: ")
    semestre = input("Digite o Semestre: ")
    return registro, sigla, ano, semestre

def entrar_atributos():
    dias_da_semana = input("Digite os Dias da Semana (separados por vírgula): ").split(", ")
    horarios_inicio = input("Digite os Horários do curso (separados por vírgula): ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")
    return dias_da_semana, horarios_inicio, nome_do_curso

def incluir_dados(db_prof_disc, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, nome_do_curso):
    db_prof_disc[(registro, sigla_disciplina, ano, semestre)] = {
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

    Retorna:
    # bool: True se existe algum dado no banco de dados, False caso contrário.
    """
    if len(db_prof_disc) < 1:
        return False
    
    print("Aulas:\n")
    for (registro, sigla, ano, semestre) in db_prof_disc:
        print(f"\t{'-' * 30}")
        listar_atributos_aula(db_prof_disc, registro, sigla, ano, semestre)
    return True

def listar_atributos_aula(db_prof_disc, registro, sigla, ano, semestre):
    """
    Lista os atributos de uma aula específica.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    registro (str): O registro funcional do professor.

    Retorna:
    bool: True se o conjunto chaves foi encontrado e os atributos listados, False caso contrário.
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
    if (registro, sigla, ano, semestre) in db_prof_disc:
        atributos = entrar_atributos()
        if confirmar('alterar'):
            incluir_dados(db_prof_disc, registro, sigla, ano, semestre, *atributos)

            return 1  # Alterado com sucesso!
        return -1  # Alteração cancelada!
    return 0  # Dados não encontrados (Registro ou (sigla, ano, semestre)) no db_prof_disc

def remover_prof_disc(db_prof_disc, registro, sigla, ano, semestre):
    if (registro, sigla, ano, semestre) in db_prof_disc:
        if confirmar('excluir'):
            del db_prof_disc[(sigla, ano, semestre)]

            return 1  # Removido com sucesso!
        return -1  # Remoção cancelada
    return 0  # Dados não encontrados (Registro ou (sigla, ano, semestre)) no db_prof_disc

def gravar_dados(db_prof_disc, path):
    """
    Grava os dados do banco de dados de professores-disciplinas em um arquivo.

    Parametros:
    db_prof_disc (dict): Dicionário contendo o banco de dados de professores-disciplinas.
    path (str): O caminho do arquivo onde os dados serão gravados.
    """
    arq =  open(path, "w", encoding="utf-8")
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
    Carrega os dados do arquivo para o banco de dados de professores-disciplinas.

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
    opt_submenu = 1
    while opt_submenu != 6:
        opt_submenu = submenu_prof_disc()

        if opt_submenu == 1:
            print("Listando todas as aulas cadastradas...\n")
            if not listar_todas_aulas(db_prof_disc):
                print("Erro: Nenhuma aula cadastrada.")
            
        elif opt_submenu == 2:
            print("Listando os dados de uma determinada aula cadastrada...\n")
            if not listar_atributos_aula(db_prof_disc, *entrar_chaves()):
                print("Erro: Não foi possível localizar os dados desta aula.")

        elif opt_submenu == 3:
            print("Inserindo uma nova aula...\n")
            registro, sigla, ano, semestre = entrar_chaves()
            retorno = inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas, registro, sigla, ano, semestre)

            if retorno == 0:
                print("Erro: Registro funcional ou sigla da disciplina inexistente.")
            elif retorno == -1:
                print("Erro: Já existe um cadastro para esta aula.")
            else:
                print("Sucesso: Aula cadastrada com sucesso.")

        elif opt_submenu == 4:
            print("Alterando os dados de uma aula cadastrada...\n")
            registro, sigla, ano, semestre = entrar_chaves()
            retorno = alterar_cadastro(db_prof_disc, registro, sigla, ano, semestre)

            if retorno == 0:
                print("Erro: Não foi possível localizar os dados desta aula.")
            elif retorno == -1:
                print("Aviso: Alteração cancelada pelo usuário.")
            else:
                print("Sucesso: Dados da aula alterados com sucesso.")

        elif opt_submenu == 5:
            print("Excluindo uma aula cadastrada...\n")
            registro, sigla, ano, semestre = entrar_chaves()
            retorno = remover_prof_disc(db_prof_disc, registro, sigla, ano, semestre)

            if retorno == 0:
                print("Erro: Não foi possível localizar os dados desta aula.")
            elif retorno == -1:
                print("Aviso: Remoção cancelada pelo usuário.")
            else:
                print("Sucesso: Aula removida com sucesso.")

        # Salva os dados após cada operação e encerra o submenu 
        gravar_dados(db_prof_disc, path)
    print("Voltando ao menu principal...")
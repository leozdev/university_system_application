import os
from src.auxiliar import existe_arquivo, confirmar

def submenu_prof_disc():
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

def entrada_registro(db_professores):
    registro = input("Digite o Registro Funcional: ")
    return registro if registro in db_professores else None #Retorna o registro se ele estiver no db_professores, caso contrário retorna um valor nulo

def entrada_chaves(db_disciplinas):
    sigla = input("Digite a Sigla da Disciplina: ")
    if sigla in db_disciplinas:
        ano = input("Digite o Ano: ")
        semestre = input("Digite o Semestre: ")
        return sigla, ano, semestre # Retorna uma tupla de chaves se a sigla existir no db_disciplinas
    print("A disciplina não foi encontrada no banco de dados.")
    return None, None, None # Retorna uma tupla de valores nulos se a sigla não existir no db_disciplinas

def incluir_dados(db_prof_disc, registro, sigla_disciplina, ano, semestre, novo_cadastro=True):
    dias_da_semana = input("Digite os Dias da Semana (separados por vírgula): ").split(", ")
    horarios_inicio = input("Digite os Horários do curso (separados por vírgula): ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")

    if novo_cadastro:
        if registro not in db_prof_disc:
            db_prof_disc[registro] = {}

    db_prof_disc[registro][(sigla_disciplina, ano, semestre)] = {
    "dias_da_semana": dias_da_semana,
    "horarios_inicio": horarios_inicio,
    "curso": nome_do_curso
    }
    # return True # Cadastrado com sucesso
    # return False # Cadastro já existe

def inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas):
    registro = entrada_registro(db_professores)
    if not registro:
        return 0 # Registro não existente
    
    sigla, ano, semestre = entrada_chaves(db_disciplinas)
    if not (sigla and ano and semestre):
        return 0 # Sigla não existente
    
    if (sigla, ano, semestre) not in db_prof_disc[registro]:
        if incluir_dados(db_prof_disc, registro, sigla, ano, semestre, novo_cadastro=True):
            return 1 # Cadastrado com sucesso
    return -1 # Cadastro já existe
   
def listar_todos(db_prof_disc):
    print("Todos os dados cadastrados:\n")
    for registro in db_prof_disc:
        print(f"{'-' * 30}")
        print(f"Registro Funcional do Professor: {registro}")
        listar_atributos(db_prof_disc, registro)

def listar_atributos(db_prof_disc, registro=None):
    if registro is None:
        registro = entrada_registro()
        if not registro:
            return 0 # Registro não existe no db_professores consequentemente não existe no db_prof_disc
        
    if registro in db_prof_disc:
        for (sigla_disciplina, ano, semestre), atributos in db_prof_disc[registro].items():
            print(f"\nSigla da disciplina: {sigla_disciplina}")
            print(f"Ano: {ano}")
            print(f"Semestre: {semestre}")
            print(f"Dias da Semana: {', '.join(atributos['dias_da_semana'])}")
            print(f"Horários de início: {', '.join(atributos['horarios_inicio'])}")
            print(f"Curso: {atributos['curso']}")
        return 1 # Tudo ocorreu bem
    else:
        return 0 # Registro não encontrado no db_prof_disc

def existe_dados(db_prof_disc, db_professores, db_disciplinas, mostrar_mensagens=True):
    registro = entrada_registro(db_professores)
    if registro:
        sigla, ano, semestre = entrada_chaves(db_disciplinas)
        if sigla and ano and semestre:
            if (sigla, ano, semestre) in db_prof_disc[registro]:
                return registro, (sigla, ano, semestre)
            
            elif mostrar_mensagens:
                print("Dados não encontrados.")
        elif mostrar_mensagens:
            print("Sigla da disciplina não encontrado no banco de dados.")
    elif mostrar_mensagens:
        print("Registro não encontrado no banco de dados.")
    
    return None, None

def excluir_cadastro(db_prof_disc):
    registro, conjunto_chaves = existe_dados(db_prof_disc)
    
    if registro and conjunto_chaves:
        if confirmar('excluir'):
            if len(db_prof_disc[registro]) > 1:
                del db_prof_disc[registro][conjunto_chaves]
            else:
                del db_prof_disc[registro]
            return 1 # Excluido com sucesso!
        else:
            return -1 # Exclusão Cancelada
    return 0 # Registro ou Conjunto Chaves não existe

def alterar_cadastro(db_prof_disc):
    registro, conjunto_chaves = existe_dados(db_prof_disc)

    if registro and conjunto_chaves:
        print("\nAtualize os dados:\n")

        if confirmar('alterar'):
            incluir_dados(db_prof_disc, registro, *conjunto_chaves, novo_cadastro=False)
            return 1 # Alterado com sucesso!
        else:
            return -1 # Alteração cancelada com sucesso!
    return 0 # Registro ou Conjunto Chaves não existe
    
def gravar_dados(db_prof_disc, path):
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

#Refatorar essa função
def carregar_dados(db_prof_disc, path):
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")

        for linha in arq:
            registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, nome_do_curso = linha.strip().split(";")

            atributos = {
            "dias_da_semana": dias_da_semana,
            "horarios_inicio": horarios_inicio,
            "curso": nome_do_curso
            }

        arq.close()

# Trazer as mensagens de erro, sucesso aqui na função
def executa(db_prof_disc, db_professores, db_disciplinas, path):
    carregar_dados(db_prof_disc, path)
    while True:
        opt = submenu_prof_disc()

        if opt == 1:
            listar_todos(db_prof_disc)
        elif opt == 2:
            listar_atributos(db_prof_disc)
        elif opt == 3:
            inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas)
        elif opt == 4:
            alterar_cadastro(db_prof_disc)
        elif opt == 5:
            excluir_cadastro(db_prof_disc)
        elif opt == 6:
            gravar_dados(db_prof_disc, path)
            return

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

def incluir_dados(db_prof_disc, registro, sigla_disciplina, ano, semestre):
    dias_da_semana = input("Digite os Dias da Semana (separados por vírgula): ").split(", ")
    horarios_inicio = input("Digite os Horários do curso (separados por vírgula): ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")

    db_prof_disc[registro][(sigla_disciplina, ano, semestre)] = {
    "dias_da_semana": dias_da_semana,
    "horarios_inicio": horarios_inicio,
    "curso": nome_do_curso
    }

def inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas):
    registro = entrada_registro(db_professores)
    if not registro:
        return -1 # Registro não existente no db_professores
    
    db_prof_disc[registro] = {}

    sigla, ano, semestre = entrada_chaves(db_disciplinas)
    if not (sigla and ano and semestre):
        return -2 # Sigla não existente no db_disciplinas
    
    if (sigla, ano, semestre) not in db_prof_disc[registro]:
        incluir_dados(db_prof_disc, registro, sigla, ano, semestre)
        return 1 # Cadastrado com sucesso no db_prof_disc
    return 0 # Cadastro já existe no prof_disc
   
def listar_todas_aulas(db_prof_disc):
    print("Todas as aulas cadastradas por professor:\n")
    for registro in db_prof_disc:
        print(f"{'-' * 30}")
        print(f"Registro Funcional do Professor: {registro}")
        listar_atributos_aula(db_prof_disc, registro)

def listar_atributos_aula(db_prof_disc, registro=None):
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
        return True # Tudo ocorreu bem
    else:
        return False # Registro não encontrado no db_prof_disc

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
            print("Erro: Essa sigla da disciplina não consta no banco de dados de disciplinas.")
    elif mostrar_mensagens:
        print("Erro: Esse registro funcional não consta no banco de dados de professores.")
    
    return None, None

# Melhorar essas duas funçoes
def alterar_cadastro(db_prof_disc):
    registro, conjunto_chaves = existe_dados(db_prof_disc)

    if registro and conjunto_chaves:
        print("\nAtualize os dados:\n")

        if confirmar('alterar'):
            incluir_dados(db_prof_disc, registro, *conjunto_chaves)
            return 1 # Alterado com sucesso!
        else:
            return -1 # Alteração cancelada com sucesso!
    return 0 # Registro ou Conjunto Chaves não existe

def remover_prof_disc(db_prof_disc):
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

# def alterar_cadastro(db_prof_disc):
#     registro = entrada_registro()
#     if registro:
#         conjunto_chaves = entrada_chaves()
        
#         if conjunto_chaves in db_prof_disc[registro]:
#             print("\nAtualize os dados:\n")

#             if confirmar('alterar'):
#                 incluir_dados(db_prof_disc, registro, *conjunto_chaves, novo_cadastro=False)

#                 return 1 # Alterado com sucesso!
#             return 0 # Alteração cancelada!
#         return -2 # Conjuntos chaves não existe
#     return -1 # Registro não existe

# def remover_prof_disc(db_prof_disc):
#     registro = entrada_registro()
#     if registro:
#         conjunto_chaves = entrada_chaves()
        
#         if conjunto_chaves in db_prof_disc[registro]:

#             if confirmar('excluir'):
#                 if len(db_prof_disc[registro]) > 1:
#                     del db_prof_disc[registro][conjunto_chaves]
#                 else:
#                     del db_prof_disc[registro]

#                 return 1 # Excluido com sucesso!
#             return 0 # Exclusão Cancelada
#         return -2 # Conjuntos chaves não existe
#     return -1 # Registro não existe
    
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

def carregar_dados(db_prof_disc, path):
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

def executa(db_prof_disc, db_professores, db_disciplinas, path):
    while True:
        opt = submenu_prof_disc()

        if opt == 1:
            listar_todas_aulas(db_prof_disc)

        elif opt == 2:
            if not listar_atributos_aula(db_prof_disc):
                print("Erro: Essa aula não está registrada no banco de dados!")

        # Pensar em alguma solução melhor que essa (Se tiver como...)
        elif opt == 3:
            retorno = inserir_prof_disc(db_prof_disc, db_professores, db_disciplinas)
            if retorno == 1:
                print("Aula cadastrada com sucesso.")
            elif retorno == -1:
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")
            elif retorno == -2:
                print("Erro: Essa sigla da disciplina não consta no banco de dados de disciplinas.")
            else:
                print("Erro: Já existe um cadastrado dessa aula no banco de dados.")

        elif opt == 4:
            retorno = alterar_cadastro(db_prof_disc)
            if retorno == 1:
                print("Dados da aula alterado com sucesso.")
            elif retorno == -1:
                print("Alteração cancelada!")
            else:
                print("Erro:")

        elif opt == 5:
            retorno = remover_prof_disc(db_prof_disc)
            if retorno == 1:
                print("Aula removida com sucesso.")
            elif retorno == -1:
                print("Remoção cancelada!")
            else:
                print("Erro:")
                
        elif opt == 6:
            gravar_dados(db_prof_disc, path)
            return

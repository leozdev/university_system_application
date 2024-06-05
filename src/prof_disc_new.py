import os
from src.auxiliar import existe_arquivo, confirmar

def entrada_registro():
    registro = input("Digite o Registro Funcional: ")
    return registro

def entrada_chaves():
    sigla = input("Digite a Sigla da Disciplina: ")
    ano = input("Digite o Ano: ")
    semestre = input("Digite o Semestre: ")
    return [sigla, ano, semestre]

def incluir_dados(db_prof_disc, registro, conjunto_chaves, dias_da_semana, horarios_inicio, nome_do_curso):
    sigla_disciplina, ano, semestre = conjunto_chaves

    db_prof_disc[registro][(sigla_disciplina, ano, semestre)] = {
    "dias_da_semana": dias_da_semana,
    "horarios_inicio": horarios_inicio,
    "curso": nome_do_curso
    }

def inserir_prof_disc(db_prof_disc, registro, conjunto_chaves):
    db_prof_disc[registro] = {}
    sigla, ano, semestre = conjunto_chaves
    
    # Fazer a verificação dos dados
    
    if (sigla, ano, semestre) not in db_prof_disc[registro]:
        incluir_dados(db_prof_disc, registro, sigla, ano, semestre)
        return 1 # Cadastrado com sucesso no db_prof_disc
    return 0 # Cadastro já existe no prof_disc
   
   
###############################################################################
# def existe_dados(db_prof_disc, db_professores, db_disciplinas):
#     registro = entrada_registro(db_professores)
#     if registro:
#         sigla, ano, semestre = entrada_chaves(db_disciplinas)
#         if sigla and ano and semestre:
#             if (sigla, ano, semestre) in db_prof_disc[registro]:
#                 return registro, (sigla, ano, semestre)

def existe_dados(db_prof_disc, db_professores, db_disciplinas, registro, conjunto_chaves):
    if registro in db_professores and registro in db_prof_disc:
        sigla, ano, semestre = conjunto_chaves

        if sigla in db_disciplinas and conjunto_chaves in db_prof_disc[registro]:
            ...

###############################################################################

################
def alterar_cadastro(db_prof_disc):
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

def executa(db_prof_disc, db_professores, db_disciplinas, path):
    while True:
        opt = submenu_prof_disc()

        if opt == 3:
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
            return

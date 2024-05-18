import os

'''
database1 (dict): professores-disciplinas
database2 (dict): professores
database3 (dict): disciplinas
'''
# Refatorar para o tipo Arquivos... 
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

def entrada_registro():
    return input("Digite o Registro Funcional: ")

def entrada_sigla_disciplina():
    return input("Digite a Sigla da Disciplina: ")

def entrada_chaves():
    ano = input("Digite o Ano: ")
    semestre = input("Digite o Semestre: ")
    return ano, semestre

def entrada_atributos():
    dias_da_semana = input("Digite os Dias da Semana: (separados por vírgula) ").split(", ")
    horarios_do_curso = input("Digite os Horários do curso: (separados por vírgula) ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")
    return dias_da_semana, horarios_do_curso, nome_do_curso

def incluir(database1, database2, database3):
    registro = entrada_registro()

    if registro in database2:
        sigla_disciplina = entrada_sigla_disciplina()

        if sigla_disciplina in database3:
            ano, semestre, dias_da_semana, horarios_inicio, curso = *entrada_chaves(), *entrada_atributos()

            if registro not in database1:
                database1[registro] = {}
            
            if (sigla_disciplina, ano, semestre) in database1[registro]:
                print("Esses dados já estão cadastrados!")
                return
            
            database1[registro][(sigla_disciplina, ano, semestre)] = {
                "dias_da_semana": dias_da_semana,
                "horarios_inicio": horarios_inicio,
                "curso": curso
                }
            
            print("Cadastro adicionado com sucesso.")
        else:
            print("Não foi possível encontrar essa disciplina no banco de dados.")
    else:
        print("Não foi possível encontrar esse registro no banco de dados.")

def listar_todos(database1):
    for registro in database1:
        listar_atributos(database1, registro)

def listar_atributos(database1, registro=None):

    if registro is None:
        registro = entrada_registro()

    if registro in database1:
        print("Registro:", registro)

        # conjunto_chaves 'tuple': Um conjunto de chaves
        for conjunto_chaves, atributos in database1[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves
        
            print("Sigla da disciplina:", sigla_disciplina)
            print("Ano:", ano)
            print("Semestre:", semestre)
            print("Dias da Semana:", ", ".join(atributos["dias_da_semana"]))
            print("Horários de início", ", ".join(atributos["horarios_inicio"]))
            print("Curso:", atributos["curso"])
            print()

    else:
        print(f"O registro não foi encontrado no banco de dados.")
  
# Melhorar essa função
def cruzar_dados(database1):
    registro = entrada_registro()

    if registro in database1:
        conjunto_chaves = (input("Digite a Sigla da Disciplina: "), input("Digite o Ano: "), input("Digite o Semestre: "))

        if conjunto_chaves in database1[registro]:
            return registro, conjunto_chaves
        
        else:
            print("Dados não encontrado.")

    else:
        print("Registro não encontrado no banco de dados.")
    return None, None

def confirmar():
    while True:
        input_confirma = input("Tem certeza que deseja excluir? (S/N): ").upper()
        if input_confirma == "S":
            return True
        elif input_confirma == "N":
            return False
        else:
            print("Opção inválida!")

def excluir_cadastro(database1):
    registro, conjunto_chaves = cruzar_dados(database1)

    if registro and conjunto_chaves:
        if confirmar():

            if len(database1[registro]) > 1:
                del database1[registro][conjunto_chaves]
            else:
                del database1[registro]

            print("Cadastro excluído com sucesso.")
        else:
            print("Exclusão cancelada!")


def alterar_cadastro(database1):
    registro, conjunto_chaves = cruzar_dados(database1)

    if registro and conjunto_chaves:
        # Melhorar frase
        print("\nAtualize os dados:\n")
        dias, horarios, nome_curso = entrada_atributos()

        database1[registro][conjunto_chaves]["dias_da_semana"] = horarios
        database1[registro][conjunto_chaves]["horarios_inicio"] = dias
        database1[registro][conjunto_chaves]["curso"] = nome_curso

        print("Cadastro alterado com sucesso.")

def executa(database1, database2, database3):
    while True:
        opt = submenu_prof_disc()
        
        funcoes = {
            1:listar_todos,
            2:listar_atributos,
            4:alterar_cadastro,
            5:excluir_cadastro
        }
        
        if opt in funcoes:
            funcoes[opt](database1)
        
        elif opt == 3:
            incluir(database1, database2, database3)
        
        elif opt == 6:
            return

import os
from src.auxiliar import existe_arquivo

"""
database1 (dict): professores-disciplinas
database2 (dict): professores
database3 (dict): disciplinas
"""

# BRECANDO SO NO FINAL -> ARRUMAR
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

def entrada_registro(database2):
    registro = input("Digite o Registro Funcional: ")
    if registro in database2:
        return registro
    else:
        print("O registro não foi encontrado no banco de dados.")
        return None

def entrada_chaves(database3):
    sigla = input("Digite a Sigla da Disciplina: ")
    if sigla in database3:
        ano = input("Digite o Ano: ")
        semestre = input("Digite o Semestre: ")
        return sigla, ano, semestre
    else:
        print("A disciplina não foi encontrada no banco de dados.")
        return None, None, None

def entrada_atributos():
    dias_da_semana = input("Digite os Dias da Semana (separados por vírgula): ").split(", ")
    horarios_do_curso = input("Digite os Horários do curso (separados por vírgula): ").split(", ")
    nome_do_curso = input("Digite o Nome do Curso: ")
    return dias_da_semana, horarios_do_curso, nome_do_curso

def incluir(database1, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, curso):  
    if registro not in database1:
        database1[registro] = {}

    # Conjunto chaves = (sigla_disciplina, ano, semestre) -> Tupla (tuple)
    if (sigla_disciplina, ano, semestre) not in database1[registro]:
        database1[registro][(sigla_disciplina, ano, semestre)] = {
            "dias_da_semana": dias_da_semana,
            "horarios_inicio": horarios_inicio,
            "curso": curso
        }
        return True
    return False

def incluir_cadastro(database1, database2, database3):
    registro = entrada_registro(database2)
    if registro:
        sigla, ano, semestre = entrada_chaves(database3)
        if sigla and ano and semestre:
            atributos = entrada_atributos()
            if incluir(database1, registro, sigla, ano, semestre, *atributos):
                print("Dados cadastrados com sucesso!")
            else:
                print("Esses dados já estão cadastrados!")

def listar_todos(database1):
    print("Todos os dados cadastrados:\n")
    for registro in database1:
        print("-" * 30)
        print("Registro Funcional do Professor:", registro)
        listar_atributos(database1, registro)

def listar_atributos(database1, registro=None):
    if registro is None:
        registro = input("Digite o Registro Funcional: ")

    if registro in database1:
        for conjunto_chaves, atributos in database1[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves
            print("\nSigla da disciplina:", sigla_disciplina)
            print("Ano:", ano)
            print("Semestre:", semestre)
            print("Dias da Semana:", ", ".join(atributos["dias_da_semana"]))
            print("Horários de início:", ", ".join(atributos["horarios_inicio"]))
            print("Curso:", atributos["curso"])
    else:
        print("Registro não encontrado.")

def existe_dados(database1):
    registro = input("Digite o Registro Funcional: ")
    if registro in database1:
        sigla = input("Digite a Sigla da Disciplina: ")
        ano = input("Digite o Ano: ")
        semestre = input("Digite o Semestre: ")
        if (sigla, ano, semestre) in database1[registro]:
            return registro, (sigla, ano, semestre)
        else:
            print("Dados não encontrados.")
    else:
        print("Registro não encontrado no banco de dados.")
    return None, None

def confirmar(acao):
    while True:
        input_confirma = input(f"Tem certeza que deseja {acao} o cadastro? (S/N): ").upper()
        if input_confirma == "S":
            return True
        elif input_confirma == "N":
            return False
        else:
            print("Opção inválida!")

def excluir_cadastro(database1):
    registro, conjunto_chaves = existe_dados(database1)
    if registro and conjunto_chaves:
        if confirmar('excluir'):
            if len(database1[registro]) > 1:
                del database1[registro][conjunto_chaves]
            else:
                del database1[registro]
            print("Cadastro excluído com sucesso.")
        else:
            print("Exclusão cancelada!")

# Falta confirmar alteraração
def alterar_cadastro(database1):
    registro, conjunto_chaves = existe_dados(database1)
    if registro and conjunto_chaves:
        print("\nAtualize os dados:\n")
        dias, horarios, curso = entrada_atributos()
        database1[registro][conjunto_chaves]["dias_da_semana"] = dias
        database1[registro][conjunto_chaves]["horarios_inicio"] = horarios
        database1[registro][conjunto_chaves]["curso"] = curso
        print("Cadastro alterado com sucesso.")

def gravar_dados(database1, path):
    arq =  open(path, "w", encoding="utf-8")

    for registro in database1:
        for conjunto_chaves, atributos in database1[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves
            linha = (f"{registro};{sigla_disciplina};{ano};{semestre};{','.join(atributos['dias_da_semana'])};{','.join(atributos['horarios_inicio'])};{atributos['curso']}\n")
            arq.write(linha)
    arq.close()

def carregar_dados(database1, path):
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")

        for linha in arq:
            linha = linha.strip().split(";")
            registro = linha[0]
            sigla_disciplina = linha[1]
            ano = linha[2]
            semestre = linha[3]
            dias_da_semana = linha[4].split(',')
            horarios_inicio = linha[5].split(',')
            curso = linha[6]
            incluir(database1, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, curso)

        arq.close()
    
def executa(database1, database2, database3, path):
    carregar_dados(database1, path)
    while True:
        opt = submenu_prof_disc()
        funcoes = {
            1: listar_todos,
            2: listar_atributos,
            4: alterar_cadastro,
            5: excluir_cadastro
        }
        if opt in funcoes:
            funcoes[opt](database1)
        elif opt == 3:
            incluir_cadastro(database1, database2, database3)
        elif opt == 6:
            gravar_dados(database1, path)
            return

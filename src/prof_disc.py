import os
from src.auxiliar import existe_arquivo, confirmar

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

def entrada_registro(db_professores):
    registro = input("Digite o Registro Funcional: ")
    if registro in db_professores:
        return registro
    else:
        print("O registro não foi encontrado no banco de dados.")
        return None

def entrada_chaves(db_disciplinas):
    sigla = input("Digite a Sigla da Disciplina: ")
    if sigla in db_disciplinas:
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

def incluir(db_prof_disc, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, curso):  
    if registro not in db_prof_disc:
        db_prof_disc[registro] = {}

    # Conjunto chaves = (sigla_disciplina, ano, semestre) -> Tupla (tuple)
    if (sigla_disciplina, ano, semestre) not in db_prof_disc[registro]:
        db_prof_disc[registro][(sigla_disciplina, ano, semestre)] = {
            "dias_da_semana": dias_da_semana,
            "horarios_inicio": horarios_inicio,
            "curso": curso
        }
        return True
    return False

def incluir_cadastro(db_prof_disc, db_professores, db_disciplinas):
    registro = entrada_registro(db_professores)
    if registro:
        sigla, ano, semestre = entrada_chaves(db_disciplinas)
        if sigla and ano and semestre:
            atributos = entrada_atributos()
            if incluir(db_prof_disc, registro, sigla, ano, semestre, *atributos):
                print("Dados cadastrados com sucesso!")
            else:
                print("Esses dados já estão cadastrados!")

def listar_todos(db_prof_disc):
    print("Todos os dados cadastrados:\n")
    for registro in db_prof_disc:
        print("-" * 30)
        print("Registro Funcional do Professor:", registro)
        listar_atributos(db_prof_disc, registro)

def listar_atributos(db_prof_disc, registro=None):
    if registro is None:
        registro = input("Digite o Registro Funcional: ")

    if registro in db_prof_disc:
        for conjunto_chaves, atributos in db_prof_disc[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves
            print()
            listar_atributos_especifico(db_prof_disc, registro, sigla_disciplina, ano, semestre)
    else:
        print("Registro não encontrado.")

def listar_atributos_especifico(db_prof_disc, registro, sigla, ano, semestre):
    atributos = db_prof_disc[registro][(sigla, ano, semestre)]
    print("Sigla da disciplina:", sigla)
    print("Ano:", ano)
    print("Semestre:", semestre)
    print("Dias da Semana:", ", ".join(atributos["dias_da_semana"]))
    print("Horários de início:", ", ".join(atributos["horarios_inicio"]))
    print("Curso:", atributos["curso"])

def existe_dados(db_prof_disc):
    registro = input("Digite o Registro Funcional: ")
    if registro in db_prof_disc:
        sigla = input("Digite a Sigla da Disciplina: ")
        ano = input("Digite o Ano: ")
        semestre = input("Digite o Semestre: ")
        if (sigla, ano, semestre) in db_prof_disc[registro]:
            return registro, (sigla, ano, semestre)
        else:
            print("Dados não encontrados.")
    else:
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
            print("Cadastro excluído com sucesso.")
        else:
            print("Exclusão cancelada!")

# Falta confirmar alteraração
def alterar_cadastro(db_prof_disc):
    registro, conjunto_chaves = existe_dados(db_prof_disc)
    if registro and conjunto_chaves:
        print("\nAtualize os dados:\n")
        dias, horarios, curso = entrada_atributos()
        db_prof_disc[registro][conjunto_chaves]["dias_da_semana"] = dias
        db_prof_disc[registro][conjunto_chaves]["horarios_inicio"] = horarios
        db_prof_disc[registro][conjunto_chaves]["curso"] = curso
        print("Cadastro alterado com sucesso.")

def gravar_dados(db_prof_disc, path):
    arq =  open(path, "w", encoding="utf-8")

    for registro in db_prof_disc:
        for conjunto_chaves, atributos in db_prof_disc[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves
            linha = (f"{registro};{sigla_disciplina};{ano};{semestre};{','.join(atributos['dias_da_semana'])};{','.join(atributos['horarios_inicio'])};{atributos['curso']}\n")
            arq.write(linha)
    arq.close()

def carregar_dados(db_prof_disc, path):
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
            incluir(db_prof_disc, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, curso)

        arq.close()
    
def executa(db_prof_disc, db_professores, db_disciplinas, path):
    carregar_dados(db_prof_disc, path)
    while True:
        opt = submenu_prof_disc()
        funcoes = {
            1: listar_todos,
            2: listar_atributos,
            4: alterar_cadastro,
            5: excluir_cadastro
        }
        if opt in funcoes:
            funcoes[opt](db_prof_disc)
        elif opt == 3:
            incluir_cadastro(db_prof_disc, db_professores, db_disciplinas)
        elif opt == 6:
            gravar_dados(db_prof_disc, path)
            return

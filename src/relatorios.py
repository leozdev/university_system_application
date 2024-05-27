import os
import src.professores as professores
import src.disciplinas as disciplinas
import src.prof_disc as prof_disc

# !!!REFATORAR ESSE CÓDIGO!!!

def submenu_relatorios():
    """
    Exibe um submenu para o gerenciamento dos relatórios.

    Return:
        int: A opção selecionada pelo usuário.
    """
    while True:
        input("\nPressione [enter] para continuar...")
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu de Gerenciamento de Relatórios ---")
        print("1 - Mostrar dados de professores por titulação.")
        print("2 - Mostrar dados de disciplinas com mais de X créditos.")
        print("3 - Mostrar dados de disciplinas das Terças e Quintas.")
        print("4 - Voltar")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 4:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 4.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Melhorar mais... textos, inputs, chamadas, parametros, impressao, função (modularizar)

def buscar_professores_titulacao(db_professores):
    det_titulacao = input("Informe a titulação a ser listada (Mestrado ou Doutorado): ").lower()
    existe = False
    for registro in db_professores:
        if db_professores[registro]['titulacao'].lower() == det_titulacao:
            existe = True
            print("-" * 30)
            print("Registro Funcional:", registro)
            professores.listar_atributos(db_professores, registro)
    if not existe:
        print("Não existe nenhum cadastro com essa titulação!") 

def buscar_disciplina_creditos(db_disciplinas):
    min_creditos = float(input("Informe a quantidade de créditos da disciplina a ser listada: "))
    print("Disciplinas com mais de", min_creditos, "créditos:\n")
    existe = False
    for sigla in db_disciplinas:
        if float(db_disciplinas[sigla]['n_creditos']) > min_creditos:
            existe = True
            disciplinas.mostra_disciplina(db_disciplinas, sigla)
            print()
    if not existe:
        print("Não existe nenhuma disciplina com essa quantidade mínima de créditos!") 

def buscar_disciplina_dias(db_prof_disc, db_professores, db_disciplinas):
    print("Disciplinas ministradas às terças e quintas-feiras:\n")
    existe = False
    for registro in db_prof_disc:
        for conjunto_chaves, atributos in db_prof_disc[registro].items():
            sigla, ano, semestre = conjunto_chaves

            if "Terça" in atributos["dias_da_semana"] and "Quinta" in atributos["dias_da_semana"]:
                existe = True
                print(f"\nRegistro Funcional: {registro}\n"
                      f"Nome do Professor: {db_professores[registro]['nome']}\n"
                      f"Nome da Disciplina: {db_disciplinas[sigla]['nome']}")
                prof_disc.listar_atributos_especifico(db_prof_disc, registro, sigla, ano, semestre)
                
    if not existe:
        print("Não existem disciplinas ministradas às terças e quintas-feiras!")

# def buscar_disciplina_dias(database1, database2, database3):
#     print("Disciplinas ministradas às terças e quintas-feiras:\n")
#     existe = False
#     for registro_prof, prof_disc in database1.items():
#         for (sigla_disciplina, _, _), atributos in prof_disc.items():
#             if "Terça-feira" in atributos["dias_da_semana"] and "Quinta-feira" in atributos["dias_da_semana"]:
#                 existe = True
#                 print("-" * 30)
#                 print("Registro Funcional do Professor:", registro_prof)
#                 print("Nome do Professor:", database2[registro_prof]["nome"])
#                 print("Sigla da Disciplina:", sigla_disciplina)
#                 print("Nome da Disciplina:", database3[sigla_disciplina]["nome"])
#                 print("Dias da Semana:", ", ".join(atributos["dias_da_semana"]))
#                 print("Horários de início:", ", ".join(atributos["horarios_inicio"]))
#                 print("Curso:", atributos["curso"])
#     if not existe:
#         print("Não existem disciplinas ministradas às terças e quintas-feiras!")

def gravar_dados():
    ...

def carregar_dados():
    ...

def executa(db_prof_disc, db_professores, db_disciplinas):

    while True:
        opt = submenu_relatorios()

        if opt == 1:
            buscar_professores_titulacao(db_professores)
        elif opt == 2: 
            buscar_disciplina_creditos(db_disciplinas)
        elif opt == 3:
            buscar_disciplina_dias(db_prof_disc, db_professores, db_disciplinas)
        elif opt == 4:
            # gravar_dados()
            return
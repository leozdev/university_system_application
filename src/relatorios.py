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

def buscar_professores_titulacao(db_professores):
    path = "relatorios\\relatorio_professores_titulacao.txt"
    det_titulacao = input("Informe a titulação a ser listada (Mestrado ou Doutorado): ").lower()

    existe = False
    for registro in db_professores:
        if db_professores[registro]['titulacao'].lower() == det_titulacao:
            existe = True
            atributos = db_professores[registro]
            dados = (f"{'-' * 30}\n"
                     f"Registro Funcional: {registro}\n"
                     f"Nome: {atributos['nome']}\n"
                     f"Data de Nascimento: {atributos['data-nascimento']}\n"
                     f"Sexo: {atributos['sexo']}\n"
                     f"Área de Pesquisa: {atributos['area-de-pesquisa']}\n"
                     f"Titulação: {atributos['titulacao']}\n"
                     f"Graduação: {atributos['graduacao']}\n"
                     f"E-mails: {', '.join(atributos['emails'])}\n"
                     f"Telefones: {', '.join(atributos['telefones'])}")
            gravar_dados(path, dados)
            return True
    if not existe:
        return False

def buscar_disciplina_creditos(db_disciplinas):
    path = "relatorios\\relatorio_disciplina_creditos.txt"
    min_creditos = float(input("Informe a quantidade de créditos da disciplina a ser listada: "))
    
    existe = False
    for sigla in db_disciplinas:
        if float(db_disciplinas[sigla]['n_creditos']) > min_creditos:
            existe = True
            atributos = db_disciplinas[sigla]
            dados = (f"{'-' * 30}\n"
                     f"Sigla da Disciplina: {sigla}\n"
                     f"Nome da Disiciplina: {atributos['nome']}\n"
                     f"Ementa: {atributos['ementa']}\n"
                     f"Bibliografia: {atributos['bibliografia']}\n"
                     f"Número de Créditos: {atributos['n_creditos']}\n"
                     f"Carga Horária: {atributos['carga_horaria']}\n")
            gravar_dados(path, dados)
            return True
        
    if not existe:
        return False

def buscar_disciplina_dias(db_prof_disc, db_professores, db_disciplinas):
    path = "relatorios\\relatorio_disciplinas_dias.txt"

    print("Disciplinas ministradas às terças e quintas-feiras:\n")
    existe = False
    for registro in db_prof_disc:
        for conjunto_chaves, atributos in db_prof_disc[registro].items():
            sigla, ano, semestre = conjunto_chaves

            if "Terça" in atributos["dias_da_semana"] and "Quinta" in atributos["dias_da_semana"]:
                existe = True
                dados = (f"{'-' * 30}\n"
                        f"Registro Funcional: {registro}\n"
                        f"Nome do Professor: {db_professores[registro]['nome']}\n"
                        f"Nome da Disciplina: {db_disciplinas[sigla]['nome']}\n"
                        f"Sigla da Disciplina: {sigla}\n"
                        f"Ano: {ano}\n"
                        f"Semestre: {semestre}\n"
                        f"Dias da Semana: {', '.join(atributos['dias_da_semana'])}\n"
                        f"Horários de Início: {', '.join(atributos['horarios_inicio'])}\n"
                        f"Curso: {atributos['curso']}\n")
                gravar_dados(path, dados)
                return True
            
    if not existe:
        return False

def gravar_dados(path, dados):
    arq = open(path, "w", encoding="utf-8")
    arq.write(dados)
    arq.close

def executa(db_prof_disc, db_professores, db_disciplinas):

    while True:
        opt = submenu_relatorios()

        if opt == 1:
            if buscar_professores_titulacao(db_professores):
                print("Relatório gerado com sucesso!")
            else:
                print("Não existe nenhum cadastro com essa titulação!") 

        elif opt == 2: 
            if buscar_disciplina_creditos(db_disciplinas):
                print("Relatório gerado com sucesso!")
            else:
                print("Não existe nenhuma disciplina com essa quantidade mínima de créditos!") 

        elif opt == 3:
            if buscar_disciplina_dias(db_prof_disc, db_professores, db_disciplinas):
                print("Relatório gerado com sucesso!")
            else:
                print("Não existem disciplinas ministradas às terças e quintas-feiras!")

        elif opt == 4:
            return
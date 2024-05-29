import os
from datetime import datetime

def escrever_cabecalho_relatorio(arq, titulo, subtitulo):
    cabecalho = (f"======================== Relatório  ========================\n"
                 f"{titulo}\n"
                 f"============================================================\n"
                 f"{subtitulo}\n")
    arq.write(cabecalho)

def escrever_rodape_relatorio(arq):
    data_hora_formatada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    rodape = (f"\n============================================================\n"
              f"Relatório gerado em: {data_hora_formatada}\n"
              f"============================================================\n")
    arq.write(rodape)

def buscar_professores_titulacao(db_professores, det_titulacao, path_relatorio_titulacoes):
    arq = open(path_relatorio_titulacoes, "w", encoding="utf-8")
    existe = False
  
    escrever_cabecalho_relatorio(arq, titulo=f"Professores com a titulação '{det_titulacao}'", subtitulo="Professores:")

    for registro in db_professores:
        if db_professores[registro]['titulacao'] == det_titulacao:
            existe = True
            atributos = db_professores[registro]

            dados = (f"\n\tRegistro Funcional: {registro}\n"
                     f"\tNome: {atributos['nome']}\n"
                     f"\tData de Nascimento: {atributos['data-nascimento']}\n"
                     f"\tSexo: {atributos['sexo']}\n"
                     f"\tÁrea de Pesquisa: {atributos['area-de-pesquisa']}\n"
                     f"\tTitulação: {atributos['titulacao']}\n"
                     f"\tGraduação: {atributos['graduacao']}\n"
                     f"\tE-mails: {', '.join(atributos['emails'])}\n"
                     f"\tTelefones: {', '.join(atributos['telefones'])}\n"
                     f"\t{'_' * 30}\n")
            arq.write(dados)

    escrever_rodape_relatorio(arq)

    arq.close()
    return existe

def buscar_disciplina_creditos(db_disciplinas, min_creditos, path_relatorio_creditos):
    existe = False
    
    arq = open(path_relatorio_creditos, "w", encoding="utf-8")

    escrever_cabecalho_relatorio(arq, titulo=f"Disciplinas com mais de {min_creditos} créditos", subtitulo="Disciplinas:")

    for sigla in db_disciplinas:
        if float(db_disciplinas[sigla]['n_creditos']) > min_creditos:
            existe = True
            atributos = db_disciplinas[sigla]

            dados = (f"\n\tSigla da Disciplina: {sigla}\n"
                     f"\tNome da Disciplina: {atributos['nome']}\n"
                     f"\tEmenta: {atributos['ementa']}\n"
                     f"\tBibliografia: {atributos['bibliografia']}\n"
                     f"\tNúmero de Créditos: {atributos['n_creditos']}\n"
                     f"\tCarga Horária: {atributos['carga_horaria']}\n"
                     f"\t{'_' * 30}\n")
            arq.write(dados)

    escrever_rodape_relatorio(arq)

    arq.close()
    return existe

def buscar_disciplina_dias(db_prof_disc, db_professores, db_disciplinas, path_relatorio_dias):
    existe = False
    
    arq = open(path_relatorio_dias, "w", encoding="utf-8")

    escrever_cabecalho_relatorio(arq, titulo=f"Disciplinas que serão ministradas às terças-feiras e às quintas-feiras", subtitulo="Informações:")

    for registro in db_prof_disc:
        for conjunto_chaves, atributos in db_prof_disc[registro].items():
            sigla, ano, semestre = conjunto_chaves

            if "Terça-Feira" in atributos["dias_da_semana"] and "Quinta-Feira" in atributos["dias_da_semana"]:
                existe = True
                dados = (f"\n\tRegistro Funcional: {registro}\n"
                         f"\tNome do Professor: {db_professores[registro]['nome']}\n"
                         f"\tNome da Disciplina: {db_disciplinas[sigla]['nome']}\n"
                         f"\tSigla da Disciplina: {sigla}\n"
                         f"\tAno: {ano}\n"
                         f"\tSemestre: {semestre}\n"
                         f"\tDias da Semana: {', '.join(atributos['dias_da_semana'])}\n"
                         f"\tHorários de Início: {', '.join(atributos['horarios_inicio'])}\n"
                         f"\tCurso: {atributos['curso']}\n"
                         f"\t{'_' * 30}\n")
                arq.write(dados)

    escrever_rodape_relatorio(arq)

    arq.close()
    return existe

def submenu_relatorios():
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

def executa(db_prof_disc, db_professores, db_disciplinas, path_relatorio_titulacoes, path_relatorio_creditos, path_relatorio_dias):
    while True:
        opt = submenu_relatorios()

        if opt == 1:
            det_titulacao = input("Informe a titulação a ser listada (Mestrado ou Doutorado): ").title()
            if buscar_professores_titulacao(db_professores, det_titulacao, path_relatorio_titulacoes):
                print("Relatório gerado com sucesso!")
            else:
                print("Não existe nenhum professor com essa titulação!") 

        elif opt == 2: 
            min_creditos = float(input("Informe a quantidade de créditos da disciplina a ser listada: "))
            if buscar_disciplina_creditos(db_disciplinas, min_creditos, path_relatorio_creditos):
                print("Relatório gerado com sucesso!")
            else:
                print("Não existe nenhuma disciplina com essa quantidade mínima de créditos!") 

        elif opt == 3:
            if buscar_disciplina_dias(db_prof_disc, db_professores, db_disciplinas, path_relatorio_dias):
                print("Relatório gerado com sucesso!")
            else:
                print("Não existem disciplinas ministradas às terças e quintas-feiras!")

        elif opt == 4:
            return

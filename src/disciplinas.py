import os
from src.auxiliar import existe_arquivo, confirmar

"""
Comentário:

    Vini, eu refatorei seu código já!

    Mudanças que eu fiz:
        - Nome das funções eu tentei deixar mais claro e um padrão comparado aos outros módulos que fizemos (prof_disc.py, relatorios.py, etc...)
        - Estrutura de retorno
        - As mensagens agora terão que ser impressas pela função que chama, tendo que tratar o valor de retorno (sendo um bool, None ou int)
    
    De maneira geral, o projeto está quase concluído. Estamos na etapa final, estou verificando cada função de cada módulo, estou refatorando bastante para melhorar
    a legibilidade do código. 

    Coisas a fazer:
        - Docstring de cada função (padrão está na main, só seguir aquele escopo)
        - Melhorar a forma como está sendo gravado o relátorio (estilizar) * Opcional mas causa uma boa impressão!
        - Testar até cansar kkkk para não ter dúvidas que tudo irá funcionar como planejamos! Principalmente agora que estou refatorando tudo de novo.

    Feedbacks da Eloiza foram mais ou menos as coisas que estou alterando...
    Qualquer dúvida com alguma mudança que eu fiz nos códigos, me pergunte para eu poder explicar a lógica
    Peço que revise também todas as funçoes e verifique se existe alguma inconsistência tbm (se tiver deixa um comentário na função, para podermos reavaliar)
    
    Demais é isso!
"""

def submenu_disciplinas():
    while True:
        input("\nPressione [enter] para continuar...")
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu de Gerenciamento de Disciplinas ---")
        print("1 - Listar Todas Disciplinas")
        print("2 - Listar uma Disciplina Específica")
        print("3 - Incluir Disciplina")
        print("4 - Alterar Dados de uma Disciplina")
        print("5 - Excluir uma Disciplina")
        print("6 - Voltar")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 6:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def incluir_dados(db_disciplinas, sigla):
    nome = input("Digite o nome da disciplina: ").title()
    ementa = input("Digite a ementa da disciplina: ").capitalize()
    bibliografia = input("Digite a bibliografia da disciplina: ").capitalize()
    n_creditos = input("Digite o número de creditos da disciplina: ")
    carga_horaria = input("Digite a carga horária da disciplina (00h): ")

    db_disciplinas[sigla] = {
    'nome': nome,
    'ementa': ementa, 
    'bibliografia': bibliografia,
    'n_creditos': n_creditos,
    'carga_horaria': carga_horaria
    }
    
def inserir_disciplina(db_disciplinas):
    sigla = input("Digite a sigla da disciplina: ")
    if sigla not in db_disciplinas:
        incluir_dados(db_disciplinas, sigla)
        return True # Dados inseridos com sucesso!
    return False # Disciplina já cadastrada!


def listar_todas_disciplinas(db_disciplinas):
    print("Todas disciplinas cadastradas:\n")
    for sigla in db_disciplinas: 
        print("-" * 30)
        print("Sigla da Disciplina:", sigla)
        listar_atributos_disciplina(db_disciplinas, sigla)

def listar_atributos_disciplina(db_disciplinas, sigla=None):
    if sigla is None:
        sigla = input("Digite a sigla da disciplina que deseja consultar: ")

    if sigla in db_disciplinas:
        atributos = db_disciplinas[sigla]
        print("\nNome:", atributos['nome'])
        print("Ementa:", atributos['ementa'])
        print("Bibliografia:", atributos['bibliografia'])
        print("Número de Créditos:", atributos['n_creditos'])
        print("Carga Horária:", atributos['carga_horaria'])
    else:
        print("Disciplina não encontrada!")

def alterar_dados_disciplina(db_disciplinas):
    sigla = input("Digite a sigla da disciplina que deseja alterar: ")
    if sigla in db_disciplinas:
        if confirmar('alterar'):
            incluir_dados(db_disciplinas, sigla)
            return 1 # Dados alterados com sucesso!
        else:
            return -1 # Alteração cancelada com sucesso!
    else:
        return 0 # Sigla não encontrada!

def remover_disciplina(db_disciplinas):
    sigla = input("Digite a sigla da disciplina que deseja remover: ")
    if sigla in db_disciplinas:
        if confirmar('excluir'):
            del db_disciplinas[sigla]
            return 1 # Dados apagados com sucesso!
        else:
            return -1 # Exclusão cancelada!
    else:
        return 0 # Disciplina não cadastrada!

def gravar_dados(db_disciplinas, path):
    arq = open(path, "w", encoding="utf-8")
    
    for sigla, atributos in db_disciplinas.items():
        linha = (f"{sigla};"
                 f"{atributos['nome']};"
                 f"{atributos['ementa']};"
                 f"{atributos['bibliografia']};"
                 f"{atributos['n_creditos']};"
                 f"{atributos['carga_horaria']}\n")
        arq.write(linha)
    arq.close()

def carregar_dados(db_disciplinas, path):
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")
        for linha in arq:
            sigla, nome, ementa, bibliografia, n_creditos, carga_horaria = linha.strip().split(";")
            db_disciplinas[sigla] = {
            'nome': nome,
            'ementa': ementa, 
            'bibliografia': bibliografia,
            'n_creditos': n_creditos,
            'carga_horaria': carga_horaria
            }

def executa(db_disciplinas, path):

    while True:
        opt = submenu_disciplinas()
        
        if opt == 1:
            listar_todas_disciplinas(db_disciplinas)

        elif opt == 2:
            listar_atributos_disciplina(db_disciplinas)

        elif opt == 3:
            if inserir_disciplina(db_disciplinas):
                print("Disciplina cadastrada com sucesso!")
            else:
                print("Erro: Já existe um cadastrado dessa sigla da disciplina no banco de dados!")

        # Pensar em alguma solução melhor que essa (Se tiver como...)
        elif opt == 4:
            retorno = alterar_dados_disciplina(db_disciplinas)
            if retorno == 1:
                print("Dados da disciplina alterado com sucesso!")
            elif retorno == -1:
                print("Você cancelou essa alteração!")
            else:
                print("Erro: Sigla da disciplina não consta no banco de dados de disciplinas!")

        elif opt == 5:
            retorno = remover_disciplina(db_disciplinas)
            if retorno == 1:
                print("Disciplina removida com sucesso!")
            elif retorno == -1:
                print("Você cancelou essa remoção!")
            else:
                print("Erro: Sigla da disciplina não consta no banco de dados de disciplinas!")
                
        elif opt == 6:
            gravar_dados(db_disciplinas, path)
            return
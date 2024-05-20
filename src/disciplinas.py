# disciplina = { 
#     'APR1' : { 
#         'nome': 'Algoritmos',
#         'ementa': 'BES', 
#         'bibliografia': 'blabla',
#         'n_creditos': '10',
#         'carga_horaria': '122h'
#     }
# }

import os
from src.auxiliar import *

def existe_disciplina(dic,sigla):
    if sigla in dic.keys():
        return True
    else:
        return False
    
    
def insere_disciplina(dic):

    sigla = input("Digite a sigla da disciplina: ")

    
    if existe_disciplina(dic,sigla):
        print("Disciplina já cadastrada!")
        input("Tecle <ENTER> para continuar...\n")
        
    else:
        nome = input("Digite o nome da disciplina: ")
        ementa = input("Digite a ementa da disciplina: ")
        bibliografia = input("Digite a bibliografia da disciplina: ")
        n_creditos = input("Digite o número de creditos da disciplina: ")
        carga_horaria = input("Digite a carga horaria da disciplina: ")

        dic[sigla] = {
        'nome': nome,
        'ementa': ementa, 
        'bibliografia': bibliografia,
        'n_creditos': n_creditos,
        'carga_horaria': carga_horaria
        }

        print("Dados inseridos com sucesso!")


def mostra_disciplina(dic, sigla=None):
    if sigla is None:
        sigla = input("Digite a sigla da disciplina que deseja consultar: ")

    if existe_disciplina(dic, sigla):
        dados = dic[sigla]
        print("Nome:", dados['nome'])
        print("Ementa:", dados['ementa'])
        print("Bibliografia:", dados['bibliografia'])
        print("Número de Créditos:", dados['n_creditos'])
        print("Carga Horária:", dados['carga_horaria'])
    else:
        print("Disciplina não encontrada!")

def mostra_td_disciplinas(dic):

    print("Todas disciplinas\n")
    for sigla in dic: 
        print("Sigla da Disciplina:", sigla)
        mostra_disciplina(dic, sigla)
        print()


def altera_disciplina(dic):
    sigla = input("Digite a sigla da disciplina que deseja alterar: ")
    
    if existe_disciplina(dic,sigla):
        confirma = input("Tem certeza que deseja alterar? (S/N): ").upper()
        
        if confirma == 'S':
            nome = input("Digite o nome da disciplina: ")
            ementa = input("Digite a ementa da disciplina: ")
            bibliografia = input("Digite a bibliografia da disciplina: ")
            n_creditos = input("Digite o número de creditos da disciplina: ")
            carga_horaria = input("Digite a carga horaria da disciplina: ")

            dic[sigla] = {
            'nome': nome,
            'ementa': ementa, 
            'bibliografia': bibliografia,
            'n_creditos': n_creditos,
            'carga_horaria': carga_horaria
            }
            
            print("Dados alterados com sucesso!")
            
        else:
            print("Alteração cancelada!")

    else:
        print("Disciplina não foi encontrada!")


def remove_disciplina(dic):
    sigla = input("Digite a sigla da disciplina que deseja remover: ")

    if existe_disciplina(dic,sigla):
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
        if confirma == 'S':
            del dic[sigla]
            print("Dados apagados com sucesso!")
            
        else:
            print("Exclusão cancelada!")

    else:

        print("Disciplina não cadastrada!")


def relatorio(dic, n):
    print("Disciplinas com mais de", n, "créditos:\n")
    print("SIGLA - NOME - EMENTA - BIBLIOGRAFIA - NUM DE CREDITOS - CARGA HORARIA\n")
    
    for codigo, dados in dic.items():
        num_creditos = int(dados['n_creditos'])
        if num_creditos > n:
            linha = codigo + " - " + dados['nome'] + " - " + dados['ementa'] + " - " + dados['bibliografia'] + " - " + dados['n_creditos'] + " - " + dados['carga_horaria'] + "\n"
            print(linha)
    
    print("")


def grava_disciplinas(dic, path):
    arq = open(path, "w", encoding="utf-8")
    
    for sigla in dic:
        info = dic[sigla]
        # Monta linha para gravação:
        linha = sigla + ";" + info['nome'] + ";" + info['ementa'] + ";" + info['bibliografia'] + ";" + info['n_creditos'] + ";" + info['carga_horaria'] + "\n"

        # Grava no arquivo:
        arq.write(linha)

    # Fecha o arquivo:
    arq.close()


def recupera_disciplinas(dic, path):

    # Verificando se o arquivo existe:
    if ( existe_arquivo(path) ):

        # Existe! Abrindo arquivo para leitura:
        arq = open(path, "r", encoding="utf-8")

        # Percorrendo as linhas do arquivo:
        for linha in arq:

            # Tirando o \n do final:
            linha = linha[:len(linha)-1]
            
            # Vamos quebrar por ;
            lista = linha.split(";")
        
            sigla = lista[0]
            nome = lista[1]
            ementa = lista[2]
            bibliografia = lista[3]
            n_creditos = lista[4]
            carga_horaria = lista[5]

            # Colocando os dados no dicionario:
            dic[sigla] = {
            'nome': nome,
            'ementa': ementa, 
            'bibliografia': bibliografia,
            'n_creditos': n_creditos,
            'carga_horaria': carga_horaria
            }


def submenu_disciplinas():
    """
    Exibe um submenu para o gerenciamento de cadastros de professores.

    Return:
        int: A opção selecionada pelo usuário.
    """
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


def executa(dic, path):

    while True:
        opt = submenu_disciplinas()
        
        funcoes = {
            1:mostra_td_disciplinas,
            2:mostra_disciplina,
            3:insere_disciplina,
            4:altera_disciplina,
            5:remove_disciplina,
        }

        if opt in funcoes:
            funcoes[opt](dic)
        elif opt == 6:
            grava_disciplinas(dic, path)
            return
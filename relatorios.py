import os
from professores import listar_atributos
from disciplinas import mostra_disciplina

# SUBMENU"s:
# 1 - Lista todos
# 2 - Listar um elemento específico do conjunto
# 3 - Incluir (sem repetição)
# 4 - Alterar 
# 5 - Excluir (após confirmação dos dados) um elemento do conjunto. 

"""
database1 (dict): professores-disciplinas
database2 (dict): professores
database3 (dict): disciplinas
"""

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

def buscar_professores_titulacao(database2):
    det_titulacao = input("Informe a titulação a ser listada (Mestrado ou Doutorado): ").lower()
    existe = False
    for registro in database2:
        if database2[registro]['titulacao'].lower() == det_titulacao:
            existe = True
            print("-" * 30)
            print("Registro Funcional:", registro)
            listar_atributos(database2, registro)
    if not existe:
        print("Não existe nenhum cadastro com essa titulação!") 

def buscar_disciplina_creditos(database3):
    min_creditos = float(input("Informe a quantidade de créditos da disciplina a ser listada: "))
    print("Disciplinas com mais de", min_creditos, "créditos:\n")
    existe = False
    for sigla in database3:
        if float(database3[sigla]['n_creditos']) > min_creditos:
            existe = True
            mostra_disciplina(database3, sigla)
            print()
    if not existe:
        print("Não existe nenhuma disciplina com essa quantidade mínima de créditos!") 

def buscar_disciplina_dias():
    ...
def executa(database1, database2, database3):

    while True:
        opt = submenu_relatorios()
        
        # funcoes = {
        #     1:buscar_professores
        # }

        if opt == 1:
            buscar_professores_titulacao(database2)
        elif opt == 2: 
            buscar_disciplina_creditos(database3)
        elif opt == 4:
            return
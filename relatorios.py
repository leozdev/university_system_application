import os
from professores import listar_atributos

# SUBMENU's:
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
        input('\nPressione [enter] para continuar...')
        os.system('cls')
        print('Sistema da Universidade')
        print('Desenvolvido por Leo Freitas & Vinicius Rafael\n')
        print('--- Menu de Gerenciamento de Relatórios ---')
        print('1 - Mostrar todos os dados de todos os professores que têm determinada titulação fornecida pelo usuário (mestrado ou doutorado)')
        print('2 - Mostrar todos os dados de todas as disciplinas que possuem mais do que X créditos')
        print('3 - Mostrar o Registro Funcional do Professor, o nome do professor, a Sigla da disciplina, o nome da disciplina e todos os demais atributos de Prof-Disc para aquelas disciplinas que serão ministradas às terças e às quintas feiras de cada semana.')
        print('4 - Voltar')

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 4:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def buscar_professores(database2, parametro):
    for registro in database2:
        if database2[registro]['titulacao'] == parametro:
            print("-" * 30)
            print("Registro Funcional:", registro)
            listar_atributos(database2, registro)
            print()
    
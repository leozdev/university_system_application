import disciplinas
import professores
import prof_disc
import relatorios
import os

### Padrão de DOCSTRING: ###

"""
Resumo da funcionalidade 

Argumentos:
    nome_do_argumento (type): O que é?
    ...

Return:
    type: O que?
    ...
"""
###########################

def menu():
    """
    Exibe um menu dos submenus

    Return:
        (int): A opção selecionada pelo usuário

    """ 
    while True:
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu Principal ---")
        print("1 - Menu de Professores")
        print("2 - Menu de Disciplinas")
        print("3 - Menu de Professores-Disciplinas")
        print("4 - Menu Relatórios")
        print("5 - Sair")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 5:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 5.")
                input("\nPressione [enter] para continuar...")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            input("\nPressione [enter] para continuar...")

def main():
    # Dados dos Professores
    path_professores = "dados_professores.txt"
    dados_professores = {}
    professores.carregar_dados(dados_professores, path_professores)

    # Dados das disciplinas
    dados_disciplinas = {}
    disciplinas.recupera_disciplinas(dados_disciplinas)
    
    # Dados das aulas
    path_prof_disc = "dados_prof_disc.txt"
    dados_prof_disc = {}
    prof_disc.carregar_dados(dados_prof_disc, path_prof_disc)

    opt_menu = 1
    while opt_menu != 5:
        opt_menu = menu()

        # Submenu Professores
        if opt_menu == 1:
            professores.executa(database=dados_professores, path=path_professores)

        # Submenu Disciplinas
        elif opt_menu == 2:
            disciplinas.executa(dic=dados_disciplinas)

        # Submenu Prof Disc
        elif opt_menu == 3:
            prof_disc.executa(database1=dados_prof_disc, database2=dados_professores, database3=dados_disciplinas, path=path_prof_disc)

        # Submenu Relatórios
        elif opt_menu == 4:
            ...

if __name__ == "__main__":
    main()
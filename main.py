import src.disciplinas as disciplinas
import src.professores as professores
import src.prof_disc as prof_disc
import src.relatorios as relatorios
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
    path_professores = "dados\dados_professores.txt"
    dados_professores = {}

    # Dados das Disciplinas
    path_disciplinas = "dados\dados_disciplinas.txt"
    dados_disciplinas = {}
    
    # Dados das Aulas
    path_prof_disc = "dados\dados_prof_disc.txt"
    dados_prof_disc = {}

    opt_menu = 1
    while opt_menu != 5:
        opt_menu = menu()

        # Submenu Professores
        if opt_menu == 1:
            # Carrega todos os dados existe no arquivo de banco de dados de professores
            professores.carregar_dados(dados_professores, path_professores)
            professores.executa(db_professores=dados_professores, path=path_professores)

        # Submenu Disciplinas
        elif opt_menu == 2:
            # Carrega todos os dados existe no arquivo de banco de dados de disciplinas
            disciplinas.carregar_dados(dados_disciplinas, path_disciplinas)
            disciplinas.executa(db_disciplinas=dados_disciplinas, path=path_disciplinas)

        # Submenu Prof Disc
        elif opt_menu == 3:
            # Carrega todos os dados existentes nos arquivos de banco de dados
            professores.carregar_dados(dados_professores, path_professores)
            disciplinas.carregar_dados(dados_disciplinas, path_disciplinas)
            prof_disc.carregar_dados(dados_prof_disc, path_prof_disc)

            prof_disc.executa(db_prof_disc=dados_prof_disc, db_professores=dados_professores, db_disciplinas=dados_disciplinas, path=path_prof_disc)

        # Submenu Relatórios
        elif opt_menu == 4:
            relatorios.executa(db_prof_disc=dados_prof_disc, db_professores=dados_professores, db_disciplinas=dados_disciplinas)
            
if __name__ == "__main__":
    main()
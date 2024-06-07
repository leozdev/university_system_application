import src.disciplinas as disciplinas
import src.professores as professores
import src.prof_disc as prof_disc
import src.relatorios as relatorios
import os

def menu():
    """
    Exibe o menu principal e solicita ao usuário que selecione uma opção.

    O menu apresenta opções para navegar por submenus de Professores, Disciplinas, Professores-Disciplinas e Relatórios, 
    ou para sair do programa. Solicita uma entrada do usuário e retorna a opção selecionada.

    Return:
        int: A opção selecionada pelo usuário (1 a 5).
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
    """
    Executa o menu principal e o submenu correspondente com base na opção selecionada pelo usuário, carregando os dados necessários do arquivo para persistência.

    Configura os caminhos para os arquivos de dados de professores, disciplinas, professores-disciplinas e relatórios. 
    """
    # Dados dos Professores
    path_professores = "dados\dados_professores.txt"
    dados_professores = {}

    # Dados das Disciplinas
    path_disciplinas = "dados\dados_disciplinas.txt"
    dados_disciplinas = {}
    
    # Dados das Aulas
    path_prof_disc = "dados\dados_prof_disc.txt"
    dados_prof_disc = {}

    # Caminhos dos relatórios:
    path_relatorio_titulacoes = "relatorios\\relatorio_professores_titulacao.txt"
    path_relatorio_creditos = "relatorios\\relatorio_disciplina_creditos.txt"
    path_relatorio_dias = "relatorios\\relatorio_disciplinas_dias.txt"

    opt_menu = 1
    while opt_menu != 5:
        opt_menu = menu()

        # Submenu Professores
        if opt_menu == 1:
            # Carrega todos os dados existe no arquivo de banco de dados de professores
            professores.carregar_dados(dados_professores, path_professores)
            # Executa
            professores.executa(dados_professores, path_professores)

        # Submenu Disciplinas
        elif opt_menu == 2:
            # Carrega todos os dados existe no arquivo de banco de dados de disciplinas
            disciplinas.carregar_dados(dados_disciplinas, path_disciplinas)
            # Executa 
            disciplinas.executa(dados_disciplinas, path_disciplinas)

        # Submenu Prof Disc
        elif opt_menu == 3:
            # Carrega todos os dados existentes nos arquivos de banco de dados
            professores.carregar_dados(dados_professores, path_professores)
            disciplinas.carregar_dados(dados_disciplinas, path_disciplinas)
            prof_disc.carregar_dados(dados_prof_disc, path_prof_disc)
            # Executa
            prof_disc.executa(dados_prof_disc, dados_professores, dados_disciplinas, path_prof_disc)

        # Submenu Relatórios
        elif opt_menu == 4:
            # Carrega todos os dados existentes nos arquivos de banco de dados
            professores.carregar_dados(dados_professores, path_professores)
            disciplinas.carregar_dados(dados_disciplinas, path_disciplinas)
            prof_disc.carregar_dados(dados_prof_disc, path_prof_disc)
            # Executa
            relatorios.executa(dados_prof_disc, dados_professores, dados_disciplinas, path_relatorio_titulacoes, path_relatorio_creditos, path_relatorio_dias)
    
    # Opção 5 -> Encerra o programa
    print("Encerrando programa...")

if __name__ == "__main__":
    main()
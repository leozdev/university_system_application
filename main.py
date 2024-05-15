import disciplinas
import professores
import prof_disc
import relatorios
import os

# SUBMENU's:
# 1 - Lista todos
# 2 - Listar um elemento específico do conjunto
# 3 - Incluir (sem repetição)
# 4 - Alterar 
# 5 - Excluir (após confirmação dos dados) um elemento do conjunto. 

def menu():
    """
    Exibe um menu dos submenus

    Returns:
        (int): A opção selecionada pelo usuário

    """
    show_input = False
    while True:
        if show_input:
            input('\nPressione [enter] para continuar...')

        os.system('cls')
        print('--- Menu Principal ---')
        print('1 - Menu de Professores')
        print('2 - Menu de Disciplinas')
        print('3 - Menu de Professores-Disciplinas')
        print('4 - Menu Relatórios')
        print('5 - Sair')
        
        show_input = True

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 5:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    dados_professores = {}

    opt_menu = 1
    while opt_menu != 5:
        opt_menu = menu()

        # Submenu Professores
        if opt_menu == 1:
            professores.executa(database = dados_professores)

        # Submenu Disciplinas
        elif opt_menu == 2:
            disciplinas.submenu_disciplinas()
            ...

        # Submenu Prof Disc
        elif opt_menu == 3:
            prof_disc.submenu_prof_disc()

        # Submenu Relatórios
        elif opt_menu == 4:
            relatorios.submenu_relatorios()
        
        elif opt_menu == 5:
            print('Saindo...')
                
if __name__ == "__main__":
    main()
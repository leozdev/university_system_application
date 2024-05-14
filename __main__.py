# import disciplinas
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
    os.system('cls')
    print('1 - Submenu de Professores')
    print('2 - Submenu de Disciplinas')
    print('3 - Submenu de Professores-Disciplinas')
    print('4 - Submenu Relatórios')
    print('5 - Sair')
    opt = int(input())
    return opt

def submenu_disciplinas():
    ...

def submenu_prof_disc():
    ...

def submenu_relatorios():
    ...

def main():
    dados_professores = {}

    opt_menu = 1
    while opt_menu != 5:
        opt_menu = menu()

        # Submenu Professores
        if opt_menu == 1:
            os.system('cls')
            professores.submenu_professores(dados_professores)

        # Submenu Disciplinas
        elif opt_menu == 2:
            submenu_disciplinas()

        # Submenu Prof Disc
        elif opt_menu == 3:
            submenu_prof_disc()

        # Submenu Relatórios
        elif opt_menu == 4:
            submenu_relatorios()
        
        elif opt_menu == 5:
            print('Saindo...')
        
        input('Pressione <enter> para continuar...')

if __name__ == "__main__":
    main()
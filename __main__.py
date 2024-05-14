import disciplinas
import professores
import prof_disc
import relatorios
import os

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

def submenu_professores():
    os.system('cls')
    print('1 - Listar Todos Dados Cadastrados')
    print('2 - Listar um Elemento Específico do Cadastro')
    print('3 - Incluir Cadastro')
    print('4 - Alterar um Dado do Cadastro')
    print('5 - Excluir um Dado do Cadastro')
    print('6 - Voltar')
    opt = int(input())
    return opt

def submenu_disciplinas():
    ...

def submenu_prof_disc():
    ...

def submenu_relatorios():
    ...

def main():
    opt = 1
    while opt != 5:
        opt = menu()

if __name__ == "__main__":
    main()
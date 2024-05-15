import os

# SUBMENU's:
# 1 - Lista todos
# 2 - Listar um elemento específico do conjunto
# 3 - Incluir (sem repetição)
# 4 - Alterar 
# 5 - Excluir (após confirmação dos dados) um elemento do conjunto. 

def submenu_prof_disc():
    """
    Exibe um submenu para o gerenciamento de cadastros de professores-disciplinas.

    Return:
        int: A opção selecionada pelo usuário.
    """
    while True:
        input('\nPressione [enter] para continuar...')
        os.system('cls')
        print('Sistema da Universidade')
        print('Desenvolvido por Leo Freitas & Vinicius Rafael\n')
        print('--- Menu de Gerenciamento de Professores-Disciplinas ---')
        print('1 - Listar Todos os Cadastros')
        print('2 - Listar um Cadastro Específico')
        print('3 - Incluir Cadastro')
        print('4 - Alterar um Cadastro Existente')
        print('5 - Excluir um Cadastro')
        print('6 - Voltar')

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 6:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def executa(database):
    """
    Executa o menu de gerenciamento de professores.

    Argumentos:
        database (dict): O banco de dados de professores.
    """
    while True:
        opt = submenu_prof_disc()
        
        if opt == 3:
            dados_prof_disc = dados()
            incluir(database, *dados_prof_disc)
            print(database)
        elif opt == 6:
            return

def dados():
    """
    ...
    """
    registro = input('Registro Funcional: ')
    sigla_disciplina = input('Sigla da Disciplina: ')
    ano = input('Ano: ')
    semestre = input('Semestre: ')
    dias_da_semana = input('Dias da Semana: ').split()
    horarios_do_curso = input('Horários do curso: ').split()
    nome_do_curso = input('Nome do Curso: ')
    return registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_do_curso, nome_do_curso


def incluir(database, registro, sigla_disciplina, ano, semestre, dias_da_semana, horarios_inicio, curso):
 
    if registro not in database:
        database[registro] = {}
    
    if (sigla_disciplina, ano, semestre) in database[registro]:
        print("Não é permitido adicionar mais de um cadastro com os mesmos valores para as chaves.")
        return
    
    database[registro][(sigla_disciplina, ano, semestre)] = {
        'dias_da_semana': dias_da_semana,
        'horarios_inicio': horarios_inicio,
        'curso': curso
    }

    print("Cadastro adicionado com sucesso.")



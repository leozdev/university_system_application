import os

def submenu_professores():
    """
    Exibe um submenu para o gerenciamento de cadastros de professores.

    Return:
        int: A opção selecionada pelo usuário.
    """
    while True:
        input('\nPressione [enter] para continuar...')
        os.system('cls')

        print('--- Menu de Gerenciamento de Professores ---')
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
        opt = submenu_professores()
        
        if opt == 1:
            listar_todos(database, nome_da_chave='registro-funcional')
        
        elif opt == 2:
            listar_elemento_especifico(database)
        
        elif opt == 3:
            incluir_cadastro(database)
        
        elif opt == 4:
            alterar_dado_cadastro(database)
        
        elif opt == 5:
            excluir_dado_cadastro(database)
        
        elif opt == 6:
            return

def existe_chave(database, chave):
    """
    Verifica se uma chave existe no banco de dados.

    Argumentos:
        database (dict): O banco de dados.
        chave (str): A chave a ser verificada.

    Return:
        bool: True se a chave existe, False caso contrário.
    """
    return chave in database.keys()

def dados():
    """
    Recebe os dados necessários para incluir um novo cadastro no banco de dados.

    Return:
        tuple: Uma tupla com os dados do novo cadastro.
    """
    nome = input('Nome completo: ')
    data_nasc = input('Data de Nascimento (DD/MM/AAAA): ')
    sexo = input('Sexo (F/M): ')
    area = input('Área de Pesquisa: ')
    titulacao = input('Titulação: ')
    graduacao = input('Graduação: ')
    emails = input('E-mails (separados por espaço): ').split()
    telefones = input('Telefones (separados por espaço): ').split()
    return nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones

def incluir(database, chave, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones):
    """
    Inclui um novo cadastro no banco de dados.

    Argumentos:
        database (dict): O banco de dados.
        chave (str): A chave para o novo cadastro.
        nome (str): Nome completo.
        data_nasc (str): Data de Nascimento (DD/MM/AAAA).
        sexo (str): Sexo (F/M).
        area (str): Área de Pesquisa.
        titulacao (str): Titulação.
        graduacao (str): Graduação.
        emails (list): Lista de e-mails.
        telefones (list): Lista de telefones.
    """
    database[chave] = {
        'nome': nome,
        'data-nascimento': data_nasc,
        'sexo': sexo,
        'area-de-pesquisa': area,
        'titulacao': titulacao,
        'graduacao': graduacao,
        'emails': emails,
        'telefones': telefones
    }

def listar_atributos(database, chave):
    """
    Lista os atributos de um cadastro específico no banco de dados.

    Argumentos:
        database (dict): O banco de dados.
        chave (str): A chave do cadastro.
    """
    for subchave, valor in database[chave].items():
        if type(valor) == list:
            print(f'{subchave.capitalize()}:', ', '.join(map(str, valor)))
        else:
            print(f'{subchave.capitalize()}:', valor)

def listar_todos(database, nome_da_chave):
    """
    Lista todos os cadastros do banco de dados.

    Argumentos:
        database (dict): O banco de dados.
        nome_da_chave (str): O nome da chave que identifica os cadastros.
    """
    print('Todos os dados cadastrados:\n')
    for chave in database.keys():
        print('*' * 20)
        print(f'{nome_da_chave.capitalize()}:', chave)
        listar_atributos(database, chave)
        print()

def listar_elemento_especifico(database):
    """
    Lista os atributos de um cadastro específico no banco de dados.

    Argumentos:
        database (dict): O banco de dados.
    """
    input_chave = input('Registro Funcional: ')
    if existe_chave(database, chave=input_chave):
        listar_atributos(database, chave=input_chave)
    else:
        print("Registro não encontrado!")

def incluir_cadastro(database):
    """
    Solicita ao usuário os dados para incluir um novo cadastro no banco de dados.

    Argumentos:
        database (dict): O banco de dados.
    """
    input_chave = input('Registro Funcional: ')
    if not existe_chave(database, chave=input_chave):
        dados_do_professor = dados()
        incluir(database, input_chave, *dados_do_professor)
        print("Dados inseridos com sucesso!")
    else:
        print('Dados já existem...')


# Modularizar mais essas ultimas 2 funcoes, se possivel...

def alterar_dado_cadastro(database):
    """
    Altera os dados de um cadastro existente no banco de dados.

    Argumentos:
        database (dict): O banco de dados.
    """
    input_chave = input('Registro Funcional: ')
    if existe_chave(database, chave=input_chave):
        dados_do_professor = dados()
        input_confirma = input("Tem certeza que deseja alterar? (S/N): ").upper()
        if input_confirma == 'S':
            incluir(database, input_chave, *dados_do_professor)
            print("Dados alterados com sucesso!")
        elif input_confirma == 'N':
            print("Alteração cancelada!")
        else:
            print('Opção inválida, retornando ao menu principal...')
    else:
        print("Registro não encontrado!")

def excluir_dado_cadastro(database):
    """
    Exclui um cadastro existente do banco de dados.

    Argumentos:
        database (dict): O banco de dados.
    """
    input_chave = input('Registro Funcional: ')
    if existe_chave(database, chave=input_chave):
        input_confirma = input("Tem certeza que deseja excluir? (S/N): ").upper()
        if input_confirma == 'S':
            del database[input_chave]
            print("Dados excluídos com sucesso!")
        elif input_confirma == 'N':
            print("Exclusão cancelada!")
        else:
            print('Opção inválida, retornando ao menu principal...')
    else:
        print("Registro não encontrado!")

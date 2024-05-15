def dados():
    nome = input('Nome completo: ')
    data_nasc = input('Data de Nascimento: (DD/MM/AAAA) ')
    sexo = input('Sexo: (F/M) ')
    area = input('Área de Pesquisa: ')
    titulacao = input('Titulação: ')
    graduacao = input('Graduação: ')
    emails = input('E-mails: ').split()
    telefones = input('Telefones: (DD)99999-9999 ').split()
    return nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones

def incluir(database, chave, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones):
    database[chave] = {
    'nome':nome,
    'data-nascimento':data_nasc,
    'sexo': sexo,
    'area-de-pesquisa': area,
    'titulacao': titulacao,
    'graduacao': graduacao,
    'emails': emails,
    'telefones':telefones
    }

def listar_atributos(database, chave):
    for subchave in database[chave].keys():
            valor = database[chave][subchave]

            if type(valor) == list:
                print(f'{subchave.capitalize()}:', ', '.join(map(str, valor)))
            else:
                print(f'{subchave.capitalize()}:', valor)

def existe_chave(database, chave):
    if chave in database.keys():
        return True
    
# MELHORAR ESSA FUNCAO
def listar_todos(database, nome_da_chave):
    print('Todos os dados cadastrados:\n')
    for chave in database.keys():
        print('*'*20)
        print(f'{nome_da_chave.capitalize()}:', chave)
        listar_atributos(database, chave)
        print()
           
def alterar(database, chave):
    incluir(database, chave)
        
def excluir(database, chave):
    del database[chave]

def confirma_dados(database, chave):
    listar_atributos(database, chave)
    input_confirma = input('Confirma os dados')

##############################################

def submenu_professores():
    print('1 - Listar Todos database Cadastrados')
    print('2 - Listar um Elemento Específico do Cadastro')
    print('3 - Incluir Cadastro')
    print('4 - Alterar um Dado do Cadastro')
    print('5 - Excluir um Dado do Cadastro')
    print('6 - Voltar')
    opt = int(input(">> "))
    return opt

def executa(database):
    
    opt = submenu_professores()

    str_input_chave = 'Registro Funcional: '
    str_nome_da_chave = 'registro-funcional'

    # Listar todos
    if opt == 1:
        listar_todos(database, nome_da_chave = str_nome_da_chave)

    # Listar um elemento específico do conjunto
    elif opt == 2:
        listar_atributos(database, chave= input(str_input_chave))

    # Incluir (sem repetição)
    elif opt == 3:
        input_chave = input(str_input_chave)
        nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = dados()

        if not existe_chave(database, chave=input_chave):
            incluir(database, input_chave, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones)

            # print("Dados inseridos com sucesso!")
        else:
            print('Dados já existem...')

    # Alterar 
    elif opt == 4:
        input_chave = input(str_input_chave)
        nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = dados()

        if existe_chave(database, chave=input_chave):
            alterar(database, chave=input_chave)

        else:
            print("Registro não encontrado!")

    # Excluir (após confirmação dos DADOS) um elemento do conjunto.
    elif opt == 5:
        input_chave = input(str_input_chave)
        nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = dados()

        excluir(database, chave=input_chave)

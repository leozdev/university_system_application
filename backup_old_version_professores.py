def existe(dados, chave):
    if chave in dados.keys():
        return True
    return False

def listar_todos(dados, nome_da_chave):
    for chave in dados.keys():
        print('*'*20)
        print(nome_da_chave.capitalize(), chave)
        for subchave in dados[chave].keys():
            valor = dados[chave][subchave]
            if type(valor) == list:
                print(subchave.capitalize(),':', ', '.join(map(str, dados[chave][subchave])))
            else:
                print(subchave.capitalize(),':', dados[chave][subchave])
        print()
            
def listar_elemento_especifico(dados, chave, conteudo):
    if existe(dados, chave):
        return dados[chave][conteudo]

def incluir(dados):
    registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = cadastro()
    if not existe(dados, registro):
        dados[registro] = {
        'nome':nome,
        'data-nasc':data_nasc,
        'sexo': sexo,
        'area-de-pesquisa': area,
        'titulacao': titulacao,
        'graduacao': graduacao,
        'emails': emails,
        'telefones':telefones
    }
        return True
    return False
        
def alterar(dados, chave, subchave, atualizacao):
    if existe(dados, chave):
        dados[chave][subchave] = atualizacao

def excluir(dados, chave, subchave):
    if existe(chave, dados):
        dados[chave][subchave] = ''

def cadastro():
    registro = input('Registro funcional: ')
    nome = input('Nome completo: ')
    data_nasc = input('Data de Nascimento: (DD/MM/AAAA) ')
    sexo = input('Sexo: (F/M) ')
    area = input('Área de Pesquisa: ')
    titulacao = input('Titulação: ')
    graduacao = input('Graduação: ')
    emails = input('E-mails: ').split()
    telefones = input('Telefones: (DD)99999-9999 ').split()
    return registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones

def submenu_professores(dados):
    print('1 - Listar Todos Dados Cadastrados')
    print('2 - Listar um Elemento Específico do Cadastro')
    print('3 - Incluir Cadastro')
    print('4 - Alterar um Dado do Cadastro')
    print('5 - Excluir um Dado do Cadastro')
    print('6 - Voltar')

    opt = int(input())

    if opt == 1:
        print('Todos os dados cadastrados:\n')
        listar_todos(dados,'registro-funcional:')

    elif opt == 2:
        registro = input('Registro funcional: ')
        if existe(dados, registro):
            print('Dados disponíveis:',', '.join(dados[registro].keys()).title())
            conteudo = input('Informe o dado que deseja listar: ').lower()
            print(listar_elemento_especifico(dados, registro, conteudo))

    elif opt == 3:
        incluir(dados)

    elif opt == 4:
        registro = input('Registro funcional:')
        print('Dados disponíveis:',', '.join(dados[registro].keys()).title())
        dado = input('Informe o dado que deseja alterar: ')
        atualizacao = input('Atualização: ')

        confirma = input('Confirma? [S]im [N]ão: ').upper()
        if confirma == 'S':
            alterar(dados, registro, dado, atualizacao)
            print('Alteração concluida!')

        elif confirma == 'N':
            print('Alteração cancelada...')

        else:
            print('Opção inválida!')

    elif opt == 5:
        chave = input()
        subchave = input()
        excluir(dados, chave, subchave)

    elif opt == 6:
        return
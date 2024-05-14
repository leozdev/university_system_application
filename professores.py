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
    if chave in dados.keys():
        print(dados[chave][conteudo])
        return True
    return False

def incluir(dados):
    registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = cadastro()
    if registro not in dados.keys():
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
    if chave in dados.keys():
        dados[chave][subchave] = atualizacao
        return True
    return False

def excluir(dados, chave, subchave):
    if chave in dados and subchave in dados[chave]:
        del dados[chave][subchave]
        return True
    return False


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

# Novas funcionalidades ... (TERMINAR)
def submenu_professores(dados):
    print('1 - Listar Todos Dados Cadastrados')
    print('2 - Listar um Elemento Específico do Cadastro')
    print('3 - Incluir Cadastro')
    print('4 - Alterar um Dado do Cadastro')
    print('5 - Excluir um Dado do Cadastro')
    print('6 - Voltar')

    opt = int(input())

    return executa(dados, opt)

def dados_disponiveis(dados, registro):
    if registro in dados.keys():
        print('Dados disponíveis:',', '.join(dados[registro].keys()).title())
        return True
    return False

def executa(dados, opt):
    print()

    # Listar todos
    if opt == 1:
        print('Todos os dados cadastrados:\n')
        listar_todos(dados,'registro-funcional: ')

    # Listar um elemento específico do conjunto
    elif opt == 2:
        registro = input('Registro funcional: ')
        if dados_disponiveis(dados, registro):
            conteudo = input('Informe um dado que deseja listar: ').lower()
            listar_elemento_especifico(dados, registro, conteudo)
        else:
            ...

    # Incluir (sem repetição)
    elif opt == 3:
        incluir(dados)

    # Alterar 
    elif opt == 4:
        registro = input('Registro funcional:')
        if dados_disponiveis(dados, registro):
            dado = input('Informe o dado que deseja alterar: ')

            if type(dados[registro][dado]) == list:
                atualizacao = input('Atualização: ').split()
            else:
                atualizacao = input('Atualização: ')

            confirma = input('Confirma? [S]im [N]ão: ').upper()
            if confirma == 'S':
                alterar(dados, registro, dado, atualizacao)
                print('Alteração concluida!')

            elif confirma == 'N':
                print('Alteração cancelada...')

            else:
                print('Opção inválida!')
        else:
            ...

    # Excluir (após confirmação dos dados) um elemento do conjunto.
    elif opt == 5:
        chave = input()
        subchave = input()
        excluir(dados, chave, subchave)

    elif opt == 6:
        return
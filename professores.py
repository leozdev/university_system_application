professores = {}

def existe(dados, chave):
    if chave in dados.keys():
        return True
    return False

def listar_todos(dados):
    for chave in dados.keys():
        print(chave)
        for subchave in dados[chave].keys():
            valor = dados[chave][subchave]
            if type(valor) == list:
                print(subchave.capitalize(),':', ', '.join(map(str, dados[chave][subchave])))
            else:
                print(subchave.capitalize(),':', dados[chave][subchave])
            
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

import os
from src.auxiliar import existe_arquivo, confirmar

def submenu_professores():
    while True:
        input("\nPressione [enter] para continuar...")
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu de Gerenciamento de Professores ---")
        print("1 - Listar Todos os Cadastros")
        print("2 - Listar um Cadastro Específico")
        print("3 - Incluir Cadastro")
        print("4 - Alterar um Cadastro Existente")
        print("5 - Excluir um Cadastro")
        print("6 - Voltar")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 6:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 6.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def entrada_registro():
    return input("Digite o Registro Funcional: ")

# Futuramente incluir uma função que checa se não tem campos em brancos!
def incluir_dados(db_professores, registro):
    nome = input("Digite o Nome completo: ").title()
    data_nasc = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
    sexo = input("Digite o Sexo (F/M): ").title()
    area = input("Digite a Área de Pesquisa: ").title()
    titulacao = input("Digite a Titulação: ").title()
    graduacao = input("Digite a Graduação: ").title()
    emails = input("Digite os E-mails (separados por vírgula-espaço): ").capitalize().split(", ")
    telefones = input("Digite os Telefones (separados por vírgula-espaço): ").split(", ")

    db_professores[registro] = {
        "nome": nome,
        "data-nascimento": data_nasc,
        "sexo": sexo,
        "area-de-pesquisa": area,
        "titulacao": titulacao,
        "graduacao": graduacao,
        "emails": emails,
        "telefones": telefones
    }

def inserir_professor(db_professores):
    registro = entrada_registro()
    if registro not in db_professores:
        incluir_dados(db_professores, registro)
        return True
    return False

def listar_todos_professores(db_professores):
    print("Todos os professores cadastrados:\n")
    for registro in db_professores:
        print("-" * 30)
        print("Registro Funcional:", registro)
        listar_atributos_professor(db_professores, registro)

def listar_atributos_professor(db_professores, registro=None):
    if registro is None:
        registro = entrada_registro()

    if registro in db_professores:
        dados = db_professores[registro]
        print("\nNome:", dados['nome'])
        print("Data de Nascimento:", dados['data-nascimento'])
        print("Sexo:", dados['sexo'])
        print("Área de Pesquisa:", dados['area-de-pesquisa'])
        print("Titulação:", dados['titulacao'])
        print("Graduação:", dados['graduacao'])
        print("E-mails:", ", ".join(dados['emails']))
        print("Telefones:", ", ".join(dados['telefones']))
        return True # Tudo ocorreu bem
    else:
        return False # Registro não encontrado

def alterar_dados_professor(db_professores):
    registro = entrada_registro()
    if registro in db_professores:
        if confirmar('alterar'):
            incluir_dados(db_professores, registro)
            return 1 # Alterado
        else:
            return -1 # Alteração Cancelada
    else:
        return 0 # Registro não encontrado

def remover_professor(db_professores):
    registro = entrada_registro()
    if registro in db_professores:
        if confirmar('remover'):
            del db_professores[registro]
            return 1 # Excluído
        else:
            return -1 # Exclusão Cancelada
    else:
        return 0 # Registro não encontrado

def gravar_dados(db_professores, path):
    arq = open(path, "w", encoding="utf-8")
    for registro, dados in db_professores.items():
        linha = (f"{registro};{dados['nome']};"
                 f"{dados['data-nascimento']};{dados['sexo']};"
                 f"{dados['area-de-pesquisa']};{dados['titulacao']};"
                 f"{dados['graduacao']};{','.join(dados['emails'])};"
                 f"{','.join(dados['telefones'])}\n"
                 )
        arq.write(linha)
    arq.close()

def carregar_dados(db_professores, path):
    if existe_arquivo(path):
        arq = open(path, "r", encoding="utf-8")

        for linha in arq:
            registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones = linha.strip().split(";")

            db_professores[registro] = {
                "nome": nome,
                "data-nascimento": data_nasc,
                "sexo": sexo,
                "area-de-pesquisa": area,
                "titulacao": titulacao,
                "graduacao": graduacao,
                "emails": emails.split(','),
                "telefones": telefones.split(',')
            }
        arq.close()

def executa(db_professores, path):
    while True:
        opt = submenu_professores()

        if opt == 1:
            listar_todos_professores(db_professores)

        elif opt == 2:
            if not listar_atributos_professor(db_professores):
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")

        elif opt == 3:
            if inserir_professor(db_professores):
                print("Professor cadastrado com sucesso.")
            else:
                print("Erro: Já existe um cadastrado com esse registro funcional no banco de dados.")
        
        # Pensar em alguma solução melhor que essa (Se tiver como...)
        elif opt == 4:
            retorno = alterar_dados_professor(db_professores)
            if retorno == 1:
                print("Dados do professor alterado com sucesso.")
            elif retorno == -1:
                print("Alteração cancelada!")
            else:
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")

        elif opt == 5:
            retorno = remover_professor(db_professores)
            if retorno == 1:
                print("Professor removido com sucesso.")
            elif retorno == -1:
                print("Remoção cancelada!")
            else:
                print("Erro: Esse registro funcional não consta no banco de dados de professores.")

        elif opt == 6:
            gravar_dados(db_professores, path)
            return
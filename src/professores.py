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

def entrada_dados():

    nome = input("Digite o Nome completo: ")
    data_nasc = input("Digite a Data de Nascimento (DD/MM/AAAA): ")
    sexo = input("Digite o Sexo: ")
    area = input("Digite a Área de Pesquisa: ")
    titulacao = input("Digite a Titulação: ")
    graduacao = input("Digite a Graduação: ")
    emails = input("Digite os E-mails (separados por vírgula): ").split(", ")
    telefones = input("Digite os Telefones (separados por vírgula): ").split(", ")

    return nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones

def incluir(db_professores, registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones):

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

def incluir_cadastro(db_professores):
    registro = entrada_registro()
    if registro not in db_professores:
        dados_do_professor = entrada_dados()
        incluir(db_professores, registro,  *dados_do_professor)
        return True
    else:
        return False

def listar_todos(db_professores):
    print("Todos os dados cadastrados:\n")
    for registro in db_professores:
        print("-" * 30)
        print("Registro Funcional:", registro)
        listar_atributos(db_professores, registro)

def listar_atributos(db_professores, registro=None):
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

    else:
        print("Registro não encontrado!")

# Arrumar a funcao confirmar
def alterar_cadastro(db_professores):
    registro = entrada_registro()
    if registro in db_professores:
        dados_do_professor = entrada_dados()
        
        if confirmar('alterar'):
            incluir(db_professores, registro, *dados_do_professor)
            return True
    else:
        return False

def excluir_cadastro(db_professores):
    registro = entrada_registro()
    
    if registro in db_professores:
        if confirmar('excluir'):
            del db_professores[registro]
            return True
    else:
        return False
 
def gravar_dados(db_professores, path):
    arq = open(path, "w", encoding="utf-8")

    for registro in db_professores:
        dados = db_professores[registro]
        linha = (f"{registro};{dados['nome']};"
                 f"{dados['data-nascimento']};"
                 f"{dados['sexo']};"
                 f"{dados['area-de-pesquisa']};"
                 f"{dados['titulacao']};" 
                 f"{dados['graduacao']};" 
                 f"{','.join(dados['emails'])};" 
                 f"{','.join(dados['telefones'])}\n")
        
        arq.write(linha)
    arq.close()

def carregar_dados(db_professores, path):
    if existe_arquivo(path):
        arq = open(path, "r")

        for linha in arq:
            linha = linha.strip().split(";")
            registro = linha[0]
            nome = linha[1]
            data_nasc = linha[2]
            sexo = linha[3]
            area = linha[4]
            titulacao = linha[5]
            graduacao = linha[6]
            emails = linha[7].split(',')
            telefones = linha[8].split(',')

            incluir(db_professores, registro, nome, data_nasc, sexo, area, titulacao, graduacao, emails, telefones)
        
        arq.close()
        
def executa(db_professores, path):
    while True:
        opt = submenu_professores()

        if opt == 1:
            listar_todos(db_professores)

        elif opt == 2:
            listar_atributos(db_professores)
        
        elif opt == 3:
            if incluir_cadastro(db_professores):
                print("Professor cadastrado com sucesso!")
            else:
                print("Professor já cadastrado!")

        elif opt == 4:
            if alterar_cadastro(db_professores):
                print("Cadastro alterado com sucesso!")
            else:
                print("Registro não encontrado!")

        elif opt == 5:
            if excluir_cadastro(db_professores):
                print("Cadastro excluído com sucesso!")
            else:
                print("Registro não encontrado!")

        elif opt == 6:
            gravar_dados(db_professores, path)
            return
disciplina = { 
    'APR1' : { 
        'nome': 'Algoritmos',
        'ementa': 'BES', 
        'bibliografia': 'blabla',
        'n_creditos': '10',
        'carga_horaria': '122h'
    }
}


def existe_disciplina(dic,sigla):
    if sigla in dic.keys():
        return True
    else:
        return False
    
    
def insere_disciplina(dic):

    sigla = input("Digite a sigla da disciplina: ")

    
    if existe_disciplina(dic,sigla):
        print("Disciplina já cadastrada!")
        input("Tecle <ENTER> para continuar...\n")
        
    else:
        nome = input("Digite o nome da disciplina: ")
        ementa = input("Digite a ementa da disciplina: ")
        bibliografia = input("Digite a bibliografia da disciplina: ")
        n_creditos = input("Digite o número de creditos da disciplina: ")
        carga_horaria = input("Digite a carga horaria da disciplina: ")

        dic[sigla] = {
        'nome': nome,
        'ementa': ementa, 
        'bibliografia': bibliografia,
        'n_creditos': n_creditos,
        'carga_horaria': carga_horaria
        }

        print("Dados inseridos com sucesso!")


def mostra_disciplina(dic):
    sigla = input("Digite a sigla da disciplina que deseja consultar: ")

    if existe_disciplina(dic, sigla):
        dados = dic[sigla]
        print("Nome:", dados['nome'])
        print("Ementa:", dados['ementa'])
        print("Bibliografia:", dados['bibliografia'])
        print("Número de Créditos:", dados['n_creditos'])
        print("Carga Horária:", dados['carga_horaria'])
    else:
        print("Disciplina não encontrada!")


def mostra_td_disciplinas(dic):

    print("Todas disciplinas\n")
    print("SIGLA - NOME - EMENTA - BIBLIOGRAFIA - NUM DE CREDITOS - CARGA HORARIA\n")

    for codigo, dados in dic.items(): 

        linha = codigo + " - " + dados['nome'] + " - " + dados['ementa'] + " - " + dados['bibliografia'] + " - " + dados['n_creditos'] + " - " + dados['carga_horaria'] + "\n"
        print(linha)

    print("")


def altera_disciplina(dic):
    sigla = input("Digite a sigla da disciplina que deseja alterar: ")
    
    if existe_disciplina(dic,sigla):
        confirma = input("Tem certeza que deseja alterar? (S/N): ").upper()
        
        if confirma == 'S':
            nome = input("Digite o nome da disciplina: ")
            ementa = input("Digite a ementa da disciplina: ")
            bibliografia = input("Digite a bibliografia da disciplina: ")
            n_creditos = input("Digite o número de creditos da disciplina: ")
            carga_horaria = input("Digite a carga horaria da disciplina: ")

            dic[sigla] = {
            'nome': nome,
            'ementa': ementa, 
            'bibliografia': bibliografia,
            'n_creditos': n_creditos,
            'carga_horaria': carga_horaria
            }
            
            print("Dados alterados com sucesso!")
            
        else:
            print("Alteração cancelada!")

    else:
        print("Disciplina não foi encontrada!")


def remove_disciplina(dic):
    sigla = input("Digite a sigla da disciplina que deseja remover: ")

    if existe_disciplina(dic,sigla):
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
        if confirma == 'S':
            del dic[sigla]
            print("Dados apagados com sucesso!")
            
        else:
            print("Exclusão cancelada!")

    else:

        print("Disciplina não cadastrada!")


def relatorio(dic, n):
    print("Disciplinas com mais de", n, "créditos:\n")
    print("SIGLA - NOME - EMENTA - BIBLIOGRAFIA - NUM DE CREDITOS - CARGA HORARIA\n")
    
    for codigo, dados in dic.items():
        num_creditos = int(dados['n_creditos'])
        if num_creditos > n:
            linha = codigo + " - " + dados['nome'] + " - " + dados['ementa'] + " - " + dados['bibliografia'] + " - " + dados['n_creditos'] + " - " + dados['carga_horaria'] + "\n"
            print(linha)
    
    print("")


def submenu_disciplinas():
    ...
    
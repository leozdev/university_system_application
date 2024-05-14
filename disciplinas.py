disciplina = { 
    'APR1' : { 
        'nome': 'Algoritmos',
        'ementa': 'BES', 
        'bibliografia': 'blabla',
        'n_creditos': '10',
        'carga_horarria': '122h'
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
        'carga_horarria': carga_horaria
        }

        print("Dados inseridos com sucesso!")


def altera_disciplina(dic):
    sigla = input("Digite a sigla da disciplina: ")
    
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
            'carga_horarria': carga_horaria
            }
            
            print("Dados alterados com sucesso!")
            
        else:
            print("Alteração cancelada!")

    else:
        print("Disciplina não foi encontrada!")


altera_disciplina(disciplina)
print(disciplina)

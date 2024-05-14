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
        bibliografia = input("Digite a bibliografia: ")
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

insere_disciplina(disciplina)
print(disciplina)

def main():
    ...

if __name__ == "__main__":
    main()
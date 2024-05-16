import os
# DATABASE 1 = PROF-DIC
# DATABASE 2 = PROFESSORES
# DATABASE 3 = DISCIPLINAS

def submenu_prof_disc():
    while True:
        input('\nPressione [enter] para continuar...')
        os.system('cls')
        print('Sistema da Universidade')
        print('Desenvolvido por Leo Freitas & Vinicius Rafael\n')
        print('--- Menu de Gerenciamento de Professores-Disciplinas ---')
        print('1 - Listar Todos os Cadastros')
        print('2 - Listar um Cadastro Específico')
        print('3 - Incluir Cadastro')
        print('4 - Alterar um Cadastro Existente')
        print('5 - Excluir um Cadastro')
        print('6 - Voltar')

        try:
            opt = int(input('Selecione uma opção: '))
            if 1 <= opt <= 6:
                return opt
            else:
                print('Opção inválida. Por favor, selecione uma opção de 1 a 6.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')

def dados():
    ano = input('Ano: ')
    semestre = input('Semestre: ')
    dias_da_semana = input('Dias da Semana: ').split()
    horarios_do_curso = input('Horários do curso: ').split()
    nome_do_curso = input('Nome do Curso: ')

    return ano, semestre, dias_da_semana, horarios_do_curso, nome_do_curso

def incluir(database1, database2, database3):
    registro = input('Registro Funcional: ')

    if registro in database2:
        sigla_disciplina = input('Sigla da Disciplina: ')

        if sigla_disciplina in database3:
            ano, semestre, dias_da_semana, horarios_inicio, curso = dados()

            if registro not in database1:
                database1[registro] = {}
            
            if (sigla_disciplina, ano, semestre) in database1[registro]:
                print('Não é permitido adicionar mais de um cadastro com os mesmos valores para as chaves.')
                return
            
            database1[registro][(sigla_disciplina, ano, semestre)] = {
                'dias_da_semana': dias_da_semana,
                'horarios_inicio': horarios_inicio,
                'curso': curso
            }
            print('Cadastro adicionado com sucesso.')
        else:
            print('Não foi possível encontrar essa disciplina no banco de dados.')
    else:
        print('Não foi possível encontrar esse registro no banco de dados.')

def listar_todos(database1):
    for registro in database1.keys():
        listar_elemento_especifico(database1, registro)

def listar_elemento_especifico(database1, registro):

    if registro in database1:

        print(f'\nRegistro: {registro}')

        for conjunto_chaves, valores in database1[registro].items():
            sigla_disciplina, ano, semestre = conjunto_chaves
        
            print("Sigla da disciplina:", sigla_disciplina)
            print("Ano:", ano)
            print("Semestre:", semestre)
            print("Dias da Semana:", ', '.join(valores['dias_da_semana']))
            print("Horários de início", ', '.join(valores['horarios_inicio']))
            print("Curso:", valores['curso'])
            print()

    else:
        print(f'O registro não foi encontrado no banco de dados.')
  
def obter_registro_e_conjunto_chaves(database1):
    registro = input('Registro Funcional: ')
    if registro in database1:
        conjunto_chaves = (input('Sigla da Disciplina: '), input('Ano: '), input('Semestre: '))
        if conjunto_chaves in database1[registro]:
            return registro, conjunto_chaves
        else:
            print('Dados não encontrado.')
    else:
        print('Registro não encontrado no banco de dados.')
    return None, None

def excluir_elemento(database1):
    registro, conjunto_chaves = obter_registro_e_conjunto_chaves(database1)
    if registro and conjunto_chaves:
        del database1[registro][conjunto_chaves]
        print('Cadastro excluído com sucesso.')


def alterar_dados(database1):
    registro, conjunto_chaves = obter_registro_e_conjunto_chaves(database1)
    if registro and conjunto_chaves:
        print('\nCadastro Encontrado!\nAtualize os dados:\n')
        database1[registro][conjunto_chaves]['dias_da_semana'] = input('Dias da Semana: ').split()
        database1[registro][conjunto_chaves]['horarios_inicio'] = input('Horários do curso: ').split()
        database1[registro][conjunto_chaves]['curso'] = input('Nome do Curso: ')
        print('Cadastro alterado com sucesso.')

def executa(database1, database2, database3):
    while True:
        opt = submenu_prof_disc()
        
        if opt == 1:
            listar_todos(database1)
        
        elif opt == 2:
            registro = input('Informe o registro funcional: ')
            listar_elemento_especifico(database1, registro)
        
        elif opt == 3:
            incluir(database1, database2, database3)
        
        elif opt == 4:
            alterar_dados(database1)
        
        elif opt == 5:
            excluir_elemento(database1)
        
        elif opt == 6:
            return

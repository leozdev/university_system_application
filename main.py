import disciplinas
import professores
import prof_disc
import relatorios
import os

### Padrão de DOCSTRING: ###

"""
Resumo da funcionalidade 

Argumentos:
    nome_do_argumento (type): O que é?
    ...

Return:
    type: O que?
    ...
"""
###########################

def menu():
    """
    Exibe um menu dos submenus

    Return:
        (int): A opção selecionada pelo usuário

    """ 
    while True:
        os.system("cls")
        print("Sistema da Universidade")
        print("Desenvolvido por Leo Freitas & Vinicius Rafael\n")
        print("--- Menu Principal ---")
        print("1 - Menu de Professores")
        print("2 - Menu de Disciplinas")
        print("3 - Menu de Professores-Disciplinas")
        print("4 - Menu Relatórios")
        print("5 - Sair")

        try:
            opt = int(input("Selecione uma opção: "))
            if 1 <= opt <= 5:
                return opt
            else:
                print("Opção inválida. Por favor, selecione uma opção de 1 a 5.")
                input("\nPressione [enter] para continuar...")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            input("\nPressione [enter] para continuar...")

def main():
    # Coloquei esses dados para fazer o teste unitario + integração
    dados_professores = {
        "1000": {
            "nome": "Jorge Curtigi", 
            "data-nascimento": "01/01/1900", 
            "sexo": "M", 
            "area-de-pesquisa": "Engenharia de Software", 
            "titulacao": "Doutor", 
            "graduacao": "Usp", 
            "emails": ["curtigi@ifsp.edu.br", "jorge@ifsp.edu.br"], 
            "telefones": ["(16)9999-8888", "(11)97777-7777"]}, 

        "1001": {
            "nome": "Eloize Seno", 
            "data-nascimento": "01/01/1900", 
            "sexo": "F", 
            "area-de-pesquisa": "Processamento de Linguagem Natural", 
            "titulacao": "Doutora", 
            "graduacao": "Usp", 
            "emails": ["eloize.seno@ifsp.edu.r"], 
            "telefones": ["119999-3333"]
            }}
    
    # dados_disciplinas = {
    #     "SCLPPSW": {
    #         "nome": "Processos de Produção de Software",
    #         "ementa": "A disciplina define e contextualiza historicamente a Engenharia de Software, oferecendo uma visão geral dos principais assuntos estudados e do perfil profissional esperado nessa área da Computação.",
    #         "bibliografia": "PFLEEGER, Shari L. Engenharia de software: teoria e prática. 2. ed. São Paulo: Prentice Hall, 2004.", 
    #         "n_creditos": "66,7", 
    #         "carga_horaria": "66,7h"}, 

    #     "SCLAPR1": {
    #         "nome": "Algoritimos e Programação 1", 
    #         "ementa": "A disciplina aborda os conceitos básicos sobre computadores, com foco no desenvolvimento de algoritmos.", 
    #         "bibliografia": "ASCENCIO, Ana Fernanda Gomes; CAMPOS, Edilene Aparecida Veneruchi de. Fundamentos da programação de computadores. 3. ed. São Paulo: Pearson Prentice Hall, 2012.", 
    #         "n_creditos": "100", 
    #         "carga_horaria": "100h"
    #         }}
    dados_disciplinas = {}
    disciplinas.recupera_disciplinas(dados_disciplinas)
    
    dados_prof_disc = {}

    opt_menu = 1
    while opt_menu != 5:
        opt_menu = menu()

        # Submenu Professores
        if opt_menu == 1:
            professores.executa(database=dados_professores)

        # Submenu Disciplinas
        elif opt_menu == 2:
            disciplinas.executa(dic=dados_disciplinas)
            # disciplinas.submenu_disciplinas()
            ...

        # Submenu Prof Disc
        elif opt_menu == 3:
            prof_disc.executa(dados_prof_disc, dados_professores, dados_disciplinas)

        # Submenu Relatórios
        elif opt_menu == 4:
            # relatorios.submenu_relatorios()
            print(dados_prof_disc)
        
if __name__ == "__main__":
    main()
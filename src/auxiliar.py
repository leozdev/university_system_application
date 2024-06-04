import os

def existe_arquivo(nome):
    """
    Verifica se um arquivo existe.

    Parâmetros:
    nome (str): O nome do arquivo a ser verificado.

    Retorna:
    bool: True se o arquivo existe, False caso contrário.
    """
    if os.path.exists(nome):
        return True
    return False
    
def confirmar(acao):
    """
    Solicita confirmação para uma ação.

    Parâmetros:
    acao (str): A ação para a qual a confirmação está sendo solicitada.

    Retorna:
    bool: True se a ação for confirmada, False se não for.
    """
    while True:
        input_confirma = input(f"Tem certeza que deseja {acao} o cadastro? (S/N): ").upper()
        if input_confirma == "S":
            return True
        elif input_confirma == "N":
            return False
        else:
            print("Opção inválida!")

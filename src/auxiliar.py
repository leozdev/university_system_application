import os

def existe_arquivo(nome):
    if os.path.exists(nome):
        return True
    return False
    
def confirmar(acao):
    while True:
        input_confirma = input(f"Tem certeza que deseja {acao} o cadastro? (S/N): ").upper()
        if input_confirma == "S":
            return True
        elif input_confirma == "N":
            return False
        else:
            print("Opção inválida!")
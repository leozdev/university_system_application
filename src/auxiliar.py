import os

def existe_arquivo(nome):
    if os.path.exists(nome):
        return True
    
def confirmar(acao):
    while True:
        input_confirma = input(f"Tem certeza que deseja {acao} o cadastro? (S/N): ").upper()
        if input_confirma == "S":
            return True
        elif input_confirma == "N":
            # print(f"Ação de {acao} cancelada com sucesso!")
            return False
        else:
            print("Opção inválida!")
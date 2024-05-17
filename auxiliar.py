import os

def existe_arquivo(nome):
    if os.path.exists(nome):
        return True
    else:
        return False
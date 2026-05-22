from classes import Funcionario # Classe criada

# Ler dados do usuário e seu espaço utilizado em bytes
def ler_dados(caminho_arquivo: str)->list:

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        
        return [Funcionario(linha[:16].strip(), linha[16:].strip()) for linha in arquivo]
from reader import ler_dados
from transformation import transformar_dados
from writer import gerar_relatorio

CAMINHO_ENTRADA = 'data/input/usuarios.txt'
CAMINHO_SAIDA = 'data/output/relatorio.txt'

def main()->None:

    lista_funcionarios = ler_dados(CAMINHO_ENTRADA)
    lista_funcionarios = transformar_dados(lista_funcionarios)

    gerar_relatorio(CAMINHO_SAIDA, lista_funcionarios)

    print("O relatório foi gerado com sucesso!")

if __name__ == '__main__':
    main()
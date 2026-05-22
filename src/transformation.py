# Transformando o espaço de armazenamento de bytes para megabytes e taxa de ocupação
def transformar_dados(lista_funcionarios: list)->list:

    espaco_total_utilizado = sum(funcionario.espaco_bytes for funcionario in lista_funcionarios)

    for funcionario in lista_funcionarios:
        funcionario.bytes_megabytes() # Transforma bytes em megabytes
        funcionario.percentual(espaco_total_utilizado) # Calcula a taxa de ocupação

    return lista_funcionarios
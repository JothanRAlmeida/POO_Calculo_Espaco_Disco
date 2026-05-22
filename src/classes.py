class Funcionario:
    def __init__(self, nome: str, espaco_bytes: int):
        self.nome = nome
        self.espaco_bytes = int(espaco_bytes)
        self.espaco_megabytes = 0
        self.taxa_ocupacao = 0
    
    # Transforma bytes em megabytes
    def bytes_megabytes(self, valor_transformacao: int = 1048576):
        self.espaco_megabytes = self.espaco_bytes/valor_transformacao

    # Calcula a taxa de ocupação
    def percentual(self, espaco_total_utilizado):
        self.taxa_ocupacao = (self.espaco_bytes/espaco_total_utilizado)*100
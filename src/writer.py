# Escreve o relatório estruturado em novo arquivo .txt
def gerar_relatorio(caminho_saida: str, lista_usuarios: list)->None:

    with open(caminho_saida, 'w', encoding= 'utf-8') as arquivo:

        # Indice para preencher coluna com a ordem
        indice = 1

        # Cabeçalho do relatório
        arquivo.write(f"{'ACME Inc.':<20}Uso de espaço em disco pelos usuários\n")
        arquivo.write("-" * 72 + "\n")
        arquivo.write(f"{'Nr.':5}{'Usuários':<15}{'Espaço utilizado':<20}{'% do uso':<10}\n\n")

        # Escreve todos os usuários, a quantidade megabytes utilizados e a taxa de ocupação
        for usuario in lista_usuarios:
            
            arquivo.write(
                f"{indice:<5}"
                f"{usuario.nome.capitalize():<15}"
                f"{usuario.espaco_megabytes:>7.2f} MB"
                f"{usuario.taxa_ocupacao:>15.2f}%\n"
            )
            
            indice += 1
        
        # Final do relatório
        total_megabytes = sum(funcionario.espaco_megabytes for funcionario in lista_usuarios)
        ocupacao_media = total_megabytes/len(lista_usuarios)

        arquivo.write(f"\n\nEspaço total ocupado: {total_megabytes:.2f} MB")
        arquivo.write(f"\nEspaço médio ocupado: {ocupacao_media:.2f} MB")
# Programa que calcula e gera relatório com a taxa de ocupação de disco de usuários de uma empresa

## Descrição

A ACME Inc., uma empresa com aproximadamente 500 funcionários, estava enfrentando problemas de espaço em disco em seu servidor de arquivos. Para auxiliar na identificação dos usuários que mais consomem armazenamento, foi desenvolvido um programa capaz de gerar um relatório detalhado de utilização de disco.

O sistema utiliza como entrada um arquivo chamado `usuarios.txt`, contendo o nome dos usuários e a quantidade de espaço ocupado em bytes no servidor.

Nesta nova versão, o projeto foi refatorado utilizando **Programação Orientada a Objetos (POO)**, tornando o código mais organizado, reutilizável e de fácil manutenção.

Foi criada a classe `Funcionario`, responsável por representar cada usuário do relatório. A classe possui atributos relacionados ao funcionário e métodos específicos para:

* Converter bytes para megabytes
* Calcular a taxa de ocupação de disco

Com isso, a complexidade do código foi reduzida, melhorando significativamente a clareza e separação de responsabilidades da aplicação.

---

## Funcionalidades

O programa gera automaticamente um relatório contendo:

* Espaço utilizado por cada usuário em MB
* Percentual de uso individual
* Total de espaço utilizado
* Média de utilização dos usuários

---

## Conceitos Aplicados

* Programação Orientada a Objetos (POO)
* Classes e Objetos
* Encapsulamento de responsabilidades
* Manipulação de arquivos
* List Comprehension
* Formatação de strings
* Cálculos percentuais
* Conversão de unidades (Bytes → MB)

---

## 📂 Estrutura do Arquivo de Entrada

O arquivo `usuarios.txt` possui os dados no seguinte formato:

```txt
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
```

---

## 📄 Exemplo de Saída (`relatorio.txt`)

```txt
ACME Inc.           Uso de espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuários       Espaço utilizado    % do uso

1    alexandre       434.99 MB          16.11%
2    anderson       1187.99 MB          44.01%
3    antonio         117.74 MB           4.36%
4    carlos           87.03 MB           3.22%
5    cesar             0.94 MB           0.03%
6    rosemary        752.88 MB          27.89%
7    jothan          117.74 MB           4.36%

Espaço total ocupado: 2699.31 MB
Espaço médio ocupado: 385.62 MB
```

---

## Estrutura do Projeto

```bash
projeto/
│
├── data/
│   ├── input/
│   │   └── usuarios.txt
│   │
│   └── output/
│       └── relatorio.txt
│
├── src/
│   ├── __init__.py
│   ├── classes.py
│   ├── main.py
│   ├── reader.py
│   ├── transformation.py
│   └── writer.py
│
└── README.md
```

---

## Classe `Funcionario`

A classe criada no projeto centraliza toda a lógica relacionada aos usuários.

### Responsabilidades da classe

* Armazenar os dados do funcionário
* Converter o espaço utilizado de bytes para MB
* Calcular a porcentagem de ocupação no disco

Essa abordagem tornou o código mais modular, legível e escalável.

---

## Como Executar

1. Adicione o arquivo `usuarios.txt` dentro da pasta:

```bash
data/input/
```

2. Execute o programa:

```bash
python src/main.py
```

3. O relatório será gerado automaticamente em:

```bash
data/output/relatorio.txt
```

---

## Possíveis Melhorias Futuras

* Ordenar usuários por maior consumo de disco
* Exportar relatório para CSV
* Adicionar interface gráfica
* Ler arquivos `.csv`
* Criar testes automatizados
* Implementar logs da aplicação

---

## Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
# Repositório do projeto `TING (Trybe is not Google)` 📟

## Módulo: CIÊNCIA DA COMPUTAÇÃO

 Repositório possuí projeto desenvolvido no período que estive na **Trybe**, abordando conceitos de `algoritmo de busca`, `Nó`, `lista encadeada`, `Pilha` e `Fila`.

## Informações de aprendizados

- Este é um projeto desenvolvido para praticar `Python`;
- Utilizei o `Pytest` para fazer meus testes;
- Primeiro projeto utilizando `Fila`.

## Linguagens e ferramentas usadas

[![Git][Git-logo]][Git-url]
[![Python][Python-logo]][Python-url]
[![Pytest][Pytest-logo]][Pytest-url]

## O que foi desenvolvido

Neste projeto, implementei um programa que simula um algoritmo de indexação de documentos similar ao do Google. Ele é capaz de identificar ocorrências de termos em arquivos TXT.

Ele possui dois módulos:

- Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
- Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

## Habilidades trabalhadas

- Manipular Filhas;
- Manipular Deque;
- Manipular Nó & Listas Ligadas e;
- Manipular Listas Duplamente Ligadas.

## Instruções para instalar e rodar

<!-- <details> -->

1. Clone o repositório e entre na pasta:

    ```bash-shell
    git clone git@github.com:Ludson96/project-TING.git
    cd project-TING
    ```

1. Crie, ative e instale as dependências no ambiente virtual:

    ```bash-shell
    python3 -m venv .venv && source .venv/bin/activate
    python3 -m pip install -r dev-requirements.txt
    ```

1. Para rodar todos os testes utilize o comando:

    ```bash
    python3 -m pytest
    ```

1. Para rodar apenas em um arquivo:

    ```bash-shell
    python3 -m pytest <path do arquivo>
    ```

<!-- </details> -->

<!-- ## Detalhamento das funções

Abaixo está uma lista das funções disponíveis.

<!-- <details> -->

<!-- ### `study_schedule(permanence_period, target_time)`

- localizado em `challenges/challenge_study_schedule.py`

Essa função recebe uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída e um numero inteiro (`target_time`) que será o objetivo  de tempo a ser analisado como parâmetro, retorna a quantidade de pessoas estudantes estavam no sistema neste horário.

Exemplo de uso:

```python
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
students_quantity = study_schedule(permanence_period, 5)
```

Exemplo de retorno:

```md
# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
```

</details> -->

[Git-logo]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[Python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Pytest-logo]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/

# Sistema Completo de Atendimento e Análise

## Descrição

Sistema desenvolvido em Python para gerenciamento de atendimentos em uma clínica ou central de atendimento.

O sistema permite o cadastro de clientes e atendentes, controle de filas comuns e prioritárias, histórico de atendimentos, geração de relatórios e exportação de dados em CSV.

O projeto foi desenvolvido para aplicar conceitos de Estruturas de Dados e Algoritmos, incluindo filas, pilhas, listas encadeadas, busca binária, recursão e ordenação.

---

## Funcionalidades

### Clientes

* Cadastro de clientes
* Busca de clientes
* Remoção de clientes inativos
* Controle de prioridade

### Atendentes

* Cadastro de atendentes
* Listagem de atendentes

### Atendimentos

* Abertura de atendimento
* Fila comum
* Fila prioritária
* Chamada do próximo cliente
* Finalização de atendimento
* Histórico de atendimentos

### Relatórios

* Tempo médio de atendimento
* Top 5 clientes mais atendidos
* Exportação para CSV

### Recursos Extras

* Persistência em arquivos JSON
* Desfazer última finalização utilizando pilha
* Busca binária por ID
* Contagem recursiva de clientes ativos

---

## Estruturas de Dados Utilizadas

### Vetor (Lista Python)

Utilizado para armazenamento temporário de registros e geração de relatórios.

Complexidade:

* Inserção: O(1)
* Busca: O(n)

### Busca Binária

Utilizada para localizar clientes por ID em listas ordenadas.

Complexidade:

* Busca: O(log n)

### Fila Comum

Utilizada para clientes sem prioridade.

Complexidade:

* Inserção: O(1)
* Remoção: O(1)

### Fila Prioritária

Utilizada para clientes prioritários.

Complexidade:

* Inserção: O(1)
* Remoção: O(1)

### Pilha

Utilizada para desfazer a última finalização de atendimento.

Complexidade:

* Push: O(1)
* Pop: O(1)

### Lista Encadeada

Utilizada para armazenar clientes ativos.

Complexidade:

* Inserção: O(n)
* Busca: O(n)
* Remoção: O(n)

### Recursão

Utilizada para contagem de clientes ativos na lista encadeada.

---

## Estrutura do Projeto

SistemaAtendimento/

├── main.py

├── README.md

├── requirements.txt

├── data/

│ ├── clientes.json

│ ├── atendentes.json

│ └── atendimentos.json

├── models/

│ ├── cliente.py

│ ├── atendente.py

│ └── atendimento.py

├── services/

│ ├── cliente_service.py

│ ├── atendente_service.py

│ ├── atendimento_service.py

│ └── relatorio_service.py

├── structures/

│ ├── binary_search.py

│ ├── linked_list.py

│ ├── priority_queue.py

│ ├── queue.py

│ └── stack.py

├── utils/

│ └── file_manager.py

└── tests/

---

## Como Executar

### Clonar o repositório

git clone <url-do-repositorio>

### Entrar na pasta

cd SistemaAtendimento

### Executar

python main.py

---

## Arquivos de Dados

Os dados são armazenados automaticamente em arquivos JSON localizados na pasta:

data/

* clientes.json
* atendentes.json
* atendimentos.json

---

## Requisitos

* Python 3.10 ou superior

---

## Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Estruturas de Dados e Algoritmos.

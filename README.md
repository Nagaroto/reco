# RECO — Reconnaissance Tool

Ferramenta de reconhecimento desenvolvida em Python, voltada à identificação de caminhos e possíveis subdomínios por meio de wordlists.

O RECO foi desenvolvido para atuar na etapa de reconhecimento de aplicações web, utilizando listas de palavras para explorar diferentes possibilidades de caminhos e estruturas de domínio.

## Funcionalidades

### 1. Path Reconnaissance

Realiza a identificação de possíveis caminhos e diretórios existentes em uma aplicação web.

A ferramenta trabalha com wordlists, incluindo listas disponibilizadas pelo projeto SecLists, para testar diferentes rotas e identificar respostas HTTP relevantes.

Exemplo de possibilidades investigadas:

```text
https://host.com/admin
https://host.com/dashboard
https://host.com/api
https://host.com/backup
```

### 2. DNS Reconnaissance

Realiza a investigação de possíveis subdomínios utilizando wordlists específicas.

Para cada palavra da lista, a ferramenta constrói duas variações de domínio:

**Primeira estrutura:**

```text
admin.host.com
dev.host.com
api.host.com
```

**Segunda estrutura:**

```text
host.admin.com
host.dev.com
host.api.com
```

O reconhecimento DNS tende a ser uma das etapas mais demoradas, principalmente devido ao tamanho das wordlists utilizadas e à quantidade de combinações testadas.

A ferramenta utiliza requisições HTTP para verificar as respostas dos domínios gerados.

> Observação: uma falha de conexão HTTP não significa necessariamente que o subdomínio não exista. Questões de DNS, TLS e disponibilidade do serviço também podem interferir nos resultados.

## Wordlists

O RECO utiliza wordlists externas, permitindo que o usuário escolha e substitua suas listas conforme a necessidade do reconhecimento.

As listas podem ser obtidas no projeto:

- [SecLists — GitHub](https://github.com/danielmiessler/SecLists)

Estrutura esperada:

```text
reco/
├── path.py
└── wordlist/
    ├── common.txt
    └── dns.txt
```

## Tecnologias utilizadas

- Python
- Requests
- Pathlib
- ThreadPoolExecutor
- Concurrent Futures
- Thread Local Storage

## Características do projeto

O RECO foi desenvolvido priorizando uma estrutura simples, de fácil compreensão e manutenção.

A organização do código busca facilitar:

- Modificações nas funcionalidades existentes.
- Inclusão de novas modalidades de reconhecimento.
- Substituição e inclusão de wordlists.
- Otimizações futuras de desempenho.
- Expansão gradual da ferramenta.

## Desenvolvimento contínuo

O RECO é um projeto em desenvolvimento de longo prazo.

Sua estrutura foi pensada para permitir melhorias progressivas, sem tornar o código excessivamente complexo ou dificultar futuras manutenções.

Novas funcionalidades e modalidades de reconhecimento poderão ser incorporadas conforme a evolução do projeto.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Nagaroto/reco.git
```

Entre no diretório:

```bash
cd reco
```

Instale a dependência:

```bash
pip install requests
```

Execute:

```bash
python3 path.py
```

## Aviso de uso

Utilize o RECO somente em aplicações próprias, ambientes de laboratório ou sistemas para os quais você tenha autorização explícita para realizar testes.

---

**RECO — Reconhecimento, análise e evolução contínua.**

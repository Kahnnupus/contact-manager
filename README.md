# Projeto de Gerenciamento de Contatos.

Projeto de gerenciamento de contatos em Python, que permite adicionar, listar e remover contatos de uma lista.

## Funcionalidades

### main.py
 
 Este arquivo contém a lógica principal do programa. Oferece um menu interativo para o usuário realizar o gerenciamento dos contatos, como adicionar, lista e remover contatos.

 Exemplo de uso:
 
 ```bash
 python main.py
 ```

### contact_manager.py

Este arquivo contém as funções de gerenciamento de contatos, como adicionar, listar e remover contatos. Ele é importado pelo arquivo `main.py` para ser utilizado na lógica do programa.

## Funcionalidades Disponíveis

- Adicionar um novo contato.
- Listar todos os contatos cadastrados.
- Remover um contato existente.

## Estrutura do Projeto

- **main.py**: Contém a lógica principal do programa.
- **contact_manager.py**: Contém as funções de gerenciamento de contatos.

## Funcionalidades do Arquivo `contact_manager.py`

- `input_nome()`: Solicita e valida o nome do contato.
- `input_telefone(exibir)`: Solicita e valida o telefone do contato.
- `verificar_cadastro(telefone)`: Verifica se um telefone já está cadastrado.
- `adicionar()`: Adiciona um novo contato à lista.
- `listar()`: Lista todos os contatos cadastrados.
- `remover(telefone)`: Remove um contato da lista.

## Como Executar

Para executar o programa, basta rodar o arquivo `main.py` em um terminal:

```bash
python main.py
```
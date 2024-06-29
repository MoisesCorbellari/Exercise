# Criando um mini sistema
Mini sistema modularizado que permite cadastrar pessoas pelo nome e idade
em um arquivo de texto simples. O programa tem somente 2 opções: Cadastrar e Visualizar Cadastro.

## Funcionalidades - libs
### archive:
- clear(): limpa a tela do terminal.

- existe(doc): verifica se um arquivo existe no diretório atual.

- criar(nome): cria um novo arquivo de texto.

- ler(nome): lê e exibe o conteúdo de um arquivo de texto, formatado para mostrar nome e idade.

- cadastrar(arq, nome='desconhecido', idade=0): adiciona uma nova linha de dados no formato "nome - idade" ao final de um arquivo de texto existente.

### screen:
- leiaInt(prompt): solicita ao usuário um número inteiro a partir do prompt fornecido. Lida com exceções como valores inválidos e interrupções do teclado.

- linha(larg=70): retorna uma linha de caracteres '-' com o comprimento especificado (padrão é 70 caracteres).

- title(prompt): imprime um título centralizado entre linhas de caracteres '-'.

- menu(lista): exibe um menu numerado a partir de uma lista de opções e solicita ao usuário que escolha uma opção válida.


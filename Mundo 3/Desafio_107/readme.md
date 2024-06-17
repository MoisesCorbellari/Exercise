# Exercitando módulos em Python
Crie um módulo chamado moeda.py 
que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.

# Funcionalidades do desafio
### Módulo 'moeda.py':
- aumento(preco, taxa): aumenta o preco pela taxa percentual fornecida.
- diminuir (valor, taxa): Aumenta o valor pela taxa percentual fornecida.
- dobro(preco): retorna o dobro do valor informado.
- metade(preco): retorna a metade do valor informado.

### Programa 'info.py':
- importa o módulo moeda.
- solicita ao usuário um valor monetário e uma taxa percentual.
- valida as entradas para garantir que sejam números válidos e que a taxa não seja negativa.
- exibe o valor original, o dobro, a metade, o valor aumentado e o valor diminuído, utilizando as funções do módulo 'moeda.py'.
- usa cores para indicar entradas inválidas. Por exemplo, se o usuário inserir uma taxa negativa, a mensagem de erro será exibida em vermelho.

# Estrutura do desafio
- moeda.py: Contém as funções aumentar(), diminuir(), dobro() e metade().
- info.py: Programa principal que importa o módulo moeda e usa suas funções. Também inclui validação de entrada e uso de cores para indicar erros.

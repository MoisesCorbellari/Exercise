# Reduzindo ainda mais seu programa
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostra na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

## Funcionalidades do desafio
### Módulo moeda.py:
- aumento(preco, taxa): aumenta o preço pela taxa percentual fornecida.
- diminuir(preco, taxa): diminui o preço pela taxa percentual fornecida.
- dobro(preco): retorna o dobro do valor informado.
- metade(preco): retorna a metade do valor informado.
- coin(preco, coin='R$'): formata o preço como uma string monetária brasileira.
- tx(taxa): formata a taxa como uma string percentual brasileira.
- title(txt, larg=70): imprime um título centralizado com tamanho de largura fixa.

### Programa info.py:
- importa o módulo "moeda".
- solicita ao usuário um valor monetário e uma taxa percentual.
- valida as entradas para garantir que sejam números válidos e que a taxa não seja negativa.
- exibe o valor original, o dobro, a metade, o valor aumentado e o valor diminuído, utilizando as funções do módulo "moeda.py".
- usa cores para indicar entradas inválidas. Por exemplo, se o usuário inserir uma taxa negativa, a mensagem de erro será exibida em vermelho.

### Estrutura do desafio
- moeda.py: Contém as funções aumento(), diminuir(), dobro(), metade(), coin(), tx() e title().
- info.py: Programa principal que importa o módulo moeda e utiliza suas funções. Também inclui validação de entrada e uso de cores para indicar erros.
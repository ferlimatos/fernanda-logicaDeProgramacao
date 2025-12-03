## Conceito Básico e Estrutura

# Listas (ou list em Python) são um tipo de variável que permite armazenar uma coleção ordenada de vários valores.

# Conteúdo: Uma lista pode conter zero ou mais elementos. Esses elementos podem ser do mesmo tipo ou de tipos diferentes, incluindo números, strings, e até mesmo outras listas.

# Mutabilidade: Listas são mutáveis, o que significa que você pode alterar, adicionar ou remover elementos depois que a lista é criada

# Criação: Listas são criadas usando colchetes ([]).

## Índices e Acesso a Elementos

# O acesso a elementos em uma lista é feito através de seu índice (posição), que é um número inteiro.

# Início da Contagem: Os índices começam em zero (0). O primeiro elemento tem índice 0.
# Último Elemento: Em uma lista de tamanho N, o último elemento tem índice N-1.
# Índices Negativos: Permitem acessar elementos a partir do final da lista.
  # -1 é o último elemento.
  # -2 é o penúltimo, e assim por diante.

Z = [7,8,9]

## Tamanho e Fatiamento (Slicing)

### Tamanho da Lista
# A função len() retorna o número de elementos contidos na lista.
  # Uso: len(L)
  # Importante: O valor retornado por len(L) não pode ser usado como índice diretamente, mas é útil para definir o limite em laços de repetição (ex: while x < len(L):).

### Fatiamento (Slicing)
# O fatiamento permite que você acesse apenas uma parte (ou "fatia") da lista.
# Sintaxe: Lista[início : fim].
  ## O número à esquerda (início) indica a posição de início da fatia.
  ## O número à direita (fim) indica a posição de fim, mas o elemento nesta posição não é incluído (intervalo aberto).
# Omissão:
  # L[:2] - Vai do início até o índice 2 (não incluso).
  # L[1:] - Vai do índice 1 até o final da lista.
  # L[:] - Cria uma cópia rasa (independente) de todos os elementos da lista.

## Modificação da Estrutura da Lista (Adição e Remoção)

# Adição de Elementos 
  ## append() - L.append(n) - Adiciona um único elemento ao final da lista.
  ## + (concatenação) - L = L + [1] - Concatena duas listas, criando uma nova lista.
## extend() - L.extend([3, 4, 5]) - Adiciona elementos de outra lista ao final da lista, "estendendo-a".

## Remoção de Elementos
# A instrução del é usada para remover elementos.
  # del L[índice] - Remove o elemento na posição especificada. Os índices são reorganizados após a remoção.
  # del L[fatia] - Remove uma fatia inteira de elementos (ex: del L[1:99]).
  # L.pop(índice) - Retorna o valor do elemento e o remove da lista. Se nenhum índice for passado, ele remove o último elemento (comportamento de Pilha).

## Listas dentro de Listas
# Listas podem conter elementos de tipos diferentes, e isso inclui outras listas. Essa estrutura é conhecida como Lista de Listas e é útil para representar dados mais complexos (como matrizes ou registros).
# Acesso: Para acessar um elemento dentro de uma lista interna, você usa um segundo índice.
compras = [["maçã", 10, 0.30]]
print(compras[0][2])

## Listas como Estruturas de Dados Abstratas
# Listas podem simular estruturas de dados mais complexas ao seguir regras específicas para inserção e remoção de elementos:
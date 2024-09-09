"""
Coleções são entidades capazes de armazenar multiplos valores em uma única variável. 
Iremos ver os quatro principais tipos ou os mais utilizados em python sendo eles:

1 - List (Lista); 2 - Tuples (Tuplas); 3 - Sets (Conjuntos); 4 - Dictionaries (Dicionários)
"""

# Lista em python
frutas = ['Maça', 'Banana', 'Cereja']
print(type(frutas))
print(frutas[0])
print(len(frutas))

# Criando uma simples lista de frutas
frutas = ['maça', 'banana', 'abacate']
# Acessando os itens
print(frutas[0])  # maça
print(frutas[2])  # abacate
print(len(frutas))  # exibe o tamanha absoluto da lista - 3

"""
Em python, diferente de algumas linguagens, podemos acessar a partir
do último para o primeiro item, para isso usamos indices negativos iniciando em -1
por exemplo:
"""
frutas = ['maça', 'banana', 'abacate']
print(frutas[-1])  # abacate
print(frutas[-2])  # banana
print(frutas[-3])  # maça

"""
Em python também é possivel pegarmos um "pedaço" da lista, passando o intervalo
entre os dados, por exemplo:
"""
minha_lista = ["maça", "banana", "cereja",
               "laranja", "Banana", "melão", "manga"]
print(minha_lista[2:5])

"""
Algumas variações
Essa variação retorna os itens a partir do inicio ':' até o quarto item e não o
índice 4.
"""
minha_lista = ["maça", "banana", "cereja",
               "laranja", "Banana", "melão", "manga"]
print(minha_lista[:4])
# mesma coisa que
print(minha_lista[0:4])

"""
Essa variação retorna os itens APÓS o segundo item '2' até o
final da lista.
"""
minha_lista = ["maça", "banana", "cereja",
               "laranja", "Banana", "melão", "manga"]
print(minha_lista[2:])
# mesma coisa que
print(minha_lista[2:len(minha_lista)])

"""
Podemos verificar se há algum item específico na lista, por exemplo
"""
minha_lista = ["maça", "banana", "cereja",
               "laranja", "Banana", "melão", "manga"]
if "maça" in minha_lista:
    print("Sim, 'maça' está na lista")


# Manipulando itens em uma lista
# Criando uma lista vazia
frutas_vermelhas = []
print(frutas_vermelhas)

"""
Para adicionar itens a uma lista, é preciso utilizar uma função da própria estrutura
chamada como 'append'
"""
frutas_vermelhas = []
frutas_vermelhas.append("Morango")
frutas_vermelhas.append("Melancia")
frutas_vermelhas.append("Cereja")
frutas_vermelhas.append("Framboesa")
print(frutas_vermelhas[2])

# Alguns métodos de lista
# list.append(elem) -- adiciona um único elemento ao final da lista. Erro comum: não retorna a nova lista, apenas modifica o original.
# list.insert (index, elem) -- insere o elemento no índice dado, deslocando elementos para a direita.
# list.extend(list2) adiciona os elementos na lista2 ao final da lista. Usar + ou += em uma lista é semelhante ao uso de extensão().
# list.index(elem) -- pesquisa o elemento dado desde o início da lista e retorna seu índice. Lança um ValueError se o elemento não aparecer (use "in" para verificar sem um ValueError).
# list.remove(elem) -- pesquisa a primeira instância do elemento dado e remove-o (lança ValueError se não estiver presente)
# list.sort() -- classifica a lista no lugar (não a devolve). (A função classificada() mostrada posteriormente é a preferida.)
# list.reverse() -- inverte a lista no lugar (não a devolve)
# list.pop(index) -- remove e retorna o elemento no índice dado. Retorna o elemento mais certo se o índice for omitido (aproximadamente o oposto do apêndice()).

# Tuplas em python
minha_tupla = ("maça", "banana", "cereja")
print(minha_tupla)

"""
Para criar uma tupla com um item é preciso passar uma virgula, por exemplo:
"""
thistuple = ("maça",)
print(type(thistuple))

# Não é uma tupla
thistuple = ("maça")
print(type(thistuple))

"""
A captura dos valores por indices é similar a lista vista anteriormente. Por exemplo:
"""
thistuple = ("maça", "banana", "cereja")
print(thistuple[1])
print(thistuple[:2])
print(thistuple[-1])

# Atualizar tuplas (Alternativas)
"""
Converta a tupla em uma lista para poder alterá-la:
"""
x = ("maça", "banana", "cereja")
y = list(x)
y[1] = "Jabuticaba"
x = tuple(y)

print(x)


"""
Adicionar itens
"""
# 1° maneira - Converter para lista
x = ("maça", "banana", "cereja")
y = list(x)
y.append("laranja")
x = tuple(y)
print(x)

# 2° maneira - Adicione uma tupla a tupla
x = ("maça", "banana", "cereja")
y = ("abacate",)
x += y
print(x)


# Remover itens
minha_tupla = ("maça", "banana", "cereja")
y = list(minha_tupla)
y.remove("banana")
minha_tupla = tuple(y)

print(minha_tupla)


# Sets (conjunto) em python
conjunto = {"maça", "banana", "abacate"}
print(conjunto)

# Não permite dados duplicados
conjunto = {"maça", "banana", "cereja", "maça"}

print(conjunto)


# Adicionando valores
conjunto = {"maça", "banana", "abacate"}
conjunto.add("laranja")
print(conjunto)


# Adiciona outros conjuntos
conjunto = {"maça", "banana", "abacate"}
conjunto_fruntas_vermelhas = {"morango", "melancia"}
conjunto.update(conjunto_fruntas_vermelhas)
print(conjunto)


"""
Remover item de um conjunto com a função remove.
Caso não haja o valor, irá ser lançada uma exceção
"""
conjunto = {"maça", "banana", "abacate"}
conjunto.remove("banana")
print(conjunto)

"""
Remover item de um conjunto com a função discard.
Caso não haja o valor, NÃO irá ser lançada uma exceção
"""
conjunto = {"maça", "banana", "abacate"}
conjunto.discard("laranja")
print(conjunto)

"""
Para remover o último item de um conjunto basta utilizar o método pop()
"""
conjunto = {"maça", "banana", "abacate"}
conjunto.pop()
print(conjunto)
"""
Para esvaziar um conjunto basta utilizar o método clear()
"""
conjunto = {"maça", "banana", "abacate"}
conjunto.clear()
print(conjunto)


# Dicionário
"""

"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
print(dicionario)

"""
Os itens do dicionário são pedidos, mutáveis e não permitem duplicatas.
Os itens do dicionário são apresentados em pares de valor chave e podem ser referidos usando o nome da chave.
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
print(dicionario["modelo"])


"""
Valores duplicados não são permitidos
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964,
    "ano": 2020
}
print(dicionario)


"""
Para capturar algum valor é necessário passar a chave.
Para isso há duas formas de fazer
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
x = dicionario["modelo"]
print(x)

x = dicionario.get("modelo")
print(x)


"""
Podemos saber quais são as chaves de um dicionário
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
x = dicionario.keys()
print(x)


"""
Exemplo de alteração de valores
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
x = dicionario.keys()
print(x)  # Antes da ateração
dicionario["cor"] = "vermelho"  # Criando uma nova chave e atribuindo um valor
print(x)  # Depois da alteração


"""
Podemos também obter os valores contido em um dicionário
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
x = dicionario.values()
print(x)


"""
Podemos obter o conjunto de itens dentro de um dicionário
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
x = dicionario.items()
print(x)


"""
Verificar se a chave existe
"""
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
if "modelo" in dicionario:
    print("Sim, 'modelo' é uma das chaves")

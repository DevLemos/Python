# Tipos de Dados

## 1. Tipos Numéricos

### int

O tipo de dado `int(inteiro)` sem casas decimais, são positivos ou negativos.

```python
idade = 25
temperatura_negativa = -10
quantidade = 1000
```

### float

O tipo de dado `float (ponto flutuante)` são números com casas decimais.

```python
altura = 1.75
preco = 19.90
pi = 3.14159
```

### complex

O tipo de dado `complex (complexo)` são formados por número real (número normal) e uma parte imaginária (que usa a letra i). Geralmente utilizados em matemática/engenharia. Algumas linguagens de programação como o python adotou a letra `j` ao invés do `i` pois ele já é utilizado para representar a corrente elétrica. Enfim, final o j é equivalente ao i.

```python
numero_complexo = 3 + 5j
```

## 2. Tipo Texto

### str(string)

O tipo de dado `string` são sequência de caracteres, entre aspas simples ou duplas.

```python
nome = "Maria"
frase = 'Aprendendo Python'
multilinha = """Isso é
um texto
com várias linhas"""
```

## 3. Tipo Booleano

### bool

O tipo de dado `bool` representa verdadeiro ou falso, geralmente utilizado em condições.

```python
esta_chovendo = True
esta_estudando = False

# resultado de comparações também é bool
resultado = 10 > 5  # True
```

## 4. Tipos de Sequência

### list

O tipo de dados `list(lista)` é uma coleção ordenada e mutável (você pode alterar depois de criada). Usar para dados que mudam constantemente.

```python
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")  # dá pra adicionar itens
numeros = [1, 2, 3, 4]
```

### tuple

O tipo de dado `tuple(tupla)` são parecidas com a lista, mas imutável (não pode ser alterada depois de criada). Usar para dados fixos que representam uma única estrutura ou configuração.

```python
coordenadas = (10, 20)
dias_da_semana = ("segunda", "terça", "quarta")
```

### range

O tipo de dado `range` é uma sequência numérica imutável gerada de forma inteligênte. Ela não guarda todos os números na memória, apenas calcula o próximo quando necessário. Use quando for para repetir ações diversas vezes sem gastar memória.

```python
numeros = range(0, 10)  # de 0 até 9
```

## 5. Tipos de Mapeamento

### dict

O tipo de dado `dict(dicionário)` armazena os dados em pares de `chave:valor`. Ao contrário de list e tupla onde os dados são buscados por índices, no mapeamento você busca por uma chave única.

```python
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa["nome"])  # João
```

## 6. Tipos de Conjuntos

### set

O tipo de coleção `set` não é ordenada e contém apenas elementos únicos (sem repetição). Ele é mutável e você pode adicionar ou remover elementos depois de criado.

```python
numeros_unicos = {1, 2, 3, 3, 2}  # vira {1, 2, 3}
```

### frozenset

O tipo de coleção `frozenset` é igual ao set porém ele é imutável. Não permite adicionar ou remover elementos depois de criado.

```python
conjunto_fixo = frozenset({1, 2, 3})
```

## 7. Tipo Nulo

### NoneType

O tipo de dado `NoneType` representa nenhum valor, usado quando algo ainda não tem valor definido.

```python
resultado = None
```

## Tipos Binários

### bytes

O tipo `bytes` são sequência de bytes, imutável. Usado para representar dados binários, como conteúdo de arquivos, imagens ou texto codificado.

```python
dados_bytes = b"Exemplo de bytes"

frase_texto = "Olá, mundo!"
dados_bytes2 = frase_texto.encode("utf-8")
print(f"Dados em bytes (UTF-8): {dados_bytes2}") #b'Ol\xc3\xa1, mundo!'
```

### bytearray

O tipo `bytearray` é praticamente a mesma coisa que bytes porém mutável.

```python
dados_bytearray = bytearray(b"Exemplo de bytearray")
print(f"Dados em bytearray: {dados_bytearray}") #bytearray(b'Exemplo de bytearray')
dados_bytearray[0] = 79  # Modificando o primeiro byte (O)
print(f"Dados em bytearray após modificação: {dados_bytearray}") #bytearray(b'Oxemplo de bytearray')
print(f"Tipo de dado: {type(dados_bytearray)}")
```

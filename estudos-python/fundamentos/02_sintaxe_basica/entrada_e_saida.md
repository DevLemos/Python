# Entrada e Saída

## 1. Saída de dados

### print()

Em python utilizamos a função `print()` para mostrar textos, números ou resultados na tela do computador. O retorno sempre será do tipo `string`:

```python
print("Hello World!")
```

### Separador

A função `print()` tem um argumento chamado `sep` que funciona como um separador. Por padrão seu valor é `sep=" "`, mas no exemplo a seguir estamos utilizando `\n` para quebra de linha.

```python
print("L","e","m","o","s", sep="\n")
```

### end

`end` é um argumento da função `print()` que por padrão tem seu valor com `end="\n"`.

```python
print("Bem vindo aos estudos de Python", end=" ")
print("em 2026!")
```

Saída:

```
Bem vindo aos estudos de Python em 2026!
```

## 2. Entrada de dados

### input()

`ìnput()` é a função utilizada para coletar informações diretamente do usuário por meio do teclado.

### Converção/Casting

Para converter em um tipo específico podemos fazer da seguinte maneira como `int()`

```python
idade = int(input("Digite sua idade: "))
```

### f-symbols

Site utilizado neste exemplo para criar um texto customizado: `https://fsymbols.com`

## 3. f-string (interpolação de strings)

Em python para fazer interpolação de strings utilizamos a letra `f` em seguida com `{}` para cada valor. Exemplo:

```python
print(f"Você selecionou a opção: {entrada_usuario}")
```

## 4. Concatenação de Strings

```python
# Abordagem simples
print("Você selecionou a opção (concatenação): ", entrada_usuario )
# Abordagem com sinal de + (concatenação)
print("Você selecionou a opção (concatenação): " + entrada_usuario)
```

## 5.type

Função que retorna o tipo de dado (class) exato do objeto. Útil durante a depuração em tempo de execução, pois o python é uma linguagem de tipagem dinâmica.

```python
print(type(entrada_usuario))
print(type(idade))
```

## 6. Formatação de números

`:.2f` é uma específicação utilizada para formatar um número de ponto flutuante em uma string com exatamente duas casas decimais. Anatomia da sintaxe:

- `:` Separa a variável ou expressão de suas regras de formatação.
- `,` Formata dinâmicamente grande quantidades de moedas ou dados financeiros
- `.2` Especifica a precisão , ou seja, exatamente 2 dígitos devem ser exibidos após a vírgula decimal.
- `f` Especifica o tipo , o que significa que trata o valor como um número de ponto flutuante ( float).

Formas de utilizar:

```python
print(f"\nO valor de pi é: {pi:.2f}")
print("O valor de pi é: {:.2f}".format(pi))
print(f"O valor do preço é: {preco:,.2f}") #1,234,567.89
print(f"O valor do número inteiro é: {numero_inteiro:.2f}")
```

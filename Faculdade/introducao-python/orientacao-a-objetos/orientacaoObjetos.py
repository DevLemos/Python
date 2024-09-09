# Declarando uma classe em python
class Pessoa:
    pass


class Pessoa:
    idade = 20
    altura = 1.85
    nome = "Maria"


pessoa1 = Pessoa()
print(pessoa1.idade)
print(pessoa1.altura)
print(pessoa1.nome)


"""
O exemplo acima nos da um pequena introdução de sintaxe
contudo os valores fixos nao parecem ser interessando
quando criamos mais de uma pessoa.
De maneira genérica, uma classe dever servir como um molde
para um objeto, ou seja, a classe só serve para a definição
do que o objeto deve ser.
Para isso, em python, uma das maneiras de fazer é utilizar
uma função especial conhecida como __init__ (construtor/inicializar)
da classe.
Vamos ao exemplos:
"""


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


# Para instanciar a classe façamos o seguinte
pessoa1 = Pessoa('Maria', 25, 1.85)
print(pessoa1.idade)
print(pessoa1.altura)
print(pessoa1.nome)

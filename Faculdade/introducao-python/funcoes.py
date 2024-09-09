# Criando uma Função
def minha_funcao():
    print("Olá, sou uma função")


minha_funcao()

# Argumentos


def minha_funcao(parametro):
    print(parametro + " Testando")


minha_funcao("Juno")
minha_funcao("Tobias")
minha_funcao("Linus")


def soma(valor1, valor2):
    return valor1 + valor2


print(soma(5, 5))
print(soma(1, 2))
print(soma(3, 5))

# Funções lambdas
# x = lambda a : a * 2


def x(a): return a * 2


print(x(5))


def x(a, b): return a + b


print(x(5, 10))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))


def funcao(n):
    return lambda a: a * n


dobro = funcao(2)
triplo = funcao(3)

print(dobro(11))
print(triplo(11))

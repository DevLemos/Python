# Operadores Aritméticos
resultado = 10 / 3
print(resultado)
print(10 % 3)
print(5//2)


"""
Exemplos de operações matemáticas.
Python segue a regra de hierárquia entre as operações.
() > /,* > +, -
Segue o exemplo abaixo
x = a + b * c
Por prioridade a multiplicação vem antes da adição
x = a / b * c
Como divisão e multiplicação possuem a mesma prioridade
a próxima regra é realizar a operação da esquerda para a direita
logo a / b será realizado primeiro
Para alterar a ordem, por exemplo do exemplo acima, é necessário utilizar
parenteses. Por exemplo:
x = a / (b * c)
"""
hora = 2
minutos = 12

# Adição
print(20 + 32)
# Multiplicação com Subtração
print(hora * 60 - minutos)
# Divisão
print(minutos / 60)
# Exponenciação
print(5 ** 2)

# Equações em geral
print((5 + 9) * (15 - 7))

# Mais exemplos
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3)
print(3 ** 2)

# Operadores de atribuição
# Igual x == y
# Não Igual  x != y
# Maior do que x > y
# Menor do que x < y
# Maior do que ou igual a x >= y
# Menor do que ou igual a x <= y

# Operadores lógicos
# Retorna verdadeiro SE TODAS as declarações são verdadeira and (e)  x < 5 and x < 10
# Retorna verdadeiro SE AO MENOS UMA das declarações for verdadeira or (ou) x < 5 or x < 10
# Retorna o resultado inverso SE resultado for verdade ele retorna falso not (não) not(x < 5 and x < 10)

# Operadores de identidade
# is       Retorna verdadeiro (True) se ambas as varíaveis são o mesmo objeto x is y
# is not   Retorna verdadeiro (True) se ambas as varíaveis **NÃO** são o mesmo objeto x is not y

# Operadores de associação
# in      Retorna verdadeiro (True) se a sequencia específica contém no objeto  x in y
# in not  Retorna verdadeiro (True) se a sequencia específica NÃO contém no objeto x in not y

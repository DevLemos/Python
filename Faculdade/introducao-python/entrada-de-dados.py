"""
Pedindo valores ao usuário (entrada de dados através do teclado)
"""
# A função usada será o input
usuario = input("Informe seu usuário: ")
senha = input("Informe sua senha: ")
print(f'Seu usuário é {usuario}')
print(f'Sua senha é {senha}')


"""
Observação, por padrão os dados capturados pela função input() serão todos do tipo str(),
devido a isso, dependendo da aplicabilidade deverá ser feita uma conversão explicita, 
como mostrado a seguir
"""
# A função usada será o input
valor1 = input("Informe um valor numérico: ")
# Captura o tipo da variável
print(f'O tipo {type(valor1)
                } diz que o valor é uma sequência de carecteres (string)')

"""
Não é possível realizar cálculo numérico em python com valores do tipo str, dessa forma
temos que realizar uma conversão explicita usando as classes dos tipos. Vejamos a 
seguir um exemplo:
"""
# Suponhamos que gostariamos de saber o dobro do valor informado
valor1 = input("Informe um valor numérico: ")
# Captura o tipo da variável
print(f'O tipo {type(
    valor1)} sendo assim não é possível realizar cálculo numérico sem converter)')

# Para isso temos que realizar uma conversão basta usarmos o tipo da variável
valor1 = int(valor1)
print(valor1 * 2)

# Podemos simplificar passando em somente uma linha
valor1 = int(input("Informe um valor:"))
# ou
print(int(input("Informe um valor numérico: ")) * 2)

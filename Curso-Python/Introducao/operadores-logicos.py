# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

if 1 and 1:
    print(True and 1 and False)  # false
else:
    print('false')


# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

print(not True)  # False
print(not False)  # True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')

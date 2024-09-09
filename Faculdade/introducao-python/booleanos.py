# Booleanos
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b é maior que a")
else:
    print("b não é maior que a")

# A maioria dos valores são verdadeiros, por exemplo
# Com erxceção de string vazias, qualque string é verdadeiro
# Qualque número, exceto o zero, são verdadeiros
# qualquer lista, tupla, conjunto e dicionário são verdadeiro
print(bool("abc"))
print(bool(123))
print(bool(["Texto", "Rosa", "Bala"]))
print(bool(("nome", "idade")))

# falso
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Verifica se x é do tipo int
x = 200
print(isinstance(x, int))

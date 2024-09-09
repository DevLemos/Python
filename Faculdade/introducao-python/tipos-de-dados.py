# Tipos de dados Python
"""
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
"""

x = 5
print(type(x))

# Com str
print(type('Esse e um string.'))
print(type("E esse tambem eh um string."))
print(type("""e esse."""))
print(type('''e mesmo esse...'''))

# Conversão de tipo de dados
print(3.14, int(3.14))  # Isto não arredonda para o inteiro mais próximo
print(3.9999, int(3.9999))
print(3.0, int(3.0))  # Observe que o resultado está mais próximo de zero
print(-3.999, int(-3.999))

# Int
x = int(1)   # x irá se transformar em 1
y = int(2.8)  # y irá se transformar em 2
z = int("3")  # z irá se transformar em 3

# Float
x = float(1)     # x irá se transformar em 1.0
y = float(2.8)   # y irá se transformar em 2.8
z = float("3")   # z irá se transformar em 3.0
w = float("4.2")  # w irá se transformar em 4.2

# String
x = str("s1")  # x irá se transformar em 's1'
y = str(2)    # y irá se transformar em '2'
z = str(3.0)  # z irá se transformar em '3.0'

# Arredondar valores flutuantes
soma = 0.1 + 0.2
print(soma)
print("%.2f" % soma)
print(round(soma, 2))
print("{0:.2f}".format(soma))

"""
Definindo o tipo de dados No Python, o tipo de dados
é definido quando você atribui um valor a uma variável:
"""
x = "Hello World"  # str
x = 20  # int
x = 20.5  # float
x = 1j  # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview

x = bytearray(5)
print(x)

# Números em python

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# números int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# números float
x = 1.10
y = 1.0
z = -35.59
a = 35e3
b = 12E4
c = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

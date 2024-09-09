# Exemplos de string
print("Hello")
print('Hello')

# multilinhas
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String são vetores
for i in "Olá, mundo!":
    print(i)

# Comprimentos string
a = "Hello, world"
print(len(a))

# Verificação da string
txt = "Estamos na aula de introdução ao python"
print("aula" in txt)
if "aula" in txt:
    print("A palavra existe no texto")

if "aula" not in txt:
    print("A palavra não existe no texto")

# Cortes de texto
b = "Olá, mundo!"
print(b[2:5])  # Corte de um pedaço do texto
print(b[:5])  # Corte do inicio
print(b[2:])  # Corte até o fim
print(b[-5:-2])

# Modificação de string
a = "  Olá, mundo!  "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("O", "P"))
print(a.split(","))

# Concatenar string
a = "Olá"
b = "mundo"
c = a + b
print(c)
c = a + " " + b
print(c)

# Formatar texto
idade = 36
txt = "Meu nome é José, e tenho " + str(idade)
print(txt)
print(txt.format(idade))

quantidade = 3
numero_item = 567
preco = 49.95
ordem = "Eu quero {} peças do item {} pelo preço de {} reais."
print(ordem.format(quantidade, numero_item, preco))
ordem = "Eu quero pagar {2} reais em {0} peças do item {1}."
print(ordem.format(quantidade, numero_item, preco))

# Outras funções de string

# capitalize()	Converter o primeiro caracter para caixa alta
print("função capitalize".capitalize())
# casefold()	Converte uma string para minusculo
print("FUNÇÃO CASEFOLD".casefold())
# center()	Retorna a string centralizada
print("centraliza o texto".center(50))
# count()	Returna o numero de vezes que um valor ocorre
print("Numero de ocorrencias de uma palavra".count('a'))
# encode('')	Returna a codificação da string
print("Ocorrencias de letras".encode())
# endswith()	Returna verdadeiro se a string termina com um determinado valor
print('Essa string termina com o'.endswith('o'))
# expandtabs()	Sets the tab size of the string
print("Exemplo de expandtabs  ".expandtabs(2))
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

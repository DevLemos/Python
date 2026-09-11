# region Numéricos
# inteiros (int)

idade: int = 23
print("================== Int ==================")
print(f"Idade: {idade}")
print(f"Tipo de dado: {type(idade)}")
print("==========================================")

# números de ponto flutuante (float)
altura: float = 1.75
peso: float = 70.5
print("================== float ==================")
print(f"Altura: {altura}")
print(f"Peso: {peso}")
print(f"Tipo de dado: {type(altura)}")
print("==========================================")

# números complexos (complex)
numero_complexo: complex = 2 + 3j
numero_complexo_funcao = complex(2, 3)
print("================== complex ==================")
print(f"Número complexo: {numero_complexo}")
print(f"Número complexo (função): {numero_complexo_funcao}")
print(f"Tipo de dado: {type(numero_complexo)}")
print("==========================================")
# endregion

# region Booleanos
# Booleanos em Python
ativo: bool = True
usuario_logado: bool = False

print("================== Boolean ==================")
print(f"Ativo: {ativo}")
print(f"Tipo de dado: {type(ativo)}")
print("==========================================")

print(f"Usuário logado: {usuario_logado}")
print(f"Tipo de dado: {type(usuario_logado)}")
print("==========================================")
# endregion

# region Strings
nome: str = "Rodrigo"
sobrenome: str = "Silva"
texto: str = """
Esse é um texto
com várias linhas
e pode conter "aspas duplas" e 'aspas simples' sem problemas.
"""
print("================== String ==================")
print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Texto: {texto}")
print(f"Tipo de dado: {type(nome)}")
print("==========================================")
# endregion

# region None (equivalente ao null)
valor: None = None
print("================== None ==================")
print(f"Valor: {valor}")
print(f"Tipo de dado: {type(valor)}")
print("==========================================")
# endregion

# region Listas
frutas: list[str] = ["maçã", "banana", "laranja"]
print("================== List ==================")
print(f"Frutas: {frutas}")
print(f"Primeira fruta: {frutas[0]}")

frutas.append("uva")
print(f"Frutas após adicionar uva: {frutas}")
frutas[0] = "abacaxi"
print(f"Primeira fruta: {frutas[0]}")
print(f"Frutas atualizadas: {frutas}")
print(f"Tipo de dado: {type(frutas)}")
print("==========================================")
# endregion

# region Tuplas
cordenada: tuple[int, int] = (10, 20)
print("================== Tuple ==================")
print(f"Cordenada: {cordenada}")
print(f"Primeiro valor da cordenada: {cordenada[0]}")

try:
    cordenada[0] = 50  # type: ignore
    print(f"Primeiro valor da cordenada após modificação: {cordenada[0]}")
except TypeError as e:
    print(f"Erro ao tentar modificar a tupla: {e}")

print(f"Tipo de dado: {type(cordenada)}")
print("==========================================")
# endregion

# region range
numeros: range = range(5)
print("================== Range ==================")
print(f"Números: {list(numeros)}")
numeros = range(1, 10, 2)
print(f"Números com passo 2: {list(numeros)}")
print("==========================================")
# endregion

# region Sets
linguagens: set[str] = {"Python", "Java", "C++"}
print("================== Set ==================")
print(f"Linguagens: {linguagens}")
linguagens.add("JavaScript")
print(f"Linguagens após adicionar JavaScript: {linguagens}")
linguagens.add("Python")  # Não adiciona duplicatas
print(f"Linguagens após tentar adicionar Python novamente: {linguagens}")
print(f"Tipo de dado: {type(linguagens)}")
print("==========================================")
# endregion

# region Frozenset
linguagens_fixas: frozenset[str] = frozenset(linguagens)
print("================== Frozenset ==================")
print(f"Linguagens fixas: {linguagens_fixas}")
print(f"Tipo de dado: {type(linguagens_fixas)}")
print("==========================================")
# endregion

# region Dictionary
pessoa: dict[str, str | int] = {"nome": "Rodrigo", "idade": 30, "cidade": "São Paulo"}
print("================== Dictionary ==================")
print(f"Pessoa: {pessoa}")
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")
print("Adicionando um novo campo 'profissão'...")
pessoa["profissão"] = "Desenvolvedor"
print(f"Pessoa após adicionar profissão: {pessoa}")
print(f"Tipo de dado: {type(pessoa)}")
print("==========================================")
# endregion

# region Bytes

dados_bytes: bytes = b"Exemplo de bytes"
print("================== Bytes ==================")
print(f"Dados em bytes: {dados_bytes}")
print(f"Tipo de dado: {type(dados_bytes)}")

frase_texto: str = "Olá, mundo!"
dados_bytes2: bytes = frase_texto.encode("utf-8")
print(f"Dados em bytes (UTF-8): {dados_bytes2}")
print(f"Tipo de dado: {type(dados_bytes2)}")
print("==========================================")
# endregion

# region Bytearray
dados_bytearray: bytearray = bytearray(b"Exemplo de bytearray")
print("================== Bytearray ==================")
print(f"Dados em bytearray: {dados_bytearray}")
dados_bytearray[0] = 79  # Modificando o primeiro byte (O)
print(f"Dados em bytearray após modificação: {dados_bytearray}")
print(f"Tipo de dado: {type(dados_bytearray)}")
print("==========================================")
# endregion

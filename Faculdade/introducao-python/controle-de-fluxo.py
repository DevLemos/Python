# Controle de fluxo
a = 33
b = 200
if b > a:
    print("b é maior do que a")


# Se um número é positivo, iremos exibi-lo.
num = 3
if num > 0:
    print(num, "É positivo.")
print("Isso sempre irá ser impresso.")

num = -1
if num > 0:
    print(num, "É positivo.")
print("Isso sempre irá ser impresso.")

# Elif
a = 33
b = 33
if b > a:
    print("b é maior do que a")
elif a == b:
    print("a e b são iguais")

# Negativo e zero exibir uma mensagem apropriada
num = int(input('Informe um valor: '))

if num > 0:
    print("Número positivo")
elif num == 0:
    print("Zero")
else:
    print("Número negativo")

# while loops
i = 0
while i < 6:
    print(i)
    i += 1
    # i++
    # ++i

# for loops
nomes = ['Luis', 'Roberta', 'Lais']
contador = 0
for nome in nomes:
    contador += 1
    if nome == 'Roberta':
        print(nome)
        print(contador)

frutas = ["maça", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

nome = "Luis"
for letra in nome:
    print(letra)

frutas = ["maça", "cereja", "banana", "melão"]
for fruta in frutas:
    if fruta == "banana":
        break
    print(fruta)

frutas = ["maça", "cereja", "banana", "melão"]
for fruta in frutas:
    if fruta == "cereja":
        continue
    print(fruta)

for valor in range(3, 10, 3):
    print(valor)

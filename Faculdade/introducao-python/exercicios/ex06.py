# Realize a somatória de todos os números pares entre 0 e 99
soma = 0
for valor in range(100):
    if valor % 2 == 0:
        soma = soma + valor
print(soma)

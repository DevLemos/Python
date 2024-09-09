# Exercício de adivinhação

import random as rd

valorParaAdivinhar = rd.randint(10, 50)
print(valorParaAdivinhar)
numeroTentativas = 0
# repetir enquanto for menor do que 3
while numeroTentativas <= 3:
    if numeroTentativas == 3:
        print('*****Perdeu 🙁***')
        break
    valorInformado = int(input("Digite um valor: "))
    print(valorInformado)

    if valorParaAdivinhar == valorInformado:
        print('*****Ganhou 😀***')
        break
    numeroTentativas += 1

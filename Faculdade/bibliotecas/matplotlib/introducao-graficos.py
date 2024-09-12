import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/monitoramento_tempo.txt')

print(df.head(), '\n')
print(df.info(), '\n')

df['data'] = pd.to_datetime(df['data'])

print(df.info(), '\n')

# Adicionar novos indices
fig = plt.figure(figsize=(15, 8))

eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3])

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color='green')
eixo.set_xlim(datetime.datetime(2014, 5, 1),
              datetime.datetime(2014, 6, 1))  # Apenas maio/14
eixo.set_ylim(0, 50)  # eixo y de 0 a 50
eixo.set_title('Temperatura em Maio/2014', fontsize=25, pad=20)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['Temperatura'], loc='lower right', fontsize=15)

eixo2.grid(True)
eixo2.plot(df['data'], df['temperatura'], color='b')
eixo2.set_xlim(datetime.datetime(2014, 1, 1),
               datetime.datetime(2015, 1, 1))  # Apenas 2014
eixo2.legend(['Temperatura'], loc='lower right')
eixo2.set_title('Temperatura 2014', fontsize=15)

plt.show()

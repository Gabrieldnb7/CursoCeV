# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
### Na aula de resolução, foi apresentado uma biblioteca chamada de "operator" em que pegamos a função "itemgetter" para ordernar nosso dicionário colocando em outro dicionário
from random import randint
from time import sleep
dicionário = {}
maior = 0
for jogos in range(1, 5):
    jogador = randint(1, 6)
    dicionário[f'Jogador{jogos}'] = jogador
print('Valores sorteados: ')
sleep(1)
for keys, values in dicionário.items():
    print(f'    O {keys} tirou {values}')
    sleep(1)
print('=' * 50)
ranking = dict()
ranking = sorted(dicionário.items(), key=lambda item: item[1], reverse=True)
print(f'{"Ranking dos Jogadores":^50}')
print('=' * 50)
for índice, valor in enumerate(ranking):
    print(f'    {índice+1}º lugar: = {valor[0]} com {valor[1]}')
    sleep(1)
print('='*50)
'''for chaves, valores in dicionário.items():
    if chaves == 'Jogador1':
        maior = dicionário['Jogador1']
    else:
        if dicionário.values() > maior:
            maior = dicionário['']'''

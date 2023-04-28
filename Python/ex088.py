# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, Cadastrando tudo em uma lista composta.
from time import sleep
from random import randint
print('-' *50)
print(f'{"Sorteador de números da MegaSENA":^50}')
print('-' *50)
sorteio = []
jogos = []
quantidade = int(input('Quantos jogos você quer fazer? '))
print(f'{"Sorteando..."}')
for c in range(0, quantidade):
    while True:
        número = randint(1,60)
        if número not in sorteio:
            sorteio.append(randint(1,60))
        if len(sorteio) >= 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
for índice, lista in enumerate(jogos):
    print(f'Jogo {índice+1} = {lista}')
    sleep(1)

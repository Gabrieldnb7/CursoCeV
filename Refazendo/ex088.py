from random import randint
from time import sleep
megasena = []
jogo = []
print('='*35)
print(f'{"Gerador de jogos da MEGA SENA":^35}')
print('='*35)
quantidade = int(input('Quantos jogos você quer gerar? '))
for palpite in range(0,quantidade):
    for números in range(0,6):
        if números not in jogo:
            jogo.append(randint(1,60))
    jogo.sort()
    megasena.append(jogo[:])
    jogo.clear()
print('Os jogos gerados foram: ')
for index,jogos in enumerate(megasena):
    print(f'Jogo {index+1}: {jogos}')
    sleep(1)
print(f'{"Boa sorte":=^35}')

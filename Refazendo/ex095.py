# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
# Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes de aproveitamento do jogador.
jogadores = list()
dicionário = dict()
gols = list()
while True:
    gols.clear()
    dicionário.clear()
    total = 0
    dicionário['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {dicionário["Nome"]} jogou? '))
    for partida in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))
    dicionário['Gols'] = gols[:]
    for gol in gols:
        total += gol
    dicionário['Total'] = total
    jogadores.append(dicionário.copy())
    while True:
        resposta = str(input('Quer continuar?[S/N] ')).strip()[0]
        if resposta in 'SsNn':
            break
        else:
            resposta = str(input('Erro! Digite somente S ou N.'))
    if resposta in 'Nn':
        break
print('=' * 40)
print('Código', end=' ') # Cabeçalho
for indice in dicionário.keys():
    print(f'{indice:<15}', end=' ')
print()
for chave, valores in enumerate(jogadores):
    # print(f'{indice:<5} {valor["Nome"]:<10}{str(valor["Gols"]):^15}{valor["Total"]:>5}')
    print(f'{chave:<6}',end='')
    for valor in valores.values():
        print(f'{str(valor):<15}', end='')
    print()
while True:
    opção = int(input('Mostrar dados de qual jogador?[999 interrompe] '))
    if opção == 999:
        break
    if opção <= len(jogadores):
        print(f'O jogador {jogadores[opção]["Nome"]} jogou {len(jogadores[opção]["Gols"])} partidas.')
        for indice, valor in enumerate(jogadores[opção]["Gols"]):
            print(f'    Na partida {indice+1} fez {valor} gols.')
    else:
        print(f'Erro! Não existe jogador com o código {opção}.')
print('Fim')

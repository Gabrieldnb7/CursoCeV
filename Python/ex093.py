# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
dicionário = {}
gols = []
total = 0
dicionário['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o(a) {dicionário["Nome"]} jogou? '))
for jogo in range(0, partidas):
    gols.append(int(input(f'Quantos gols no {jogo+1}º jogo? ')))
    dicionário['Gols'] = gols[:]
for valor in gols: #Pode ser substituido por dicionario['Total'] = sum(gols)
    total += valor
dicionário['Total'] = total
print('='*50)
print(dicionário)
print('='*50)
for chaves, valores in dicionário.items():
    print(f'    O campo {chaves} tem valor {valores}')
print('='*50)
print(f'O jogador {dicionário["Nome"]} jogou {len(dicionário["Gols"])} partidas.')
for indice, valor in enumerate(dicionário["Gols"]):
    print(f'    Na partida {indice+1}, fez {valor} gols.')
print(f'O total foi de {dicionário["Total"]} gols.')

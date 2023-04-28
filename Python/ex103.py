# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.
def ficha(nome="<desconhecido>", gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


jogador = str(input('Nome do jogador: '))
placar = str(input('Quantos gols: '))
if placar.isnumeric():
    placar = int(placar)
else:
    placar = 0
if jogador.strip() == '':
    ficha(gols=placar)
else:
    ficha(jogador,placar)

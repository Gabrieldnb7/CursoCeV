import random
print('Jogo do Pedra, papel ou tesoura')
jogador = input(str('Pedra, papel ou tesoura? '))
computador = random.choice(['pedra', 'papel', 'tesoura'])
print('O computador escolheu {}!'.format(computador))
if jogador == 'pedra' and computador == 'tesoura':
    print('O jogador ganhou!')
elif jogador == 'pedra' and computador == 'papel':
    print('O computador ganhou!')
elif jogador == 'pedra' and computador == 'pedra':
    print('Empate! ambos escolheram Pedra.')
elif jogador == 'papel' and computador == 'pedra':
    print('O jogador ganhou!')
elif jogador == 'papel' and computador == 'papel':
    print('Empate! ambos escolheram papel.')
elif jogador == 'papel' and computador == 'tesoura':
    print('O computador ganhou!')
elif jogador == 'tesoura' and computador == 'pedra':
    print('O computador ganhou!')
elif jogador == 'tesoura' and computador == 'papel':
    print('O jogador ganhou!')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('Empate! ambos escolheram tesoura.')
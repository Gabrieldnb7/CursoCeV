import random
#from time import sleep
print(f'{"JOKENPO":^25}')
jogador = str(input('Pedra, papel ou tesoura? ')).strip().lower()
computador = random.choice(['pedra', 'papel', 'tesoura'])
print(f'O computador escolheu {computador}!')
if jogador == 'papel' and computador == 'pedra':
    print('Você ganhou!')
elif jogador == 'papel' and computador == 'tesoura':
    print(f'O computador ganhou!')
elif jogador == 'papel' and computador == 'papel':
    print('Empate!')
elif jogador == 'pedra' and computador == 'papel':
    print(f'O computador ganhou!')
elif jogador == 'pedra' and computador == 'tesoura':
    print('Você ganhou!')
elif jogador == 'pedra' and computador == 'pedra':
    print('Empate!')
elif jogador == 'tesoura' and computador == 'pedra':
    print(f'O computador ganhou!')
elif jogador == 'tesoura' and computador == 'papel':
    print('Você ganhou!')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('Empate!')

from random import randint
computador = randint(0,5)
escolha = int(input('Qual é seu palpite entre 0 e 5? '))
print(f'O computador escolheu o número {computador}.')
if escolha == computador:
    print(f'Parabéns, você ganhou!')
else:
    print(f'Você perdeu! Tente novamente.')
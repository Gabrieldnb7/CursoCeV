from random import randint
computador = randint(0,10)
print('Seu computador pensou em um número de 0 a 10.\n Consegue adivinhar qual?')
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Qual é o seu palpite? '))
    palpites +=1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
            # elif poderia ser um else
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

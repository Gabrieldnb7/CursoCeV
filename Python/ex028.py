from random import randint
ia = randint(0, 5)
num = int(input('Chute um número de 0 a 5: '))
if num == ia:
    print('Meus parabéns, você venceu!')
else:
    print('Você não acertou, você pensou {} e o número era {}'.format(num,ia))
print('Fim do jogo')
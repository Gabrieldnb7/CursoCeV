from random import randint
ia = randint(1, 10)
tentativas = 0
numero = 0
print('O computador pensou em um número de 1 a 10. Você consegue descobrir qual?')
while numero != ia:
    numero = int(input('Chute um valor de 1 a 10: '))
    tentativas += 1
    if numero < ia:
        print('Mais... Tente novamente.')
    elif numero > ia:
        print('Menos... Tente novamente.')
print('Você acertou! Você precisou de {} tentativas.'.format(tentativas))
from random import randint
print('{:^30}'.format('Jogo do Par ou Ímpar'))
jogador = computador = soma = contador = 0
resposta = ''
while True:
    jogador = int(input('Escolha um número: '))
    escolha = str(input('Par ou ímpar?[P/I]: ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar?[P/I]: ')).upper().strip()[0]
    computador = randint(0,10)
    soma = jogador + computador
    if soma % 2 == 0:
        resposta = 'Par'
    else:
        resposta = 'Ímpar'
    print(f'O computador escolheu o número {computador} e você escolheu {jogador}, somando totaliza {soma}. Deu {resposta}.')
    if escolha == resposta[0]:
        print('Parabéns! Você ganhou')
        contador += 1
    else:
        break
print(f'Você perdeu! Conseguiu ganhar {contador} vezes seguidas.')

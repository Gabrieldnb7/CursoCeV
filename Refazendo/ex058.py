from random import randint
escolha = -1
palpites = 0
computador = randint(0, 10)
print(f'O computador pensou em um número de 0 a 10.')
while escolha != computador:
    escolha = int(input('Digite seu palpite: '))
    palpites += 1
    if escolha == computador:
        print('Você acertou!')
    else:
        print('Mais...Tente outro número:' if escolha < computador else 'Menos...Tente outro número: ')
print(f'Fim do jogo. Você acertou com {palpites} palpites')

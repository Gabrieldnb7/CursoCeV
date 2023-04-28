from random import randint
soma = vitórias = 0
print(f'{"Jogo do Par ou Ímpar":^30}')
while True:
    computador = randint(0, 10)
    escolha = (str(input('Par ou ímpar? '))).strip().lower()
    if escolha not in 'parimpar':
        escolha = (str(input('Escolha incorreta. Par ou impar: ')))
    número = int(input('Escolha um número entre 0 e 10: '))
    soma = número + computador
    print(f'Você jogou {número} e o computador jogou {computador}!')
    if soma % 2 == 0:
        vencedor = 'par'
    else:
        vencedor = 'impar'
    if escolha != vencedor:
        break
    elif escolha == vencedor:
        print('Parabéns! você ganhou!')
        print('Vamos denovo!')
        vitórias += 1
print(f'Você perdeu! Com um total de {vitórias} vitórias consecutivas.')

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte')
while True:
    while True:
        número = int(input('Digite um número entre 0 e 20: '))
        if 0 <= número <= 20:
            break
        print('Resposta inválida.', end=' ')
    print(f'Você digitou o número {extenso[número]}')
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('Fim do programa.')

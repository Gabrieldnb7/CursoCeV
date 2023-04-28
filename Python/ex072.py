# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
resposta = ''
números = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuário = int(input('Digite um número entre 0 e 20: '))
    while usuário < 0 or usuário > 20:
        usuário = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    print(f'Você digitou o número {números[usuário]}')
    resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print('Fim do programa')
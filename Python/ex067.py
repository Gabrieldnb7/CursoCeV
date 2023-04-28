import math
número = 0
print('-'*30)
print('{:^30}'.format('Tabuada'))
print('-'*30)
while True:
    número = int(input('Digite um número(Número negativo termina o programa): '))
    if número < 0:
        break
    for c in range(1,11):
        print(f'{número} x { c} = {número*c}')
print('-'*30)
print('{:^30}'.format('Fim do Programa.'))
print('-'*30)
t1 = int(input('digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
totaltermos = 10
termos = t1
contador = 1
resposta = -1
while resposta != 0:
    while contador <= totaltermos:
        print(f'{termos} -> ', end='')
        termos += razão
        contador += 1
    print('PAUSA')
    resposta = int(input('\nDigite quantos termos a mais você quer ver[0 para interromper]:'))
    totaltermos += resposta
print(f'Progressão finalizada com {totaltermos} termos mostrados.')
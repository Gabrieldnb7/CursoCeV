t1 = int(input('digite o primeiro termo da PA: '))
razão = int(input('digite a razão da PA: '))
termos = t1
contador = 1
while contador <= 10:
    print(f'{termos} -> ',end='')
    termos += razão
    contador += 1
print('Fim do programa')

t1 = int(input('Digite o valor do primeiro termo: '))
razão = int(input('Digite o valor do primeiro termo: '))
termos = t1
contador = 1
total = 0
maistermos = 10
while maistermos != 0:
    total += maistermos
    while contador <= total:
        print('{} -> '.format(termos), end='')
        termos += razão
        contador += 1
    print('Pausa.')
    maistermos = int(input('Quantos termos você quer ver a mais?'))
print('Fim da Progressão Aritmetica. Foram mostrados {} termos'.format(total))

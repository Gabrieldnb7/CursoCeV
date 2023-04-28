cédulas = 50
totaldenotas = 0
print('{:^30}'.format('Caixa Eletrônico'))
saque = int(input('Digite o valor a ser sacado: R$'))
total = saque
while True:
    if total >= cédulas:
        total -= cédulas
        totaldenotas += 1
    else:
        if totaldenotas > 0:
            print(f'Total de {totaldenotas} cédulas de {cédulas} reais')
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 1
        totaldenotas = 0
        if total == 0:
            break
print('{:-^40}'.format(' Fim do Programa '))
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep


def linha():
    print('=' * 40)


def maior(*núm):
    maior = 0
    print('Analisando os valores...')
    for index, valor in enumerate(núm):
        if index == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    for n in núm:
        print(f'{n}', end=' ')
        sleep(0.5)
    print()

    print(f'Dentre os valores, o maior é {maior}')



linha()
maior(2, 9, 4, 5, 7, 1)
linha()
maior(4,7,0)
linha()
maior(1,2)
linha()
maior(6)
linha()
maior()


print(f'{"Fim da análise":^40}')
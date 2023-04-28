#Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#A) de 1 até 10, de 1 em 1.
#B) de 10 até 0, de 2 em 2.
#C) Uma contagem personalizada.
from time import sleep


def contador(a, b, c):
    print(f'Contagem de {a} até {b} pulando de {c} em {c}:')
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
        #for cont in range(a, b, c):
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont += c
        print()
    else:
        cont = a
        while cont >= b:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont -= c
        print()


def fimdacontagem():
    print(f'{"Fim da contagem":=^35}')


contador(a=1, b=10, c=1)
fimdacontagem()
contador(a=10, b=0, c=2)
fimdacontagem()
n1 = int(input('Início da contagem: '))
n2 = int(input('Fim da contagem: '))
passo = int(input('Pulando de quanto? '))

contador(n1, n2, passo)
fimdacontagem()

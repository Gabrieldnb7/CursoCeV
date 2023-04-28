# Faça um programa que tenha uma lista chamada números e duos funções chamadas sorteia() e  somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
números = list()


def sorteia():
    for cont in range(0,5):
        números.append(randint(1, 10))
    print(f'Sorteei os números ', end='')
    for num in números:
        print(f'{num}', end=', ')
        sleep(0.5)
    print()


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores PARES do sorteio é {soma}.')


sorteia()
somaPar(números)

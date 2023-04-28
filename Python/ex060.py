# Faça um programa que leia um número qualquer e mostre o seu fatorial.
import math
from math import factorial
fatorial = 0
resposta = 'S'
while resposta == 'S':
    fatorial = int(input('Digite um número a ser fatorado: '))
    conta = math.factorial(fatorial)
    print('O resultado do fatorial do número {} é {}'.format(fatorial, conta))
    resposta = str(input('Deseja continuar?[S/N] ')).upper()
print('Fim do programa')
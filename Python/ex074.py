# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
menor = maior = 0
from random import randint
números = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os números sorteados foram {números}')
for contador in range(0,len(números)):
    if contador == 1 or maior < números[contador]:
        maior = números[contador]
    if contador == 1 or menor > números[contador]:
        menor = números[contador]
print(f'O maior número na lista é {maior} e o menor é {menor}')
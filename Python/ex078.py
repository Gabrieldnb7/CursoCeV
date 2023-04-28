# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
maior = menor = 0
while True:
    valores.append(int(input('Digite um número: ')))
    if len(valores) == 5:
        break
for posição, valor in enumerate(valores):
    if posição == 0 or maior < valor:
        maior = valores[posição]
    if posição == 0 or menor > valor:
        menor = valores[posição]

print(f'Sua lista é {valores}')
print(f'O maior valor da lista é {maior} na posição:', end=' ')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice},', end='')
print()
print(f'O menor valor da lista é {menor} na posição:', end=' ')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice},', end='')
print()

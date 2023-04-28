listanumeros = []
maior = menor = 0
for c in range(0,5):
    listanumeros.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = listanumeros[c]
    else:
        if maior < listanumeros[c]:
            maior = listanumeros[c]
        if menor > listanumeros[c]:
            menor = listanumeros[c]
print(f'Sua lista é {listanumeros}')
print(f'O maior valor é {maior} na posição: ', end='')
for indice, valor in enumerate(listanumeros):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor é {menor} na posição: ', end='')
for indice, valor in enumerate(listanumeros):
    if valor == menor:
        print(f'{indice}...', end='')
print()

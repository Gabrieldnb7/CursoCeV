números = []
posmaior = []
posmenor = []
for contador in range(1,6):
    números.append(int(input(f'Digite o {contador}º número: ')))
print(f'A lista de números é {números}')
for indice,valor in enumerate(números):
    if indice == 0:
        maior = menor = números[indice]
    if números[indice] > maior:
        maior = números[indice]
    if números[indice] < menor:
        menor = números[indice]
    if valor == maior:
        posmaior.append(indice)
    elif valor == menor:
        posmenor.append(indice)

print(f'O maior valor é {maior} nas posições {posmaior}.')
print(f'O menor valor é {menor} nas posições {posmenor}.')

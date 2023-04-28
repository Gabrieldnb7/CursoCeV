valores = list()
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
# valores.sort()
# print(valores)
for posicao, valor in enumerate(valores):
    print(f'{valor} na posição {posicao+1},', end=' ')
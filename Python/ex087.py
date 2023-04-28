# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores digitados
# A soma dos valores da terceira coluna
# O maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = soma3coluna = maiorvalor2linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor na posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {somapares}.')
for linha in range(0, 3):
    soma3coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma3coluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maiorvalor2linha = matriz[1][coluna]
    elif maiorvalor2linha < matriz[1][coluna]:
        maiorvalor2linha = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorvalor2linha}.')
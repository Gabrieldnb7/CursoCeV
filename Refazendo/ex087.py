matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapares = terceiracoluna = maiorvalor2 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para a posição {linha,coluna}'))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        if coluna == 2:
            terceiracoluna += matriz[linha][coluna]
        if linha == 1 or matriz[1][coluna] > maiorvalor2:
            maiorvalor2 = matriz[linha][coluna]
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {terceiracoluna}.')
print(f'O maior valor da segunda linha é {maiorvalor2}.')

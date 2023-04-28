num = int(input('Digite um número qualquer: '))
contador = num
fatorial = 1
print(f'Calculando {num}!')
while contador > 0:
    print(f'{contador}', end='')
    print(f'x' if contador > 1 else f' = {fatorial}', end='')
    fatorial = fatorial * contador
    contador -= 1
print('\nFim do programa')

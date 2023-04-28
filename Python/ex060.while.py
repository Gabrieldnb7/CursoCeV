número = int(input('Digite um número a ser fatorado: '))
contador = número
fatorial = 1
print('Calculando {}! '.format(número), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print('x' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)
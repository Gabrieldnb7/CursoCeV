n = int(input('Digite um número: '))
### d são os divisores, sendo maiores que 2, o número não será primo
d = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        d += 1
        ### d+= 1 corresponde ao somatório dos números divisiveis pelo número do input
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisivel {} vezes'.format(n, d))
if d == 2:
    print('Sendo assim, o número é primo.')
else:
    print('Sendo assim, o número não é primo.')
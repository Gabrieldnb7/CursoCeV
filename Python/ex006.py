n = int(input('Insira um número: '))
print('O dobro de {} é \033[1;33m{}\033[m, \
O triplo é \033[1;34m{}\033[m \
A raiz quadrada é \033[1;35m{:.3f}\033[m'.format(n, n*2, n*3, (n**(1/2))))

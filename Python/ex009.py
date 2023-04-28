n = int(input('Insira um número: '))
cores = {'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m',
         'cinza':'\033[1;37m',
         'branco':'\033[1;30m',
         'limpa':'\033[m'}
print('{}{} x  1 = {}{}'.format(cores['vermelho'], n, n*1, cores['limpa']))
print('{}{} x  2 = {}{}'.format(cores['verde'], n, n*2, cores['limpa']))
print('{}{} x  3 = {}{}'.format(cores['amarelo'], n, n*3, cores['limpa']))
print('{}{} x  4 = {}{}'.format(cores['azul'], n, n*4, cores['limpa']))
print('{}{} x  5 = {}{}'.format(cores['roxo'], n, n*5, cores['limpa']))
print('{}{} x  6 = {}{}'.format(cores['ciano'],n, n*6, cores['limpa']))
print('{}{} x  7 = {}{}'.format(cores['cinza'],n, n*7, cores['limpa']))
print('{}{} x  8 = {}{}'.format(cores['branco'],n, n*8, cores['limpa']))
print('{}{} x  9 = {}{}'.format(cores['vermelho'], n, n*9, cores['limpa']))
print('{}{} x 10 = {}{}'.format(cores['verde'], n, n*10, cores['limpa']))
print('{:=^30}'.format('='))

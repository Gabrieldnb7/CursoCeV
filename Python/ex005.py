n = int(input('\033[1;31mInsira um número\033[m: '))
print('O número {} tem como antecessor \033[1;32m{}\033[m e sucessor \033[1;33m{}\033[m'.format(n, n-1, n+1))

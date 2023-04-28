p = float(input('Insira o valor do produto: R$'))
print('Sendo R$\033[32m{:.2f}\033[m o valor do produto, com 5% de desconto ele será no valor de R$\033[32m{:.2f}\033[m'.format(p, p*0.95))

n1 = int(input("Digite o primeiro número: "))
n2 = int(input('Digite o segundo número: '))
cores = {'limpa' : '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
s = n1 + n2
print('A soma de {}{}{} mais {}{}{} é igual a {}.'.format(cores['vermelho'], n1, cores['limpa'], cores['verde'], n2, cores['limpa'], s))

número = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para binário é {}'.format(número, bin(número)[2:]))
elif opção == 2:
    print('O número {} convertido para octal é {}'.format(número, oct(número)[2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}'.format(número, hex(número)[2:]))
else:
    print('Está opção não está listada')

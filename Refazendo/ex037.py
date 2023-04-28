número = int(input('Digite um número: '))
resposta = int(input('Qual será a base de conversão?\n[ 1 ] para Binário\n[ 2 ] para Octal\n[ 3 ] para Hexadecimal\nSua opção: '))
if resposta == 1:
    print(f'{número} convertido para Binário é {bin(número)[2:]}')
elif resposta == 2:
    print(f'{número} convertido para Octal é {oct(número)[2:]}')
elif resposta == 3:
    print(f'{número} convertido para Hexadecimal é {hex(número)[2:]}')
else:
    print('Opção incorreta, tente novamente.')
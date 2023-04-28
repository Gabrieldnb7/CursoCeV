num = int(input('Digite um número: '))
escolha = input('Escolha a opção de conversão.\n [1] para BINÁRIO \n [2] para OCTAL \n [3] para HEXADECIMAL.\n Sua escolha:')
if escolha == '1':
    print('O número {} convertido para binário é {}'.format(num, bin(num)))
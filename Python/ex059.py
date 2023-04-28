resposta = 0
maiorvalor = 0
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while resposta != 5:
        print('Menu de Analise de Números')
        print('O que deseja fazer?')
        print('     [1] Somar os números')
        print('     [2] Multiplicar os números')
        print('     [3] Maior dentre eles')
        print('     [4] Digitar novos números')
        print('     [5] Sair do programa')
        resposta = int(input('Digite sua resposta: '))
        if resposta == 1:
            soma = n1 + n2
            print('A soma dos valores {} e {} é {}'.format(n1,n2,soma))
        if resposta == 2:
            multiplicar = n1 * n2
            print('A resultado da multiplicação dos valores {} e {} é {}'.format(n1,n2,multiplicar))
        if resposta == 3:
            maiorvalor = n1
            if n2 > maiorvalor:
                maiorvalor = n2
            print('O maior valor entre {} e {} é {}'.format(n1,n2,maiorvalor))
        if resposta == 4:
            n1 = int(input('Digite o 1º valor: '))
            n2 = int(input('Digite o 2º valor: '))
print('Fechando o programa.')
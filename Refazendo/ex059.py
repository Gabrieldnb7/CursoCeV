n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = maior = 0
print('''Analisador de números
O que deseja fazer?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Mostrar o maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa''')
while escolha != 5:
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}')
    elif escolha == 2:
        print(f'O resultado da multiplicação de {n1} * {n2} é {n1*n2}')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre {n1} e {n2} é {maior}')
        elif n2 > n1:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é {maior}')
        elif n1 == n2:
            print(f'Ambos os números são iguais.')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if escolha not in 12345:
        print('Opção inválida, tente novamente.')
print('Fim do programa')

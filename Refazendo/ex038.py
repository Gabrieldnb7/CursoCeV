#maior = menor = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = menor = n1
if n1 > n2:
    menor = n2
    print(f'O número {n1} é maior que {n2}')
elif n1 < n2:
    maior = n2
    print(f'O número {n2} é maior que {n1}')
elif n1 == n2:
    print(f'Ambos os números são iguais, logo não há um maior.')
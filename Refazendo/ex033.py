maior = 0
menor = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = menor = n1
if maior < n2:
    maior = n2
if maior < n3:
    maior = n3
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
print(f'O maior número é {maior} e o menor é {menor}')

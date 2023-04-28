#a = int(input('Digite o primeiro número: '))
#b = int(input('Digite o segundo número: '))
#c = int(input('Digite o terceiro número: '))
#d = int(input('Digite o quarto número: '))
#números = (a, b, c, d)
números = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))
print(f'Os números digitados foram: {números}')
print(f'O número 9 apareceu {números.count(9)} vezes.')
if 3 in números:
    print(f'O número 3 apareceu primeiro na {números.index(3)+1}ª posição.')
else:
    print(f'O número 3 não apareceu em nenhuma posição.')
print(f'Os números pares são:', end=' ')
for num in números:
    if num != 0:
        if num % 2 == 0:
            print(f'{num}', end=' ')

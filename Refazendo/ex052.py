num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1): # nessa lógica, cada laço servirá para identificar os divisores do número
    if num % c == 0: # condicional para os divisores + total de divisores do número
        print(f'\033[33m{c}\033[m', end=' ')
        total += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} tem {total} divisores, ', end='')
if total == 2:
    print(f'logo ele é um número primo.')
else:
    print(f'logo ele não é um número primo.')

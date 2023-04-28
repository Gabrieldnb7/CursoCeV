# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.
a = int(input('Digite um valor qualquer: '))
b = int(input('Digite outro valor:'))
c = int(input('Digite mais um: '))
d = int(input('Digite o último valor:'))
números = (a, b, c, d)

# ou substituir o a,b,c,d pelo texto do input. Ex. numeros = (int(input('digite um numero'), ...)

print(números)
print(f'O número 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O primeiro 3 apareceu na posição {números.index(3) + 1}')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print(f'Os números pares digitados são:', end=' ')
for n in números:
    if n % 2 == 0:
        print(f'{n}, ',end='')
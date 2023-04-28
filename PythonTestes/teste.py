#n = 'José'
#i = 25
#print('Você se chama {n} e tem {i} anos de idade')
maiorvalor = 0
for n in range(1,4):
    numero = int(input('Digite o {}º número: '.format(n)))
    if n == 1:
        maiorvalor = numero
    else:
        if numero > maiorvalor:
            maiorvalor = numero
print('O maior valor lido é {}'.format(maiorvalor))
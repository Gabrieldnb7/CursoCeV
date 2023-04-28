### Fstrings
#nome = 'José'
#idade = 33
#salário = 1050
#print(f'o {nome} tem {idade} anos e ganha R${salário:.2f}')
número = soma = 0
while True:
    número = int(input('Digite um número: '))
    if número == 999:
        break
    soma += número
print(f'A soma vale {soma}')
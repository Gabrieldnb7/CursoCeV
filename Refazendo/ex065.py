número = média = maior = soma = total = 0
menor = 99999
resposta = ' '
while resposta not in 'Nn':
    número = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]: ')).strip()[0]
    soma += 1
    total += número
    if número > maior:
        maior = número
    elif número < menor:
        menor = número
média = total/soma
print(f'Você digitou {soma} números.')
print(f'A média de todos os números digitados foi {média}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')

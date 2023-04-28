numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado não será adicionado a lista.')
    resposta = ' '
    while resposta not in 'NnSs':
        resposta = str(input('Quer continuar?[S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
numeros.sort()
print(f'Sua lista em ordem crescente é {numeros}')
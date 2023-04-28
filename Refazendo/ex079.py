lista = []
while True:
    número = int(input('Digite um número: '))
    if número in lista:
        print(f'Número duplicado não será adicionado.')
    else:
        lista.append(número)
        print('Valor adicionado com sucesso.')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] ')).strip()[0]
    if resp in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}.')

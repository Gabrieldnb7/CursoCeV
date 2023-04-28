lista = list()
contador = 0
while True:
    número = int(input('Digite um número: '))
    lista.append(número)
    contador += 1
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar?[S/N] '))
    if resposta in 'Nn':
        break
lista.sort(reverse=True)
print(f'{contador} números foram digitados.')
print(f'A lista na ordem decrescente é: {lista}')
if 5 in lista:
    for index, num in enumerate(lista):
        if num == 5:
            print(f'O número 5 está na lista na posição {index}')
else:
    print('O número 5 não está presente na lista')

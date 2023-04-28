soma = contador = p1000 = menor = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: R$'))
    soma += preço
    contador += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        p1000 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Suas compras totalizaram R${soma:.2f}')
print(f'{p1000} produtos custam mais de R$1000')
print(f'O produto com menor valor foi {barato} custando R${menor:.2f}')
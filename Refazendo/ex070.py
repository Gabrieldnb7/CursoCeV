compra = caro = contador = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço do produto: R$'))
    compra += preço
    contador += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        caro += 1
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar?[S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
print(f'Valor total: R${compra:.2f}')
print(f'{caro} produto(s) custam mais de R$1000.00')
print(f'O produto mais barato é {barato} que custa {menor:.2f}')

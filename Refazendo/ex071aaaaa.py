ced50 = ced20 = ced10 = ced1 = 0
montante = int(input('Digite o valor a ser sacado: R$'))
total = montante
while True:
    while total > 50:
        ced50 = total // 50
        total -= ced50*50
    while total > 20:
        ced20 = total // 20
        total -= ced20*20
    while total > 10:
        ced10 = total // 10
        total -= ced10*10
    while total > 1:
        ced1 = total
        total -= ced1
    if total == 0:
        break
print(f'''Você sacou um total de R${montante} sendo:)
{ced50} notas de R$50'
{ced20} notas de R$20'
{ced10} notas de R$10
{ced1} notas de R$1''')
print('Saque encerrado. Volte Sempre!')

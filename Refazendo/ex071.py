'''ced50 = ced20 = ced10 = ced1 = 0
while True:
    montante = int(input('Digite o valor a ser sacado: R$'))
    ced50 = (montante % 50 == 0)
    montante -= ced50*50
    if montante == 0:
        break
print(f'Você sacou um total de {montante} sendo:\n{ced50} notas de 50')
print('Saque encerrado. Volte Sempre!')'''
totaldecedulas = total = 0
cedulas = 50
while True:
    montante = int(input('Digite o valor a ser sacado: R$'))
    total = montante
    if totaldecedulas == 0:
        total -= cedulas
        totaldecedulas += 1
    if total > 0:
        total

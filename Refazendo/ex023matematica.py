número = int(input('Digite um número entre 0 e 9999: '))
print(f'Milhar = {número // 1000 % 10:.0f}')
print(f'Centena = {número // 100 % 10:.0f}')
print(f'Dezena = {número // 10 % 10:.0f}')
print(f'Unidade = {número // 1 % 10:.0f}')
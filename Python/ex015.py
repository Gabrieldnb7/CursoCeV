dias = int(input('Por quantos dias o veículo foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
print('O valor do aluguel será de R${:.2f}'.format((dias*60)+(km*0.15)))

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média é {}, parabéns'.format(m) if m >=6 else 'Sua média de {} foi baixa, estude mais!'.format(m))
print('Fim do semestre')

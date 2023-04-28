km = int(input('Informe a distância da viagem em Km: '))
if km <= 200:
    print('O valor total da sua viagem será de R${:.2f}'.format(km*0.5))
else:
    print('O valor total da sua viagem será de R${:.2f}'.format(km*0.45))
print('Fim')
distância = int(input('Digite a distância da viagem em Km: '))
if distância > 200:
    preço = distância*0.45
    print(f'Viajando uma distância de {distância}km a passagem terá o preço de R${preço:.2f}')
else:
    preço = distância*0.5
    print(f'Viajando uma distância de {distância}km a passagem ficará no valor de R${preço:.2f}')
print('Fim.')

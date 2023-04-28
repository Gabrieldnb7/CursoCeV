distancia = int(input('Digite a distancia da viagem: '))
preço = distancia * 0.50 if distancia <= 200 else distancia*0.45
print(f'Viajando {distancia}km o preço da viagem será R${preço:.2f}')
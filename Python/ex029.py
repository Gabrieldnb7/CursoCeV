v = int(input('Digite a velocidade do veículo em Km/h: '))
if v > 80:
    print('Você ultrapassou o limite de velocidade e foi multado em R${:.2f}'.format((v-80)*7))
print('Tenha um bom dia e dirija com segurança!')

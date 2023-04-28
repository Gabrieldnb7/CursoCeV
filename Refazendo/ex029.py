velocidade = int(input('Qual a velocidade em km/h: '))
if velocidade > 80:
    print(f'Você foi multado! O valor da multa é de R${(velocidade-80)*7:.2f}')
else:
    print(f'Você está dentro do limite de velocidade.')
print('Dirija sempre com segurança.')
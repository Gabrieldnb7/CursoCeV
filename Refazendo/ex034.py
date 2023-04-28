salário = float(input('Digite o valor do seu salário R$: '))
if salário <= 1250:
    aumento = 0.15
    print(f'Com um aumento de 15% seu novo salário será R${salário + salário * aumento:.2f}')
else:
    aumento = 0.10
    print(f'Com um aumento de 10% seu novo salário será R${salário+ salário * aumento:.2f}')
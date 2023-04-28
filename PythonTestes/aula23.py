num = 0
while True:
    número = str(input('Digite um número: '))
    try:
        if número.isnumeric():
            num = int(número)
    except:
        print('Erro! Insira um número real válido')
    else:
        print(f'Você digitou o número {num}')
        break
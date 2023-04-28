from datetime import date
print('ALISTAMENTO OBRIGATÓRIO DO EXÉRCITO BRASILEIRO')
sexo = str(input('Digite o seu sexo [F/M]: ')).strip()
if sexo in 'Mm':
    nascimento = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nascimento
    #alistar = date.today().year - nascimento
    print(f'Você tem {idade} anos em {date.today().year}')
    if idade < 18:
        print(f'Seu alistamento acontecerá a partir do ano de {nascimento+18}, faltam {18-idade} anos.')
    elif idade == 18:
        print(f'Você está convocado a se apresentar ao Exército.')
    elif idade > 18:
        print(f'O período do seu alistamento venceu no ano de {nascimento+18}.')
else:
    print('Não é necessário que você se apresente ao alistamento obrigatório.')
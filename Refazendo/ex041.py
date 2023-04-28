from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos e está na modalidade MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e está na modalidade INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e está na modalidade JUNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e está na modalidade SENIOR.')
elif idade > 25:
    print(f'O atleta tem {idade} anos e está na modalidade MASTER.')

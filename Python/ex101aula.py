def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f'Com {idade} anos: Não vota.')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: Voto opcional.')
    else:
        return print(f'Com {idade} anos: Voto Obrigatório.')


voto(int(input('Ano de nascimento: ')))

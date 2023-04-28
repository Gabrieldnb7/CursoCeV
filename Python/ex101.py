# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, obrigatório ou opcional nas eleições.
def voto(data):
    from datetime import date
    resposta = ''
    idade = date.today().year - data
    if 18 <= idade < 65:
        resposta = 'Voto Obrigatório'
    elif idade < 16:
        resposta = 'Não vota'
    elif idade >= 65 or 16 <= idade < 18:
        resposta = 'Voto opcional'
    print(f'Com {idade} anos: {resposta}')
    return resposta


nascimento = int(input('Ano de nascimento: '))
voto(nascimento)

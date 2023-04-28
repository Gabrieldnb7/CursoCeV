maiores = homens = mulheres20 = 0
print(f'{"Cadastro de pessoas":^35}')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo[F/M]: ')).strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = (str(input('Quer continuar?[S/N]'))).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres20 += 1
    if resposta in 'N':
        break
print(f'No total foram cadastrados {maiores} com mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres20} mulheres possuem menos de 20 anos.')

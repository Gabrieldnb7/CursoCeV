contador = homens = mulher20 = 0
print('{:-^50}'.format('Cadastro de Pessoas'))
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo[F/M]: ')).upper().strip()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if idade >= 18:
        contador += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulher20 += 1
    if resposta in 'N':
        break
print('Fim do cadastro.')
print(f'{contador} pessoas são maiores de 18 anos.\n{homens} homens foram cadastrados. \n{mulher20} mulheres possem menos de 20 anos')

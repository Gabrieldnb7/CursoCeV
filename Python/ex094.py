# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com a idade acima da média
temp = {}
pessoas = []
mulheres = []
acimadamédia = []
média = soma = 0
while True:
    temp['Nome'] = str(input('Nome: '))
    while True:
        temp['Sexo'] = str(input('Sexo[F/M]: ')).strip()[0]
        if temp['Sexo'] in 'MmFf':
            break
        else:
            print('Erro! Digite somente F ou M.')
#    while temp['Sexo'] not in 'FfMm':
#        temp['Sexo'] = str(input('Erro! Digite somente F ou M.')).strip()[0]
    temp['Idade'] = int(input('Idade: '))
    pessoas.append(temp.copy())
    temp.clear()
    while True:
        resp = str(input('Quer continuar?[S/N] ')).strip()[0]
        if resp not in 'SsNn':
            print('Erro! Digite somente S ou N.')
        else:
            break
#    while resp not in 'SsNn':
#        resp = str(input('Erro! Digite somente S ou N.')).strip()[0]
    if resp in 'Nn':
        break
for pessoa in pessoas:
    soma += pessoa['Idade']
média = soma / len(pessoas)
for pessoa in pessoas:
    if pessoa['Sexo'] in 'Ff':
        mulheres.append(pessoa)
print(f'No total foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade do grupo é {média:.0f}.')
print(f'As mulheres presentes no grupo são:', end=' ')
for mulher in mulheres:
    print(f'{mulher["Nome"]}', end=', ')
print()
for pessoa in pessoas:
    if pessoa['Idade'] > média:
        acimadamédia.append(pessoa)
print(f'A lista de pessoas com idade acima da média é:', end=' ')
for pessoa in acimadamédia:
    print(f'{pessoa["Nome"]} com {pessoa["Idade"]} anos', end=', ')
print()
print('Análise concluída.')

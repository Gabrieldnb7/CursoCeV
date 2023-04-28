# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista.
# No final mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) uma listagem com as pessoas mais leves
pessoas = []
listaprincipal = []
pesomaior = pesomenor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso em Kgs: ')))
    if len(listaprincipal) == 0:
        pesomaior = pesomenor = pessoas[1]
    else:
        if pessoas[1] > pesomaior:
            pesomaior = pessoas[1]
        if pessoas[1] < pesomenor:
            pesomenor = pessoas[1]
    listaprincipal.append(pessoas[:])
    pessoas.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break
print(f'O total de pessoas cadastradas é {len(listaprincipal)}')
print(f'O maior peso cadastrado é {pesomaior} e corresponde a ', end='')
for p in listaprincipal:
    if p[1] == pesomaior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso cadastrado é {pesomenor} e corresponde a ', end='')
for p in listaprincipal:
    if p[1] == pesomenor:
        print(f'[{p[0]}]', end='')
print()

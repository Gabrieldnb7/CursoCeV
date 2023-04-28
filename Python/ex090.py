# Faça um programa que leia nome e média de um aluno. Guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.
Aluno = dict()
Aluno['Nome'] = str(input('Nome: '))
Aluno['Média'] = float(input(f'Média de {Aluno["Nome"]}: '))
if Aluno['Média'] >= 6:
    Aluno['Situação'] = 'Aprovado'
elif 4.5 < Aluno['Média'] <= 6:
    Aluno['Situação'] = 'Recuperação'
else:
    Aluno['Situação'] = 'Reprovado'
for keys, values in Aluno.items():
    print(f'{keys} corresponde a {values}.')
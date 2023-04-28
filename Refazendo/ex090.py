Aluno = {}
Aluno['Nome'] = str(input('Nome: '))
Aluno['Média'] = float(input('Média: '))
if Aluno['Média'] < 5:
    Aluno['Situação'] = 'REPROVADO'
elif 5 <= Aluno['Média'] < 7:
    Aluno['Situação'] = 'RECUPERAÇÃO'
else:
    Aluno['Situação'] = 'APROVADO'
for chaves, valores in Aluno.items():
    print(f'{chaves} corresponde a {valores}')

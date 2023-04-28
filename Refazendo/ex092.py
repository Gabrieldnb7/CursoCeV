# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import date
inss = {}
inss['Nome'] = str(input('Nome: '))
data = int(input('Ano de nascimento: '))
idade = date.today().year - data
inss['Idade'] = idade
inss['CTPS'] = int(input('Carteira de trabalho(0 não tem): '))
if inss['CTPS'] != 0:
    inss['Contratação'] = int(input('Ano de contratação: '))
    inss['Salário'] = float(input('Salário: '))
    inss['Aposentadoria'] = idade + ((inss['Contratação'] + 35) - date.today().year)
for chaves, valores in inss.items():
    print(f'    {chaves} corresponde a {valores}')

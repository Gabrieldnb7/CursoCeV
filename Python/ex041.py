from datetime import date
print('\033[1;34mConfederação Nacional de Natação\033[m')
atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nasc
print('Este atleta possui {} anos, logo:'.format(idade))
if idade <= 9:
    print('Este(a) atleta está classificado como MIRIM.')
elif idade <= 14:
    print('Este(a) atleta está classificado como INFANTIL.')
elif idade <= 19:
    print('Este(a) atleta está classificado como JUNIOR.')
elif idade <= 25:
    print('Este(a) atleta está classificado como SENIOR.')
elif idade > 25:
    print('Este(a) atleta está classificado como MASTER.')
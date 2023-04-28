from datetime import date
print('\033[1;32mAlistamento Militar Obrigatório')
ano = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano
if idade < 18:
    print('Ainda não é necessário comparecer ao alistamento.')
    print('Faltam {} anos para você se alistar.'.format(18-idade))
elif idade == 18:
    print('Você deve comparecer ao alistamento este ano.')
elif idade > 18:
    print('Você já passou da idade para se alistar.')
    print('Já se passaram {} anos do seu alistamento.'.format(idade-18))
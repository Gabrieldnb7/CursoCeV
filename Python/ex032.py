from datetime import date
ano = int(input('Digite o ano(Se quiser analisar o ano atual, digite 0): '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 ==0:
    print('O ano {} é um ano bissexto')
else:
    print('O ano {} não é bissexto'.format(ano))
print('Fim')
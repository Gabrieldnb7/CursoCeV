from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    d = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - d
    maior += idade >= 18
    menor += idade < 18
print('{} pessoas são maiores de idade e {} são menores de idade'.format(maior,menor))
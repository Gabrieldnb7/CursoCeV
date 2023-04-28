soma = 0
media = 0
maior = 0
velho = ''
mulher20 = 0
for p in range (1,5):
    print('{}ª Pessoa'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: (M/F):')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if idade > maior and sexo in 'Mm':
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
media = soma/4
print('A média de idade é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,velho))
print('Há {} mulher(es) com menos de 20 anos'.format(mulher20))
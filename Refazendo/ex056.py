velho = ''
soma = somamulheres = média = maior = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]: ')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    elif sexo in 'Ff' and idade < 20:
        somamulheres += 1
    média = soma / 4
    if idade > maior and sexo in 'Mm':
        maior = idade
        velho = nome
print(f'A média de idade do grupo é {média:.0f} anos')
print(f'O homem mais velho tem {maior} se chama {velho}')
print(f'{somamulheres} mulher(es) possuem menos de 20 anos')

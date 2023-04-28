média = soma = contador = maiorvalor = menorvalor = número = 0
resposta = ''
while resposta != 'N':
    número = int(input('Digite um número: '))
    soma += número
    contador += 1
    if contador == 1:
        maiorvalor = menorvalor = número
    else:
        if número > maiorvalor:
            maiorvalor = número
        if número < menorvalor:
            menorvalor = número
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()
média = soma / contador
print('Você digitou {} números e a média é {}'.format(contador,média))
print('O maior valor foi {} e o menor foi {}'.format(maiorvalor,menorvalor))
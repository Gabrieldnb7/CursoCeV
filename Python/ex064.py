número = 0
soma = 0
total = 0
while número != 999:
    número = int(input('Digite um número entre 1 e 998(Digite 999 para terminar): '))
    if número != 999:
        soma += número
    total += 1
print('Você digitou um total de {} números e a soma desses números é {} '.format(total, soma))
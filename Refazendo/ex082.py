lista = []
par = []
ímpar = list()
while True:
    número = int(input('Digite um número: '))
    lista.append(número)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] ')).strip()[0]
    if resp in 'Nn':
        break
for num in lista:
    if num != 0:
        if num % 2 == 1:
            ímpar.append(num)
        else:
            par.append(num)
print(f'A lista de números é: {lista}')
print(f'A lista de números pares é: {par}')
print(f'A lista de números ímpares é :{ímpar}')

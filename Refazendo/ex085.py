par = []
ímpar = []
lista = [par, ímpar]
for cont in range(0,7):
    número = int(input(f'Digite o {cont+1}º número: '))
    if número != 0:
        if número % 2 == 0:
            #poderia ser: lista[0].append(número)
            par.append(número)
            print('Número adicionado na lista de pares.')
        else:
            #poderia ser: lista[1].append(número)
            ímpar.append(número)
            print('Número adicionado na lista de ímpares.')
    else:
        lista.insert(0, número)
        print('Número adicionado na lista')
par.sort()
ímpar.sort()
print(f'A lista completa é: {lista}')
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores impares são: {lista[1]}')

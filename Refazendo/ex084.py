lista = []
listapesados = []
listaleves = []
temp = []
#contador = \
maiorpeso = menorpeso = 0
while True:
    nome = str(input('Digite o seu nome: '))
    peso = float(input('Digite o seu peso: '))
    temp.append(nome)
    temp.append(peso)
    lista.append(temp[:])
    #contador += 1
    temp.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print(f'{len(lista)} pessoas foram cadastradas.')
for index,pessoa in enumerate(lista):
    if index == 0:
        maiorpeso = menorpeso = pessoa[1]
    elif pessoa[1] > maiorpeso:
        maiorpeso = pessoa[1]
    elif pessoa[1] < menorpeso:
        menorpeso = pessoa[1]
for pessoa in lista:
    if pessoa[1] == maiorpeso:
        listapesados.append(pessoa[0])
    elif pessoa[1] == menorpeso:
        listaleves.append(pessoa[0])
print(f'O maior peso é {maiorpeso} pertencente a(o) {listapesados}')
print(f'O maior peso é {menorpeso} pertencente a(o) {listaleves}')

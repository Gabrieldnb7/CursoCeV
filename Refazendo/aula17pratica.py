from random import randint
#lista = []
#lista = [randint(1,10), randint(1,10), randint(1,10),randint(1,10)]
lista = [8, 5, 6, 1, 3]
#for n in números:
    #lista.append(n)
'''while True:
    resp = ' '
    lista.append(int(input('Digite um número: ')))
    if resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break'''
'''lista.insert(3,9)
lista.pop(0)
#lista.sort(reverse=True)
print(f'{lista}')
print(f'O maior número da lista é {max(lista)}')
print(f'O menor número da lista é {min(lista)}')'''
valores = []
valores.append(1)
valores.append(8)
valores.append(5)
print(valores)
for chave, valor in enumerate(valores):
    print(f'Na posição {chave} achei o valor {valor}')
print(f'Fim do programa')

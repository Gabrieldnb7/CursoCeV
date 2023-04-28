# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e outra com os valores ímpares digitados.
# Ao final, mostre o contéudo das três listas geradas.

números = []
pares = []
ímpares = []
while True:
    números.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
for indíce, valor in enumerate(números):
    if valor != 0:
        if valor % 2 == 0:
            pares.append(valor)
        elif valor % 2 == 1:
            ímpares.append(valor)
print(f'A lista dos números é {números}')
print(f'A lista dos números pares é {pares}')
print(f'A lista dos números ímpares é {ímpares}')

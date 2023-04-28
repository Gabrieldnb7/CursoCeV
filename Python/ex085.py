# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
números = [[], []]

for c in range(0, 7):
    valor = (int(input('Digite um número: ')))
    if valor != 0:
        if valor % 2 == 0:
            números[0].append(valor)
        else:
            números[1].append(valor)
números[0].sort()
números[1].sort()
print(f'A lista de números pares é {números[0]}')
print(f'A lista de números ímpares é {números[1]}')

maior = menor = 0
for contador in range (1, 6):
    peso = float(input(f'Digite o {contador}º peso: '))
    if contador == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi {maior}kg e o menor foi {menor}kg')

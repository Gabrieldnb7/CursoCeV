num = int(input('Digite um número: '))
contador = num
fatorial = 1
for contador in range(contador,0, -1):
    fatorial *= contador
print(f'O fatorial de {num} é {fatorial}')
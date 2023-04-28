soma = 0
for contador in range(1,7):
    num = int(input(f'Digite o {contador}º número:'))
    if num % 2 == 0:
        soma += num
print(soma)
def fatorial(número):
    f = 1
    for cont in range(número, 0, -1):
        f *= cont
    return f


#Programa Principal
num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

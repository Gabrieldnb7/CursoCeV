'''def fatorial(num=1):
    fat = 1
    for contador in range(num, 0, -1):
        fat *= contador
    return fat


n1 = fatorial(5)
n2 = fatorial()
n3 = fatorial(3)
print(f'Os resultados foram {n1}, {n2}, {n3}')'''
# return também serve para retornar um valor logico. por exemplo:
def par(num=1):
    if num != 0:
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        print('0 Não é par nem ímpar')


num = int(input('Digite um número: '))
if par(num): # isso aqui buga a mente pq ele só pergunta em valor logico
    print('É par')
else:
    print('É impar')
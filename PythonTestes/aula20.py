# Funções
# definindo funções
'''def soma(a,b): # Sendo (a,b) o parâmetro de execução.
    print(f'A = {a} / B = {b}.')
    soma = a + b
    print(f'A soma de {a} + {b} é {soma}')


soma(8, 9)
soma(a=15, b=23)
soma(b=4, a=16)'''

'''# Utilizando empacotador de parâmetros
def contador(* num):


    tamanho = len(num)
    print(f'Recebi os valores {num} e ao total foram {tamanho} números')
contador(6, 0, 8, 4, 2)
contador(3, 3, 2, 11, 8, 9)
contador(2, 9, 15)'''
def quadrado(lista):
    print(f'Os valores são:', end=' ')
    for valor in lista:
        print(f'{valor}', end=' ')
    print()
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos]**2
        pos += 1


valores = [4, 9, 3, 12]
quadrado(valores)
print(valores)
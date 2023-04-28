# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição
# correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = []
for c in range(0,5):
    valor = int(input('Digite um número: '))
    if c == 0:
        valores.append(valor)
        print('Numéro adicionado ao final da lista.')
    elif valor > valores[-1]: # para pegar o último valor da lista
        valores.append((valor))
        print('Número adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len((valores)):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'Número adicionado na posição {posicao} da lista.')
                break
            posicao += 1
# Esse else tem o objetivo de verificar posição por posição da lista e inserir os valores menores nas posições correspondentes
print(f'Sua lista é {valores}')



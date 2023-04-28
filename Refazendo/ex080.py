lista = []
for contador in range(0,5):
    número = int(input('Digite um número: '))
    if contador == 0 or número > lista[-1]:
        lista.append(número)
        print('Número adicionado no fim na lista')
    else:
        for index,num in enumerate(lista): #esse codigo varrerá a lista posicionando o número no local adequado
            if número <= lista[index]:
                lista.insert(index, número)
                print(f'Número adicionado na posição {index} da lista.')
                break
print(lista)
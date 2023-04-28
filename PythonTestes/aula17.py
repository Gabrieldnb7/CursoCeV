lista = [1,5,6,10,3,4]
lista.insert(0, 5)
lista.sort(reverse=True)
# lista.pop()
# lista.append(5)
print(lista)
for número in lista:
    if 5 in lista:
        lista.remove(5)
print('Removendo os valores 5 da lista.')
print(f'A lista {lista} tem {len(lista)} elementos')
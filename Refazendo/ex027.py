nome = str(input('Digite o seu nome: ')).strip()
lista = nome.split()
print(lista)
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {lista[len(lista)-1]}')

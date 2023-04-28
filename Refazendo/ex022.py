nome = str(input('Digite o seu nome: ')).strip()
print(f'Maiúsculo: {nome.upper()}.')
print(f'Minúsculo: {nome.lower()}.')
separado = nome.split()
print(nome)
print(f'Quantas letras possui = {len(nome) - nome.count(" ")}')
print(f'Quantas letras tem o primeiro nome = {len(separado[0])}')
# outra forma de contar as letras do primeiro nome
# print(f'Quantas letras tem o primeiro nome = {nome.find(" ")}')
# encontrando a posição do primeiro espaço ele identifica a quantidade de caracteres
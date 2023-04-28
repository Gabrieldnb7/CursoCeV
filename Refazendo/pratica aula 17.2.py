pessoas = []
cadastro = []
for cont in range(0,5):
    nome = str(input('Digite seu nome: '))
    cadastro.append(nome)
    #sexo = str(input('Digite seu sexo:[F/M] ')).strip()[0]
    #cadastro.append(sexo)
    idade = int(input('Digite sua idade: '))
    cadastro.append(idade)
    pessoas.append(cadastro[:])
    cadastro.clear()
    #del cadastro[:]
print(f'O nome das pessoas cadastradas é', end=' ')
for pessoa in pessoas:
    print(pessoa[0], end=' ')

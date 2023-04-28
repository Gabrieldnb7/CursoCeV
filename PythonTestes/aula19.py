# pessoa = {'Nome' : 'Gabriel', 'Idade': '23', 'Sexo': 'M'}
# #del pessoa['Sexo']
# pessoa['peso'] = 54.6
# for keys, values in pessoa.items():
#     print(f'{keys} = {values}')
estado = {}
brasil = []
for c in range(1,4):
    estado['U.F.'] = str(input('Unidade federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for est in brasil:
    for values in est.values():
        print(values, end=' ')
    print()
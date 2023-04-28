#pessoas = {'nome':'Gabriel','sexo':'M','idade': 24}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#pessoas['peso'] = 58
#for keys,values in pessoas.items():
    #print(f'{keys} = {values}')
'''brasil = []
estado1 = {'Unidade Federativa': 'Distrito Federal', 'Sigla': 'DF'}
estado2 = {'Unidade Federativa': 'Alagoas', 'Sigla': 'AL'}
brasil.append(estado1)
brasil.append(estado2)
for estados in brasil:
    print(f'{estados["Unidade Federativa"]}', end='-')
    print(f'{estados["Sigla"]}')'''
estado = dict()
brasil = list()
for contador in range(0,3):
    estado['U.F.'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for estados in brasil:
    for valores in estados.values():
        print(valores, end=' ')
    print()

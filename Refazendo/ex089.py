boletim = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    média = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], média])
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print(f'{"Boletim":=^35}')
print(f'{"Nº":<5} {"Aluno:":<12} {"Média":>10}')
for index, alunos in enumerate(boletim):
    print(f'{index:<5}{alunos[0]:<10}{alunos[2]:>10}')
while True:
    maisnotas = int(input('Mostrar notas de quais alunos?[999 interrompe] '))
    if maisnotas == 999:
        break
    if maisnotas <= len(boletim):
        print(f'Notas de {boletim[maisnotas][0]} foram: {boletim[maisnotas][1]}')
print('Boletim finalizado.')

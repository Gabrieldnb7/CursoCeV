ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    if resposta == 'N':
        break
print('-' * 50)
print(f'{"Nº":<5}{"Nome":<10}{"Média":>10}')
print('-' * 50)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<5}{aluno[0]:<10}{aluno[2]:>10}')
while True:
    opcao = int(input('Mostrar notas de qual aluno?(999 Interrompe) '))
    if opcao == 999:
        break
    if opcao <= len(ficha) -1:
        print(f'As notas do Aluno {ficha[opcao][0]} são {ficha[opcao][1]}')
print('Fim do programa.')
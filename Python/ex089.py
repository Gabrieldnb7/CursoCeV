# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.
Aluno = [[''], [0], [0]]
Boletim = []
contador = média = 0
while True:
    Aluno[0] = str(input('Digite o nome do aluno(a): '))
    Aluno[1] = float(input('Digite a primeira nota do aluno(a): '))
    Aluno[2] = float(input('Digite a segunda nota do aluno(a): '))
    média = (Aluno[1] + Aluno[2])/2
    Boletim.append(Aluno[0])
    Boletim.append(média)
    Aluno.clear
    contador += 1
    resposta = ' '
    if resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N]').strip().upper())
        if resposta == 'N':
            break
print(Boletim)
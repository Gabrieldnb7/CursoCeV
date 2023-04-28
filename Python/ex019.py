from random import choice

n1 = str(input('Informe o nome do primeiro aluno: '))
n2 = str(input('Informe o nome do segundo aluno: '))
n3 = str(input('Informe o nome do terceiro aluno: '))
n4 = str(input('Informe o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
s = choice(lista)
print('O aluno sorteado é {}'.format(s))

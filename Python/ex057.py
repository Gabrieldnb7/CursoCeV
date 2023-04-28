# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto
genero = str(input('Digite o seu genêro:[M/F] ')).strip().upper()[0]
while genero not in 'MF':
    genero = str(input('Genêro invalido, tente novamente. \nDigite seu genêro:[M/F] ')).strip().upper()[0]
print('Genêro {} registrado'.format(genero))
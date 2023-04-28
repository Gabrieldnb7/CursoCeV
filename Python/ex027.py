nome = str(input('Digite seu nome completo: ')).strip().title()
separar = nome.split()
print('Seu primeiro nome é {}'.format(separar[0]))
print('Seu último nome é {}'.format(separar[len(separar)-1]))

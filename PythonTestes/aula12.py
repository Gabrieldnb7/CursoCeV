nome = str(input('Qual é o seu nome? '))
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome in 'Fernando Maria José Vitor':
    print('Seu nome é comum no Brasil.')
elif nome == 'Gustavo':
    print('O cara é brabo')
print('Muito prazer {}, tenha um bom dia!'.format(nome))
nome = 'Gabriel'
# Não é pra entender tudo, mas é uma forma de criar variável cores
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'pretoebranco': '\033[7;30m'}
# print('Prazer em te conhecer, {}{}{}!!!'.format('\033[4;36m', nome, '\033[m'))
print('Prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
